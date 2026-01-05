import zipfile
import os

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

def get_file_structure(base_path):
    structure = []
    for root, _, files in os.walk(base_path):
        for file in files:
            structure.append(os.path.relpath(os.path.join(root, file), base_path))
    return structure

def read_files(base_path):
    files_content = {}
    for root, _, files in os.walk(base_path):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    files_content[file] = f.read()
            except:
                pass
    return files_content
