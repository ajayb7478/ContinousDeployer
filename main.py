from auto_zipper import zip_folder
from auto_deleter import delete_file
from version_updater import increment_version, read_version
from auto_copier import copy_files
import time



folder_to_zip = 'F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer'
output_zip_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer.zip'
version_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Version.txt'
destination_folder = 'F:/UNITY PROJECTS/Test Folder'
print(f"Current version number: {read_version(version_file)}")
print("Deleting old build and adding new build")
delete_file(output_zip_file)
time.sleep(3)
print("Zipping the new build")
zip_folder(folder_to_zip, output_zip_file)
increment_version(version_file)
print(f"New Version Number: {read_version(version_file)}")
time.sleep(2)
copy_files(output_zip_file, destination_folder)
copy_files(version_file, destination_folder)