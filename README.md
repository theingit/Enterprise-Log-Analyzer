```text
## Enterprise Log Analyzer (Python)
A Python-based log analysis tool designed for enterprise application support.

## Overview
Enterprise Log Analyzer is a Python command-line application that analyzes application log files. It provides:

- Log level statistics
- Error extraction
- Keyword searching
- Log filtering
- System health reporting

This project simulates real-world monitoring tasks performed by Application Support Engineers and Production Support Engineers.


## Features
- Read log files
- Count log entries
- Analyze log levels
- Filter logs by level
- Search logs by keyword
- Generate system health reports

## Project Structure
Enterprise-Log-Analyzer/
> docs/
> output/
> sample_logs/
    > application.log
> src/
    > analyze_logs.py
    > read_logs.py
    > report_generator.py
> README.md
> gitignore

## Installation
Clone the repository

```bash
git clone https://github.com/<username>/Enterprise-Log-Analyzer.git
```

Move into the project

```bash
cd Enterprise-Log-Analyzer
```

Run

```bash
python src/analyze_logs.py
```


## Sample Output
==================================
 Enterprise Log Analyzer v1.0
==================================

Log Analysis Report

----------------------------------
Total Logs  : 10
INFO        : 6
WARNING     : 2
ERROR       : 2
----------------------------------

System Health
⚠️ Warning
2 ERROR entries detected.

# The analyzer also displays structured error details, supports log-level filtering, and keyword searching.


## Technologies Used
- Python 3
- Visual Studio Code
- Git
- GitHub
- Regular Expressions (re module)
- pathlib

## Future Improvements
- Export reports to CSV
- Export reports to JSON
- Support multiple log file formats
- Add command-line arguments
- Generate HTML reports
- Visualize log statistics with charts


## Author
LN

Enterprise IT Bootcamp Portfolio Project

GitHub:
https://github.com/theingit
```

