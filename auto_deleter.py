import os

def delete_file(file_path):
    """
    Delete a file.

    :param file_path: Path to the file to be deleted.
    """
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")
