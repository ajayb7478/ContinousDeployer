import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print("File renamed successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:

