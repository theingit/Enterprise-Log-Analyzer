print("----------Day4 Practice [Read file, print lines, count lines, handle FileNotFoundError]---------")

from pathlib import Path

#def read_log_file(log_file_path):
def read_log_file(log_file_path: Path):
    """Opens a file and returns its lines as a list."""
    try:
         # Open the file in read-only mode
        #with open(log_file_path,'r') as file:            
        with open(log_file_path, "r", encoding="utf-8") as file:
            return file.readlines()            

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' does not exist.")
        return None

def count_lines(lines_list):
      """Counts the total number of lines in the list."""
      return len(lines_list)

def main():

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent    
    # Go up one level to the project root, then down into sample_log/
    log_file_path  = current_dir.parent / "sample_logs" / "application.log"

     # Convert to string to pass into your existing functions
    #log_path_str = str(log_file_path)        
    print(f"Looking for log at: {log_file_path}")
    
    # 1. Read the file
    lines = read_log_file(log_file_path)
    
    # 2. If file was found, process the data
    if lines is not None:
        print("=" * 34)
        print(" Enterprise Log Analyzer v0.1")
        print("=" * 34)
        print()
      
        #for line in lines:
            #print(line, end="")  # end="" prevents extra blank lines

        #Mini challenge: print line numbers using enumerate()
        for line_number, line in enumerate(lines, start=1):
            print(f"[{line_number:03}] {line.strip()}") #print(f"Line {line_number}: {line}", end="")        
            
        # 3. Count and print the total
        total_lines = count_lines(lines)
        print(f"\n\nTotal lines in file: {total_lines}")

        if lines:
            #print(f"\n\nThe last line in file: {lines[-1].strip()}") #print the last line        
            print("\nLast Log Entry")
            print("-" * 40)
            print(lines[-1].strip())


# Standard entry point to run the program
if __name__ == "__main__":
    main()

 

