from excel_util import calculate_file_total, get_excel_files
import pytest
def test_calculate_file_total_file_not_find():
    with pytest.raises(FileNotFoundError):
        calculate_file_total("missing.xlsx")
def test_get_excel_files_empty_folder(tmp_path):
    folder= tmp_path / "sales"
    folder.mkdir()
    (folder/"a.xlsx").touch()
    (folder/ "note.txt").touch()
    result=get_excel_files(folder)
    assert len(result)==1
    assert result[0].endswith("a.xlsx")
def test_get_excel_files_folder_not_exist():
    missing_folder="not_exist_folder"
    result= get_excel_files(missing_folder)
    assert result == []