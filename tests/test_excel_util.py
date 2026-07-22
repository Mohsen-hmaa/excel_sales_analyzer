from openpyxl import Workbook
from excel_util import calculate_file_total
def test_calculate_file_total(tmp_path):
    file_path = tmp_path / "test_sales.xlsx"
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Product"
    sheet["B1"] = "Quantity"
    sheet["C1"] = "Price"
    sheet["A2"] = "Pen"
    sheet["B2"] = 2
    sheet["C2"] = 100
    sheet["A3"] = "Book"
    sheet["B3"] = 3
    sheet["C3"] = 50

    workbook.save(file_path)

    result = calculate_file_total(file_path)

    assert result == 350