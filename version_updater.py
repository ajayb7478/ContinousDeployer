def read_version(filename):
    """
    Read the version number from a text file.

    :param filename: Name of the text file.
    :return: Current version number.
    """
    try:
        with open(filename, 'r') as file:
            version_number = file.read().strip()
            if version_number == "":
                version_number = "0.0.0"
            return version_number
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new file with version number 0.0.0.")
        with open(filename, 'w') as file:
            file.write('0.0.0')
        return '0.0.0'
    except Exception as e:
        print(f"Error reading version number: {e}")

def increment_version(filename):
    """
    Increment the version number in a text file by one.

    :param filename: Name of the text file.
    """
    try:
        current_version = read_version(filename)
        version_segments = current_version.split(".")
        version_segments = [int(segment) for segment in version_segments]
        # Increment the last segment by one
        version_segments[-1] += 1
        # Ensure each segment has at most 100 digits
        for i in range(len(version_segments) - 1, 0, -1):
            if version_segments[i] >= 100:
                version_segments[i] = 0
                version_segments[i - 1] += 1
        # Convert the segments to strings and join them with "."
        updated_version_str = ".".join([str(segment) for segment in version_segments])
        with open(filename, 'w') as file:
            file.write(updated_version_str)
        # Print the version number in the desired format
        print(f"Version number incremented to: {updated_version_str}")
    except Exception as e:
        print(f"Error incrementing version number: {e}")

# Example usage:
