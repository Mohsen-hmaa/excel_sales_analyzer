from excel_util import create_report, calculate_file_total,get_excel_files
from error_util import save_error
import os
excel_files=get_excel_files("data")
if not excel_files:
    print("There is no excel file in the path")
else:
    report={}
    for file in excel_files:
        try:
            file_total=calculate_file_total(file)
            file_name=os.path.basename(file)
            report[file_name]=file_total
        except Exception as e:
            save_error(file,e,"output/errors.txt")
    create_report(report,"output/final_report.xlsx")