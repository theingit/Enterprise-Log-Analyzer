"""
Enterprise Log Analyzer v0.2

Purpose:
- Read application log files.
- Count INFO, WARNING and ERROR entries.
- Generate a summary of log levels.
- Determine overall system health.

Author: TTH
"""
from pathlib import Path
#def read_log_file(log_file_path):
#def read_log_file(log_file_path: Path) -> list[str] | None:
def read_log_file(log_file_path: Path):
    """Opens a file and returns its lines as a list."""    
    try:

        
        with open(log_file_path, "r", encoding="utf-8") as file:
            return file.readlines()            

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
        return None

def main():

    # Initialize a dictionary to store the counts
    """log_counts = {
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0
    }"""

    LOG_LEVELS = ("INFO", "WARNING", "ERROR")
    log_counts = {level: 0 for level in LOG_LEVELS}

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
        print(" Enterprise Log Analyzer v0.2")
        print("=" * 34)
        print()
      
        for line in lines:
            # Check each log level and update the dictionary count
            #if 'INFO' in line:
            if line.find("INFO") != -1:
                log_counts['INFO'] += 1
            elif 'WARNING' in line:
                log_counts['WARNING'] += 1
            elif 'ERROR' in line:
                log_counts['ERROR'] += 1

        # Report the counts
        print("Log Analysis Report")
        print("-" * 34)
        total_logs = len(lines)        
        print(f"{'Total Log Entries':<18}: {total_logs}")

        for level, count in log_counts.items():
            print(f"{level:<18}: {count}")

        print("-" * 34)
        print()
            

        if log_counts['ERROR'] > 0: 
            print(f"⚠️  Warning")
            print(f"{log_counts['ERROR']} ERROR entries detected.")
        else:
            print("✅ Healthy")
            print("No ERROR entries detected.")
      


# Standard entry point to run the program
if __name__ == "__main__":
    main()