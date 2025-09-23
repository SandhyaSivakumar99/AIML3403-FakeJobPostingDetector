from pathlib import Path


def test_data_folder_exists():
    assert Path("data").exists()

def test_package_imports():
    import fakedetector  # noqa: F401
