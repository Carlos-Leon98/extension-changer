from pathlib import Path

def change_extension(file_path, new_extension):
    path = Path(file_path)
    new_file_path = path.with_suffix("." + new_extension)
    path.rename(new_file_path)