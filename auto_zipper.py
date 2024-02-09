import zipfile
import os
import sys

def get_folder_size(folder_path):
    """
    Calculate the total size of all files in a folder and its subfolders.

    :param folder_path: Path to the folder.
    :return: Total size of all files in bytes.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def zip_folder(folder_path, output_path):
    """
    Zip a folder and its contents.

    :param folder_path: Path to the folder to be zipped.
    :param output_path: Path to the output zip file.
    """
    try:
        # Create a ZipFile object
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add the entire folder and its contents to the zip file
            for root, _, files in os.walk(folder_path):
                for file in files:
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, os.path.dirname(folder_path))
                    zipf.write(abs_path, rel_path)
                    # Calculate progress and update the progress bar
                    num_files = sum(len(files) for _, _, files in os.walk(folder_path))
                    progress = min((len(zipf.namelist()) / num_files) * 100, 100)
                    num_equals = int(progress / 2)
                    progress_bar = '[' + '=' * num_equals + ' ' * (50 - num_equals) + ']'
                    sys.stdout.write(f"\rProgress: {progress_bar} {progress:.2f}%")
                    sys.stdout.flush()
        print(f"\nFolder '{folder_path}' successfully zipped to '{output_path}'")
    except Exception as e:
        print(f"Error zipping folder: {e}")

# Example usage:

