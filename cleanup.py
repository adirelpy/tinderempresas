import os
import shutil

for root, dirs, files in os.walk("."):
    for dir_name in dirs:
        if dir_name == "__pycache__":
            full_path = os.path.join(root, dir_name)
            print(f"Eliminando: {full_path}")
            shutil.rmtree(full_path)
