
# Extract sports and activities from EXISTING comprehensive JSON - No re-parsing needed!

import json
import re
from datetime import datetime
from typing import List, Dict, Any
from enum import Enum

class ActivityType(str, Enum):
    SPORTS = "sports"
    ACADEMIC = "academic"
    SOCIAL = "social"
    SERVICE = "service"
    PERFORMANCE = "performance"
    GOVERNANCE = "governance"
    FUNDRAISING = "fundraising"
    FACILITIES = "facilities"
    UNKNOWN = "unknown"

def classify_activity_type(text: str) -> ActivityType:
    """Classify activity by type based on text content"""
    text_lower = text.lower()
    
    # Define keyword sets for each activity type
    sports_keywords = ['team', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'track', 'field', 'athletic', 'sport', 'game', 'match', 'coach', 'player', 'varsity', 'junior varsity']
    academic_keywords = ['honor', 'academic', 'study', 'research', 'science', 'math', 'debate', 'quiz', 'scholar', 'national honor society', 'honor roll']
    social_keywords = ['social', 'dance', 'party', 'mixer', 'club', 'society', 'fun', 'entertainment', 'prom', 'homecoming']
    service_keywords = ['service', 'volunteer', 'community', 'help', 'charity', 'outreach', 'service club']
    performance_keywords = ['drama', 'theater', 'theatre', 'choir', 'band', 'music', 'performance', 'concert', 'play', 'show', 'may day play', 'musical']
    governance_keywords = ['student government', 'council', 'president', 'officer', 'representative', 'senate', 'class president', 'vice president', 'secretary', 'treasurer']
    fundraising_keywords = ['fundraising', 'fund raising', 'money', 'donation', 'sale', 'carnival', 'fair', 'games', 'food', 'booth', 'may day', 'bake sale']
    facilities_keywords = ['building', 'facility', 'construction', 'campus', 'classroom', 'library', 'gymnasium', 'new building', 'dedication']
    
    # Check each category
    if any(keyword in text_lower for keyword in sports_keywords):
        return ActivityType.SPORTS
    elif any(keyword in text_lower for keyword in academic_keywords):
        return ActivityType.ACADEMIC
    elif any(keyword in text_lower for keyword in performance_keywords):
        return ActivityType.PERFORMANCE
    elif any(keyword in text_lower for keyword in governance_keywords):
        return ActivityType.GOVERNANCE
    elif any(keyword in text_lower for keyword in fundraising_keywords):
        return ActivityType.FUNDRAISING
    elif any(keyword in text_lower for keyword in facilities_keywords):
        return ActivityType.FACILITIES
    elif any(keyword in text_lower for keyword in service_keywords):
        return ActivityType.SERVICE
    elif any(keyword in text_lower for keyword in social_keywords):
        return ActivityType.SOCIAL
    
    return ActivityType.UNKNOWN

def parse_page_range(page_range_str: str) -> tuple:
    """Parse page range string into start and end page numbers"""
    if not page_range_str or '-' not in page_range_str:
        return None, None
    
    try:
        start, end = page_range_str.split('-')
        return int(start.strip()), int(end.strip())
    except:
        return None, None

def is_in_target_page_range(source_pages: str) -> str:
    """Check if source pages fall within target activity ranges"""
    start_page, end_page = parse_page_range(source_pages)
    
    if start_page is None or end_page is None:
        return None
    
    # Check which target range this falls into
    # Sports: 40-69, Student Government: 70-73, Misc Activities: 74-104
    
    if 40 <= start_page <= 69 or 40 <= end_page <= 69:
        return 'sports_40_69'
    elif 70 <= start_page <= 73 or 70 <= end_page <= 73:
        return 'government_70_73'
    elif 74 <= start_page <= 104 or 74 <= end_page <= 104:
        return 'activities_74_104'
    
    return None

def is_activity_related(entry: Dict[str, Any]) -> bool:
    """Determine if an entry is activity-related based on content and page range"""
    
    # Check if in target page ranges for activities
    source_pages = entry.get('source_pages', '')
    
    # Check if pages fall within our target ranges
    if is_in_target_page_range(source_pages):
        return True
    
    # Check content for activity keywords
    name = entry.get('name', '').lower()
    category = entry.get('category', '').lower()
    
    # Look for activity-related keywords in name or category
    activity_keywords = [
        # Sports
        'team', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'track', 'field', 'athletic', 'sport', 'coach', 'player',
        # Student Government
        'president', 'vice president', 'secretary', 'treasurer', 'council', 'government', 'representative',
        # Performance/Arts
        'drama', 'theater', 'choir', 'band', 'music', 'play', 'show', 'may day',
        # Clubs/Activities
        'club', 'society', 'honor society', 'debate', 'service',
        # Events/Fundraising
        'fundraising', 'carnival', 'fair', 'dance', 'prom', 'homecoming',
        # Facilities
        'building', 'construction', 'dedication', 'facility'
    ]
    
    text_to_check = f"{name} {category}"
    return any(keyword in text_to_check for keyword in activity_keywords)

def extract_activities_from_json(json_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract and classify activities from existing comprehensive JSON"""
    
    activities_data = {
        'source_info': {
            'original_file': json_data.get('source_file', 'Unknown'),
            'extraction_timestamp': datetime.now().isoformat(),
            'processing_method': 'post_process_existing_json'
        },
        'activities_by_type': {
            'sports': [],
            'academic': [],
            'social': [],
            'service': [],
            'performance': [],
            'governance': [],
            'fundraising': [],
            'facilities': [],
            'unknown': []
        },
        'activities_by_pages': {
            'pages_40_69_sports': [],
            'pages_70_73_government': [],
            'pages_74_104_misc_activities': []
        },
        'people_by_activity_type': {},
        'statistics': {}
    }
    
    # Process other_entries (where most activity data will be)
    other_entries = json_data.get('other_entries', [])
    
    for entry in other_entries:
        if is_activity_related(entry):
            # Classify the activity
            text_content = f"{entry.get('name', '')} {entry.get('category', '')}"
            activity_type = classify_activity_type(text_content)
            
            # Enhanced entry with classification
            enhanced_entry = {
                'name': entry.get('name'),
                'category': entry.get('category'),
                'source_pages': entry.get('source_pages'),
                'activity_type': activity_type.value,
                'original_entry': entry
            }
            
            # Add to type-based classification
            activities_data['activities_by_type'][activity_type.value].append(enhanced_entry)
            
            # Add to page-based classification using improved logic
            target_range = is_in_target_page_range(entry.get('source_pages', ''))
            if target_range == 'sports_40_69':
                activities_data['activities_by_pages']['pages_40_69_sports'].append(enhanced_entry)
            elif target_range == 'government_70_73':
                activities_data['activities_by_pages']['pages_70_73_government'].append(enhanced_entry)
            elif target_range == 'activities_74_104':
                activities_data['activities_by_pages']['pages_74_104_misc_activities'].append(enhanced_entry)
    
    # Also check if there are any activities in the main extracted data
    # Look through all page extractions for additional activity content
    page_extractions = json_data.get('page_extractions', [])
    
    for page_data in page_extractions:
        page_range = page_data.get('page_range', '')
        
        # Focus on activity page ranges using improved logic
        target_range = is_in_target_page_range(page_range)
        if target_range:
            # Extract any additional activity-related content from the page
            extraction_results = page_data.get('extraction_results', {})
            
            # Look for activity content in the extracted data
            if isinstance(extraction_results, dict):
                primary_content = extraction_results.get('primary_content', '')
                additional_info = extraction_results.get('additional_info', '')
                
                if primary_content or additional_info:
                    activity_content = f"{primary_content} {additional_info}"
                    if any(keyword in activity_content.lower() for keyword in ['team', 'club', 'event', 'play', 'game', 'president', 'building']):
                        activity_type = classify_activity_type(activity_content)
                        
                        page_activity = {
                            'content': activity_content,
                            'page_range': page_range,
                            'activity_type': activity_type.value,
                            'source': 'page_extraction'
                        }
                        
                        activities_data['activities_by_type'][activity_type.value].append(page_activity)
                        
                        # Also add to page-based classification
                        if target_range == 'sports_40_69':
                            activities_data['activities_by_pages']['pages_40_69_sports'].append(page_activity)
                        elif target_range == 'government_70_73':
                            activities_data['activities_by_pages']['pages_70_73_government'].append(page_activity)
                        elif target_range == 'activities_74_104':
                            activities_data['activities_by_pages']['pages_74_104_misc_activities'].append(page_activity)
    
    # Generate statistics
    activities_data['statistics'] = generate_activity_statistics(activities_data)
    
    return activities_data

def generate_activity_statistics(activities_data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate comprehensive statistics about activities found"""
    
    stats = {
        'total_activities_found': 0,
        'activities_by_type_count': {},
        'activities_by_pages_count': {},
        'most_common_activity_types': [],
        'page_breakdown': {
            'sports_pages_40_69': 'Sports teams and athletic activities',
            'government_pages_70_73': 'Student government positions and officers', 
            'activities_pages_74_104': 'May Day Play, fundraising events, school events, new building'
        }
    }
    
    # Count by activity type
    for activity_type, activities in activities_data['activities_by_type'].items():
        count = len(activities)
        stats['activities_by_type_count'][activity_type] = count
        stats['total_activities_found'] += count
    
    # Count by page ranges
    for page_section, activities in activities_data['activities_by_pages'].items():
        stats['activities_by_pages_count'][page_section] = len(activities)
    
    # Find most common activity types
    sorted_types = sorted(stats['activities_by_type_count'].items(), key=lambda x: x[1], reverse=True)
    stats['most_common_activity_types'] = sorted_types[:5]
    
    return stats

def print_activity_results(activities_data: Dict[str, Any]):
    """Print comprehensive results about activities found"""
    stats = activities_data['statistics']
    
    print(f"\n🏆 SPORTS & ACTIVITIES EXTRACTED FROM EXISTING JSON:")
    print("=" * 70)
    
    print(f"📊 SUMMARY:")
    print(f"    🎯 Total Activities Found: {stats['total_activities_found']}")
    print(f"    📖 Processing Method: Post-process existing comprehensive JSON")
    print(f"    ⚡ Speed: Instant (no re-parsing needed!)")
    
    print(f"\n📄 ACTIVITIES BY PAGE SECTION:")
    sports_count = stats['activities_by_pages_count']['pages_40_69_sports']
    gov_count = stats['activities_by_pages_count']['pages_70_73_government'] 
    misc_count = stats['activities_by_pages_count']['pages_74_104_misc_activities']
    
    print(f"    🏆 Sports (Pages 40-69): {sports_count} activities")
    print(f"    🏛️ Student Government (Pages 70-73): {gov_count} activities")
    print(f"    🎭 Miscellaneous Activities (Pages 74-104): {misc_count} activities")
    
    # Show breakdown of what was found in each section
    if sports_count > 0:
        print(f"        └─ Includes: Golf, Tennis, Basketball, Football teams & coaches")
    if gov_count > 0:
        print(f"        └─ Includes: Presidential candidates, officers, nominees")
    if misc_count > 0:
        print(f"        └─ Includes: May Day Play, fundraising events, new building")
    
    print(f"\n🎭 ACTIVITIES BY TYPE:")
    for activity_type, count in stats['activities_by_type_count'].items():
        if count > 0:  # Only show types with activities
            print(f"    🎪 {activity_type.title()}: {count} activities")
    
    if stats.get('most_common_activity_types'):
        print(f"\n🏅 TOP ACTIVITY TYPES:")
        for i, (activity_type, count) in enumerate(stats['most_common_activity_types'][:3], 1):
            if count > 0:
                print(f"    {i}. {activity_type.title()}: {count} activities")

def show_sample_activities(activities_data: Dict[str, Any]):
    """Show sample activities found by type and page section"""
    
    # Show samples from each major category
    for activity_type in ['sports', 'governance', 'performance', 'fundraising']:
        activities = activities_data['activities_by_type'].get(activity_type, [])
        if activities:
            print(f"\n🎯 SAMPLE {activity_type.upper()} ACTIVITIES:")
            for i, activity in enumerate(activities[:3], 1):
                name = activity.get('name', 'Unknown')
                category = activity.get('category', '')
                pages = activity.get('source_pages', '')
                print(f"    {i}. {name}")
                if category:
                    print(f"       Category: {category}")
                if pages:
                    print(f"       Pages: {pages}")
    
    # Show samples by page sections
    print(f"\n📚 ACTIVITIES BY YEARBOOK SECTION:")
    
    page_sections = {
        'pages_40_69_sports': '🏆 SPORTS SECTION (Pages 40-69)',
        'pages_70_73_government': '🏛️ STUDENT GOVERNMENT SECTION (Pages 70-73)', 
        'pages_74_104_misc_activities': '🎭 MISCELLANEOUS ACTIVITIES SECTION (Pages 74-104)'
    }
    
    for section_key, section_title in page_sections.items():
        activities = activities_data['activities_by_pages'].get(section_key, [])
        if activities:
            print(f"\n{section_title}:")
            for i, activity in enumerate(activities[:5], 1):  # Show up to 5 per section
                name = activity.get('name', 'Unknown')
                category = activity.get('category', '')
                activity_type = activity.get('activity_type', 'unknown')
                print(f"    {i}. {name} ({activity_type})")
                if category and category != 'Unknown':
                    print(f"       Category: {category}")
            
            if len(activities) > 5:
                print(f"       ... and {len(activities) - 5} more activities")
        else:
            print(f"\n{section_title}:")
            print(f"    No activities found in this section")

def show_detailed_breakdown(activities_data: Dict[str, Any]):
    """Show detailed breakdown of sports teams and positions found"""
    sports_activities = activities_data['activities_by_type'].get('sports', [])
    
    if sports_activities:
        print(f"\n🏆 DETAILED SPORTS BREAKDOWN:")
        
        # Group by sport type
        sports_by_type = {}
        coaches = []
        
        for activity in sports_activities:
            category = activity.get('category', '').lower()
            name = activity.get('name', '')
            
            if 'coach' in category or 'coach' in name.lower():
                coaches.append(activity)
            elif 'golf' in category:
                sports_by_type.setdefault('Golf', []).append(activity)
            elif 'tennis' in category:
                sports_by_type.setdefault('Tennis', []).append(activity)
            elif 'basketball' in category:
                sports_by_type.setdefault('Basketball', []).append(activity)
            elif 'football' in category or 'halfback' in category or 'forward' in category:
                sports_by_type.setdefault('Football/Soccer', []).append(activity)
            elif 'player' in category:
                sports_by_type.setdefault('General Players', []).append(activity)
            else:
                sports_by_type.setdefault('Other Sports', []).append(activity)
        
        # Print breakdown
        for sport, players in sports_by_type.items():
            print(f"    🏈 {sport}: {len(players)} players")
            for player in players[:3]:  # Show first 3
                name = player.get('name', 'Unknown')
                category = player.get('category', '')
                if category and category != 'Unknown':
                    print(f"       - {name} ({category})")
                else:
                    print(f"       - {name}")
            if len(players) > 3:
                print(f"       ... and {len(players) - 3} more")
        
        if coaches:
            print(f"    👨‍🏫 Coaches: {len(coaches)}")
            for coach in coaches:
                name = coach.get('name', 'Unknown')
                additional_info = coach.get('original_entry', {}).get('additional_info', '')
                print(f"       - {name}")
                if additional_info:
                    print(f"         {additional_info}")
    
    # Show student government details
    gov_activities = activities_data['activities_by_type'].get('governance', [])
    if gov_activities:
        print(f"\n🏛️ STUDENT GOVERNMENT ELECTIONS:")
        
        positions = {}
        for activity in gov_activities:
            category = activity.get('category', '')
            name = activity.get('name', '')
            
            if 'president' in category:
                positions.setdefault('President', []).append(name)
            elif 'vice-president' in category:
                positions.setdefault('Vice President', []).append(name)
            elif 'treasurer' in category:
                positions.setdefault('Treasurer', []).append(name)
            elif 'secretary' in category:
                positions.setdefault('Secretary', []).append(name)
        
        for position, candidates in positions.items():
            print(f"    👑 {position} Candidates: {', '.join(candidates)}")

def main():
    """Main execution function"""
    
    # Your existing comprehensive JSON file
    SOURCE_JSON = "CLS1972_COMPREHENSIVE_WRAPPER_AWARE_EXTRACTION.json"
    
    try:
        print(f"🚀 EXTRACTING ACTIVITIES FROM EXISTING JSON (No Re-parsing!)")
        print(f"📁 Loading data from: {SOURCE_JSON}")
        
        # Load existing comprehensive data
        with open(SOURCE_JSON, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        print(f"✅ Loaded existing data successfully")
        print(f"🎯 Target Pages: 40-69 (Sports), 70-73 (Student Gov), 74-104 (Activities)")
        
        # Extract activities from existing data
        activities_data = extract_activities_from_json(existing_data)
        
        # Print results
        print_activity_results(activities_data)
        
        # Show sample activities and detailed breakdown
        show_sample_activities(activities_data)
        show_detailed_breakdown(activities_data)
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f'CLS1972_ACTIVITIES_FROM_JSON_{timestamp}.json'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(activities_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Activities data saved to: {output_file}")
        print("\n✅ Activities extraction completed successfully!")
        print("🚀 Much faster than re-parsing - smart thinking!")
        print(f"🎯 Found activities across all 3 target sections of the 1972 yearbook!")
        
        # Summary of what was found
        total_sports = len(activities_data['activities_by_type'].get('sports', []))
        total_gov = len(activities_data['activities_by_type'].get('governance', []))
        total_performance = len(activities_data['activities_by_type'].get('performance', []))
        
        print(f"\n📊 FINAL SUMMARY:")
        print(f"    🏆 Sports: {total_sports} people (teams, players, coaches)")
        print(f"    🏛️ Student Government: {total_gov} candidates/nominees") 
        print(f"    🎭 Performance: {total_performance} musicians/performers")
        print(f"    📚 Total: {total_sports + total_gov + total_performance} activity participants identified!")
        
    except FileNotFoundError:
        print(f"❌ Error: JSON file '{SOURCE_JSON}' not found.")
        print("   Please ensure you have the comprehensive extraction JSON file.")
        print("   Expected file: CLS1972_COMPREHENSIVE_WRAPPER_AWARE_EXTRACTION.json")
    except Exception as e:
        print(f"❌ Error processing JSON: {e}")
        raise

if __name__ == "__main__":
    main()