from version_updater import increment_version, read_version
version_file = 'F:/UNITY PROJECTS/FINAL BUILDS/Version.txt'

def new_features_add():
    new_features = input("Type down the new features: ")
    # Save the new features to a readme.txt file
    with open("F:/UNITY PROJECTS/FINAL BUILDS/Updates.txt", "a") as f:
        f.write(f"Version Updates:{read_version(version_file)}\n{new_features}\n")
