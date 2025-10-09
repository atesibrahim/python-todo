import pathlib
import zipfile

def make_archive(file_paths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zipf:
        for file in file_paths:
            zipf.write(file, arcname=pathlib.Path(file).name)

if __name__ == "__main__":
    make_archive(file_paths=["bonus1.py", "bonus2.py"], dest_dir="zip")