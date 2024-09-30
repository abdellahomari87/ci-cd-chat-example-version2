from project_ufs.project_ufs_service import get_project_message

def test_get_project_message():
    assert get_project_message() == "Hello from the Project_UFS service!"
