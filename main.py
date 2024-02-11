from auto_zipper import zip_folder
from auto_deleter import delete_file
from version_updater import increment_version, read_version
from auto_copier import copy_files
from auto_renamer import rename_file
from new_features import new_features_add
import time



folder_to_zip = 'F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer'
output_zip_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer.zip'
version_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Version.txt'
updates_file = "F:/UNITY PROJECTS/FINAL BUILDS/Updates.txt"
destination_folder = 'F:/OneDrive/Game'
destination_folder2 = 'G:/My Drive/Game'
print(f"Current version number: {read_version(version_file)}")
#print("Deleting old build and adding new build")
old_file_name = "F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer.zip"
new_file_name = f"F:/UNITY PROJECTS/FINAL BUILDS/Rocket Flyer v{read_version(version_file)}.zip"
rename_file(old_file_name, new_file_name)
#delete_file(output_zip_file)
time.sleep(3)
print("Zipping the new build")
zip_folder(folder_to_zip, output_zip_file)
increment_version(version_file)
print(f"New Version Number: {read_version(version_file)}")
new_features_add()
time.sleep(1)
copy_files(output_zip_file, destination_folder)
copy_files(version_file, destination_folder)
copy_files(updates_file, destination_folder)
copy_files(output_zip_file, destination_folder2)
copy_files(version_file, destination_folder2)
copy_files(updates_file, destination_folder2)
input("Latest Build uploaded successfuly")