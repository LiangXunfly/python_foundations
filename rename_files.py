import os

def rename_files():
    file_path = r'E:\python\python_foundations_uda\prank'
    file_list = os.listdir(file_path)
    for  file_name in file_list:
        os.rename(os.path.join(file_path, file_name), os.path.join(file_path, file_name.translate(None, "0123456789")))
rename_files()
