import json
import logging
from pypdf import PdfReader, PdfWriter
import os
from agentic_doc.parse import parse
from pydantic import BaseModel, Field
from typing import List, Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# File paths
pdf_path = "cls1975final.pdf"  # CHANGED: Using same PDF as 9-11 script
output_file = "CLS_1975_Roster_7to8.json"

# Set API Key
os.environ["VISION_AGENT_API_KEY"] = "djN0djRsczZ6Y25pNXdtYmIwYzV3Om13OGlSN2hHazJvWlNLamhBb1dRT0lYOUtwYkRuRGE1"

# NEW: Expected student counts for verification
EXPECTED_COUNTS = {
    "8": 99,  # 8th graders
    "7": 81   # 7th graders
}

# Define the Pydantic model for extraction schema
class StudentName(BaseModel):
    name: str = Field(description="The full name of the student as it appears next to their individual portrait photo in the roster section.")

class YearbookRosterExtraction(BaseModel):
    """Schema for extracting individual student roster data from yearbook pages."""
    
    grade_level: Optional[str] = Field(
        default=None, 
        description="The grade level or class year if visible. This may not be present on roster pages."
    )
    teacher_name: Optional[str] = Field(
        default=None, 
        description="Teacher names are typically not present on high school roster pages."
    )
    students: List[StudentName] = Field(
        description="Extract ONLY students from individual portrait roster sections. Look for: individual student headshot photos arranged in a grid pattern or a cross patter with names listed directly next to or below each photo."
    )

def get_grade_from_page(page_num):
    """Determine grade level based on cls1975final.pdf layout"""
    if 50 <= page_num <= 55:
        return "8"  # 8th grade
    elif 56 <= page_num <= 61:
        return "7"  # 7th grade
    else:
        return "SKIP"  # Pages outside our range

def extract_single_page_data():
    """Extract student data for grades 7-8 using LandingAI library."""
    logging.info(f"Starting extraction from {pdf_path}")
    logging.info("Processing pages 50-61 only (8th Grade: 50-55, 7th Grade: 56-61)")
    
    all_students = []
    successful_extractions = []
    failed_pages = []
    pages_by_grade = {"7": [], "8": []}
    
    # NEW: Initialize raw page data and teacher tracking
    all_extractions = []
    teachers_found = []
    grade_teacher_combinations = []
    
    try:
        # Read the PDF
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        logging.info(f"PDF has {total_pages} total pages. Processing pages 50-61 only.")
        
        # CHANGED: Process only pages 50-61 (using 0-based indexing)
        for page_idx in range(49, 61):  # 49-60 in 0-based = 50-61 in 1-based
            page_num = page_idx + 1  # Convert to 1-based for display
            page_name = f"page_{page_num}"
            
            # Get grade for this page
            grade = get_grade_from_page(page_num)
            
            if grade == "SKIP":
                continue  # This shouldn't happen with our range
            
            logging.info(f"Processing {page_name} (Grade {grade})")
            pages_by_grade[grade].append(page_num)
            
            # Create temporary PDF for single page
            temp_page_path = f"temp_{page_name}.pdf"
            writer = PdfWriter()
            writer.add_page(reader.pages[page_idx])
            
            with open(temp_page_path, "wb") as temp_file:
                writer.write(temp_file)
            
            try:
                # Process with LandingAI library
                logging.info(f"Extracting from {page_name}...")
                results = parse(temp_page_path, extraction_model=YearbookRosterExtraction)
                
                if results and len(results) > 0:
                    result = results[0]
                    extracted_data = result.extraction
                    
                    if extracted_data and extracted_data.students and len(extracted_data.students) > 0:
                        # Successful extraction
                        page_result = {
                            "page_name": page_name,
                            "page_number": page_num,
                            "extraction": {
                                "grade_level": extracted_data.grade_level,
                                "teacher_name": extracted_data.teacher_name,
                                "students": [{"name": student.name} for student in extracted_data.students]
                            },
                            "success": True,
                            "failure_reason": None
                        }
                        successful_extractions.append(page_result)
                        all_extractions.append(page_result)  # NEW: Add to all extractions
                        
                        # NEW: Track teachers
                        teacher = extracted_data.teacher_name
                        if teacher:
                            teachers_found.append(teacher)
                            
                            # Track grade-teacher combinations
                            combo = {"grade": grade, "teacher": teacher, "pages": [page_num]}
                            existing_combo = None
                            for existing in grade_teacher_combinations:
                                if existing["grade"] == grade and existing["teacher"] == teacher:
                                    existing_combo = existing
                                    break
                            
                            if existing_combo:
                                existing_combo["pages"].append(page_num)
                            else:
                                grade_teacher_combinations.append(combo)
                        
                        # Add students to master list
                        student_count = len(extracted_data.students)
                        for student in extracted_data.students:
                            student_record = {
                                "name": student.name,
                                "grade": grade,  # Use our mapped grade
                                "teacher_name": extracted_data.teacher_name,
                                "source_page": page_num
                            }
                            all_students.append(student_record)
                        
                        logging.info(f"✅ {page_name}: Grade {grade}, {student_count} students")
                        
                    else:
                        # No students found
                        reason = "No students found"
                        page_result = {
                            "page_name": page_name,
                            "page_number": page_num,
                            "extraction": None,
                            "success": False,
                            "failure_reason": reason
                        }
                        all_extractions.append(page_result)  # NEW: Add failed attempt
                        
                        logging.warning(f"⚠️ {page_name}: {reason}")
                        failed_pages.append({"page": page_num, "reason": reason, "grade": grade})
                else:
                    # No results returned
                    reason = "No results returned"
                    page_result = {
                        "page_name": page_name,
                        "page_number": page_num,
                        "extraction": None,
                        "success": False,
                        "failure_reason": reason
                    }
                    all_extractions.append(page_result)  # NEW: Add failed attempt
                    
                    logging.warning(f"⚠️ {page_name}: {reason}")
                    failed_pages.append({"page": page_num, "reason": reason, "grade": grade})
                    
            except Exception as e:
                reason = str(e)
                page_result = {
                    "page_name": page_name,
                    "page_number": page_num,
                    "extraction": None,
                    "success": False,
                    "failure_reason": reason
                }
                all_extractions.append(page_result)  # NEW: Add failed attempt
                
                logging.error(f"❌ {page_name}: Error during processing: {e}")
                failed_pages.append({"page": page_num, "reason": reason, "grade": grade})
            
            finally:
                # Clean up temporary file
                try:
                    os.remove(temp_page_path)
                except:
                    pass
        
        # Calculate statistics by grade
        grade_counts = {}
        for student in all_students:
            grade = student["grade"]
            if grade not in grade_counts:
                grade_counts[grade] = 0
            grade_counts[grade] += 1
        
        # Create final output with NEW extraction_comparison
        final_output = {
            "7to8grade_students": all_students,
            "total_students": len(all_students),
            "successful_pages": len(successful_extractions),
            "failed_pages": len(failed_pages),
            "total_pages_processed": 12,  # Pages 50-61
            "grades_found": sorted(list(grade_counts.keys())),
            "teachers_found": list(set(teachers_found)),  # NEW: Unique teachers
            "grade_teacher_combinations": grade_teacher_combinations,  # Already had this
            "students_by_grade": grade_counts,
            "pages_by_grade": pages_by_grade,
            "extraction_comparison": {  # NEW: Added extraction comparison
                "grade_8": {
                    "expected": EXPECTED_COUNTS["8"],
                    "found": grade_counts.get("8", 0),
                    "difference": grade_counts.get("8", 0) - EXPECTED_COUNTS["8"],
                    "pages": pages_by_grade["8"]
                },
                "grade_7": {
                    "expected": EXPECTED_COUNTS["7"],
                    "found": grade_counts.get("7", 0),
                    "difference": grade_counts.get("7", 0) - EXPECTED_COUNTS["7"],
                    "pages": pages_by_grade["7"]
                }
            },
            "failed_page_details": failed_pages,
            "raw_page_data": all_extractions  # Already had this
        }
        
        # Save results
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_output, f, indent=4)
        
        logging.info(f"Results saved to {output_file}")
        
        # Print comprehensive summary
        print("\n" + "="*60)
        print("EXTRACTION SUMMARY - Grades 7-8")
        print("="*60)
        print(f"Source PDF: {pdf_path}")
        print(f"Pages processed: 50-61 (12 pages total)")
        print(f"Total students extracted: {len(all_students)}")
        print(f"Successful pages: {len(successful_extractions)}")
        print(f"Failed pages: {len(failed_pages)}")
        print(f"Teachers found: {len(set(teachers_found))}")
        
        # NEW: Print extraction comparison
        print("\n" + "-"*60)
        print("EXTRACTION COMPARISON TO EXPECTED COUNTS:")
        print("-"*60)
        
        for grade_name, grade_info in final_output["extraction_comparison"].items():
            grade_label = grade_name.replace("_", " ").title()
            found = grade_info["found"]
            expected = grade_info["expected"]
            diff = grade_info["difference"]
            pages = grade_info["pages"]
            
            status = "✅" if diff >= 0 else "⚠️"
            print(f"{status} {grade_label}:")
            print(f"   Expected: {expected} students")
            print(f"   Found: {found} students")
            print(f"   Difference: {'+' if diff >= 0 else ''}{diff}")
            if pages:
                print(f"   Pages: {pages[0]}-{pages[-1]} ({len(pages)} pages)")
        
        # Print grade-teacher combinations if found
        if grade_teacher_combinations:
            print("\n" + "-"*60)
            print("GRADE-TEACHER COMBINATIONS:")
            print("-"*60)
            for combo in grade_teacher_combinations:
                pages_str = ", ".join(map(str, combo["pages"]))
                student_count = len([s for s in all_students if s["grade"] == combo["grade"] and s["teacher_name"] == combo["teacher"]])
                print(f"  Grade {combo['grade']}: {combo['teacher']} (Pages: {pages_str}) - {student_count} students")
        
        print("\n" + "-"*60)
        
        if failed_pages:
            print(f"\nFailed Pages:")
            for failed in failed_pages:
                print(f"  Page {failed['page']} (Grade {failed['grade']}): {failed['reason']}")
        
        if len(all_students) > 0:
            print(f"\nFirst 5 students extracted:")
            for i, student in enumerate(all_students[:5]):
                print(f"  {i+1}. {student['name']} - Grade {student['grade']} (Page {student['source_page']})")
            
            if len(all_students) > 5:
                print(f"  ... and {len(all_students) - 5} more students")
        
        return final_output
        
    except Exception as e:
        logging.error(f"Critical error during extraction: {e}")
        return None

if __name__ == "__main__":
    logging.info("=== CLS 1975 Grades 7-8 Extraction ===")
    results = extract_single_page_data()
    
    if results and results["total_students"] > 0:
        logging.info(f"Extraction completed! Check the summary above for details.")
        if len(results['grades_found']) == 2:
            logging.info("SUCCESS: Both 7th & 8th grades found!")
        else:
            logging.warning(f"Only found {len(results['grades_found'])} grades: {results['grades_found']}")
    else:
        logging.error("Extraction failed or found no students. Check the logs above for details.")