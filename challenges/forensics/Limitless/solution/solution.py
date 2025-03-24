import zipfile
import os
import re

FLAG_REGEX = r"YBN24{(?!kY0Sh1ki_Mur4sAk1_)[^}]*}"

def unzip_file(zip_filepath, extract_to):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def get_flag_from_file(filepath):
    """
    Searches for a valid flag in all files in the given directory.
    """
    for file in os.listdir(filepath):
        file_path = os.path.join(filepath, file)
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                match = re.search(FLAG_REGEX, content)
                if match:
                    return match.group()  # Return the matched flag
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    return None  # Return None if no valid flag is found

def main():
    zip_filepath = '../dist/challenge.zip'
    extract_to = '../dist/unzipped_challenge'
    #unzip_file(zip_filepath, extract_to)
    flag = get_flag_from_file(extract_to)
    print(flag)

if __name__ == '__main__':
    main()
