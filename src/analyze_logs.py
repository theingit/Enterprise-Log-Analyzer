"""
Enterprise Log Analyzer v0.6

Purpose:
- Read application log files.
- Count INFO, WARNING and ERROR entries.
- Generate a summary of log levels.
- Determine overall system health.

-Search log files for keywords.
-Filter only ERROR messages.
-Count different types of errors.
-Generate a health report.
-Organize code into reusable functions.

Author: LN
"""
import re
from pathlib import Path
LOG_LEVELS = ("INFO", "WARNING", "ERROR")
LOG_PATTERN = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+' # Matches Date Time,ms
    r'\[(?P<thread>[^\]]+)\]\s+'        
    r'(?P<level>INFO|WARNING|ERROR)\s+' # Matches level + spaces. \s+: Dynamically consumes the single space after WARNING or the double spaces after INFO.
    r'(?:(?P<component>[\w\.]+)\s+-\s+)?' # Optional component + ' - '. (?:(?P<component>[\w\.]+)\s+-\s+)?: The (?: ... )? syntax makes the entire component string section optional.
    r'(?P<message>.*)$' # Matches the rest        
    )


#def read_log_file(log_file_path: Path) -> list[str] | None:
def read_log_file(log_file_path: Path):

    """Opens a file and returns its lines as a list."""    
    try:
        
        with open(log_file_path, "r", encoding="utf-8") as file:
            return file.readlines()            

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
        return None

def count_log_levels(log_lines):
     
     # Initialize a dictionary to store the counts
        """log_counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0 }"""            
        log_counts = {level: 0 for level in LOG_LEVELS}
        # Check each log level and update the dictionary count                             
        for line in log_lines:
            for level in LOG_LEVELS:
                if level in line:
                    log_counts[level] += 1
                    break                                
            
            #if 'INFO' in line:                    
            #    log_counts['INFO'] += 1
            #elif 'WARNING' in line:
            #    log_counts['WARNING'] += 1
            #elif 'ERROR' in line:
            #    log_counts['ERROR'] += 1

        return log_counts

 #Return only ERROR log entries.

def get_error_messages(log_lines):    
    error_lines = []
    if log_lines is not None:
        for line in log_lines:
            if "ERROR" in line:
                error_lines.append(line)                    

    return error_lines

def print_system_health(lines, log_counts):        
    # Report System Heath Status
    if log_counts['ERROR'] > 0: 
        total_logs = len(lines)
        if log_counts['ERROR'] < 5:  
            #print(f"System Health :⚠️  Warning") 
            print("System Health") 
            print(f"⚠️  Warning") 
            print(f"{log_counts['ERROR']} ERROR entries detected.") 
        elif log_counts['ERROR'] >= 5: 
            print(f"System Health : Critical \nImmediate investigation recommended.")  
            print(f"{log_counts['ERROR']} ERROR entries detected ({(log_counts['ERROR']/total_logs)*100}%) of the logs.")                              
        
    else:
        print("✅ System Healthy")
        print("No ERROR entries detected.")

def print_summary(total_logs, log_counts):
    # 1. Report the log counts
    print("Log Analysis Report")
    print()
    print("-" * 34)                
    print(f"{'Total Logs':<12}: {total_logs}")
         
    # 2. Count log levels             
    for level, count in log_counts.items():
        print(f"{level:<12}: {count}")         
    
    print("-" * 34)

def parse_log_entry(line):
  

    match = LOG_PATTERN.match(line.strip())

    if match:
        data = match.groupdict()
        # If there is no component listed, default its value to None
        #if not data['component']:
            #data['component'] = None
        data["component"] = data["component"] or "N/A"
        return data

    return None


def print_error_details(error_lines):
    print("\nError Details")
    for number, error_line in enumerate(error_lines, start=1):
        parsed_log = parse_log_entry(error_line)
        #print(parsed_log)
        print(f"\n[{number:03}]")
        print(f"Timestamp : {parsed_log['timestamp']}")
        print(f"Thread    : {parsed_log['thread']}")
        print(f"Level     : {parsed_log['level']}")
        print(f"Component : {parsed_log['component']}")
        print(f"Message   : {parsed_log['message']}")

def search_logs(log_lines, keyword):    
    filtered_logs = []
    keyword = keyword.strip().lower()
    for line in log_lines:
        if keyword in line.lower():            
            filtered_logs.append(line)
    return filtered_logs
                

def filter_by_level(log_lines, level):
    log_by_level = []
    if log_lines is not None:
        for line in log_lines:
            if level.upper() in line:
                log_by_level.append(line)                    
    
    return log_by_level

def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then down into sample_log/
    log_file_path  = current_dir.parent / "sample_logs" / "application.log"           
    print(f"Looking for log at: {log_file_path} ..........")
    
    # 1. Read the file
    lines = read_log_file(log_file_path)
        
    if lines is None:
        return
    
    # 2. If file was found, print hearder and process the data
    print("=" * 34)
    print(" Enterprise Log Analyzer v0.6")
    print("=" * 34)
    print()
      
    # 3. Report the log summary
    total_logs = len(lines)   
    log_counts = count_log_levels(lines)   
    print_summary(total_logs, log_counts) 

    # 4. Report Error Details    
    if log_counts['ERROR'] > 0: 
        error_lines = get_error_messages(lines)
        print_error_details(error_lines)
         

    # 5. Report the System Healtch
    print()
    print_system_health(lines, log_counts) 

    # 6. Get log by level    
    log_by_level = filter_by_level(lines, 'WARNING')
    if log_by_level: #if len(log_by_level) > 0:
        print(f"\n Warning logs")
        for number, log in enumerate(log_by_level, start=1):
            print(f"[{number}] {log}")
    else:
        print(f"\n No Warning Logs")
   

    # 7. Search log by keyword
    keyword = input("Enter keyword:")
    #keyword = input("Enter keyword (or 'quit' to exit)") to implement
    filtered_logs = search_logs(lines, keyword)
    print(f"Log result filtered by {keyword}")
    print(f"Found {len(filtered_logs)} matching entries.")
    if filtered_logs: #if len(filtered_logs) > 0:
        for line_num, line in enumerate(filtered_logs, 1):
            print(f"\nLine {line_num}: {line.strip()}")
                       
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()