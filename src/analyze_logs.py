"""
Enterprise Log Analyzer v0.3

Purpose:
- Read application log files.
- Count INFO, WARNING and ERROR entries.
- Generate a summary of log levels.
- Determine overall system health.

-Search log files for keywords.
-Filter only ERROR messages.
-Count different types of errors.
-Generate a basic health report.
-Organize code into reusable functions.

Author: TTH
"""
from pathlib import Path

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
        LOG_LEVELS = ("INFO", "WARNING", "ERROR")
        log_counts = {level: 0 for level in LOG_LEVELS}
                                      
        for line in log_lines:                    
            # Check each log level and update the dictionary count
            if 'INFO' in line:                    
                log_counts['INFO'] += 1
            elif 'WARNING' in line:
                log_counts['WARNING'] += 1
            elif 'ERROR' in line:
                log_counts['ERROR'] += 1

        return log_counts

 #Return only ERROR log entries.
def get_error_messages(log_lines):    
    error_lines = []
    if log_lines is not None:
        for line in log_lines:
            if "ERROR" in line:
                error_lines.append(line)
                    

    return error_lines

def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then down into sample_log/
    log_file_path  = current_dir.parent / "sample_logs" / "application.log"           
    print(f"Looking for log at: {log_file_path} ..........")
    
    # 1. Read the file
    lines = read_log_file(log_file_path)
    
    # 2. If file was found, process the data
    if lines is not None:
        print("=" * 34)
        print(" Enterprise Log Analyzer v0.3")
        print("=" * 34)
        print()
      
        # Report the log counts
        print("Enterprise Log Summary")
        print("-" * 34)
        total_logs = len(lines)        
        print(f"{'Total Log Entries':<18}: {total_logs}")


        # 2. Count log levels
        log_counts = count_log_levels(lines)
        for level, count in log_counts.items():
            print(f"{level:<18}: {count}")            

        print("-" * 34)
        print()
            
        # 3. Report only ERROR lines
        if log_counts['ERROR'] > 0: 
            print("ERROR Messages")
            error_lines = get_error_messages(lines)
            for line_number, error_line in enumerate(error_lines, start=1):
                print(f"[{line_number:03}] {error_line.strip()}") 
            print()   
            if log_counts['ERROR'] < 5:  
                print(f"System Health :⚠️  Warning") 
                print(f"{log_counts['ERROR']} ERROR entries detected.") 
            elif log_counts['ERROR'] >= 5: 
                        print(f"System Health : Critical \n Immediate investigation recommended.")  
                        print(f"{log_counts['ERROR']} ERROR entries detected ({(log_counts['ERROR']/total_logs)*100}%) of the logs.")                              
            
        else:
            print("✅ System Healthy")
            print("No ERROR entries detected.")
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()