def read_version(filename):
    """
    Read the version number from a text file and increment it by one.

    :param filename: Name of the text file.
    :return: Current version number.
    """
    try:
        with open(filename, 'r+') as file:
            version_number = int(file.read().strip())
            updated_version = version_number + 1
            file.seek(0)
            file.write(str(updated_version))
            file.truncate()
            return updated_version
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new file with version number 1.")
        with open(filename, 'w') as file:
            file.write('1')
        return 1
    except Exception as e:
        print(f"Error reading or updating version number: {e}")


version_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Version.txt'
current_version = read_version(version_file)
