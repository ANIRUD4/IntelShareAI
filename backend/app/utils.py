import os, shutil, time

def save_upload_file_tmp(upload_file, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    tmp_path = os.path.join(dest_folder, f'tmp_{int(time.time()*1000)}_{upload_file.filename}')
    with open(tmp_path, 'wb') as f:
        f.write(upload_file.file.read())
    return tmp_path

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
