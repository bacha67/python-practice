from pathlib import Path # Path is a class in the pathlib module that provides an object-oriented interface for working with file system paths. It allows you to manipulate and interact with file paths in a more intuitive way compared to traditional string-based path handling.
from PyPDF2 import PdfWriter, PdfReader#

root = Path(__file__).resolve().parent
source_path = root / '/Users/shadow/Desktop/python-practice/National _exit.pdf'
dest_path = root / 'National_exit_encrypted.pdf'

with source_path.open('rb') as source_file:
    reader = PdfReader(source_file)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt('12340')

    with dest_path.open('wb') as out_file:
        writer.write(out_file)
        

print(f'PDF encrypted ({len(reader.pages)} pages copied)')
