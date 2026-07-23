# Excel Sales Analyzer
## Description
 A Python application that reads multiple Excel sales files, calculates total sales for each file, generates a summary Excel report, and logs  processing errors into a separate error log file.
## Features 
- Read multiple Excel files
- Calculate total sales for each file
- Generate a summary Excel report
- Manage and log processing errors
## Project Structure
```
Excel_sales_analyzer/
│
├── main.py
├── excel_util.py
├── error_util.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── Data/        #input Excel files
├── Output/      #Generated reports
└── tests/
    ├── test_excel_util.py
    ├── test_error_util.py
    └── test_error_cases.py
```
## Requirements
- Python 3.x
- openpyxl
## How to Run
1. Create a virtual environment:
```bash
python -m venv venv
```
2. Activate the virtual environment:
```bash
.\venv\Scripts\Activate.ps1
```
3. Install required packages:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
python main.py
```
## Running Tests
To run the test suite:
```bash
python -m pytest
```
The tests cover:
- Excel sales calculation
- Report generation
- Error logging
- Handling missing files
- Empty folder handling
- Excel file filtering
## Future Improvements
- Add support for more Excel formats
- Add a graphical user interface
- Add database storage
## Example Output
The application generates an Excel report containing:

| File | Sales |
|------|-------|
| sales_1.xlsx | 350 |
| sales_2.xlsx | 650 |
| TOTAL | 1000 |
Errors are saved separately in the error log file.