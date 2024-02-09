import shutil

def copy_files(source_file, destination_folder):
    """
    Copy files from source to destination folder.

    :param source_file: Path to the source file.
    :param destination_folder: Path to the destination folder.
    """
    try:
        shutil.copy(source_file, destination_folder)
        print(f"File '{source_file}' copied to '{destination_folder}'")
    except Exception as e:
        print(f"Error copying file: {e}")


output_zip_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer.zip'
version_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Version.txt'
destination_folder = 'F:/UNITY PROJECTS/Test Folder'


