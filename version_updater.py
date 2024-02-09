def read_version(filename):
    """
    Read the version number from a text file.

    :param filename: Name of the text file.
    :return: Current version number.
    """
    try:
        with open(filename, 'r') as file:
            version_number = int(file.read().strip())
            return version_number
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new file with version number 1.")
        with open(filename, 'w') as file:
            file.write('1')
        return 1
    except Exception as e:
        print(f"Error reading version number: {e}")

def increment_version(filename):
    """
    Increment the version number in a text file by one.

    :param filename: Name of the text file.
    """
    try:
        with open(filename, 'r+') as file:
            version_number = int(file.read().strip())
            updated_version = version_number + 1
            file.seek(0)
            file.write(str(updated_version))
            file.truncate()
            print(f"Version number incremented to: {updated_version}")
    except Exception as e:
        print(f"Error incrementing version number: {e}")

