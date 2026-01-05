from fastapi import FastAPI, UploadFile
import os, shutil

from extractor import extract_zip, get_file_structure, read_files
from llm import generate_doc
from doc_generator import generate_txt, generate_pdf

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

@app.post("/generate-doc")
async def generate_documentation(file: UploadFile, format: str = "txt"):
    shutil.rmtree(UPLOAD_DIR, ignore_errors=True)
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)

    os.makedirs(UPLOAD_DIR)
    os.makedirs(OUTPUT_DIR)

    zip_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(zip_path, "wb") as f:
        f.write(await file.read())

    extract_zip(zip_path, UPLOAD_DIR)

    structure = get_file_structure(UPLOAD_DIR)
    files = read_files(UPLOAD_DIR)

    prompt = f"""
You are a software documentation generator.

Generate documentation with:
1. Project file structure
2. Purpose of each file
3. Explanation of code
4. Mention file name at the end of each section

FILE STRUCTURE:
{structure}

FILES CONTENT:
{files}
"""

    documentation = generate_doc(prompt)

    output_path = f"{OUTPUT_DIR}/project_documentation.{format}"

    if format == "pdf":
        generate_pdf(documentation, output_path)
    else:
        generate_txt(documentation, output_path)

    return {
        "status": "Documentation generated",
        "file": output_path
    }
