from error_util import save_error


def test_save_error(tmp_path):
    error_file = tmp_path / "errors" / "errors.txt"

    save_error(
        "test.xlsx",
        "File is corrupted",
        error_file
    )

    assert error_file.exists()

    content = error_file.read_text()

    assert "test.xlsx" in content
    assert "File is corrupted" in content