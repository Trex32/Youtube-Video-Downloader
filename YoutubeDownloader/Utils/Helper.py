import os
import shutil

def create_directory_if_not_exist(directory_name):
    if os.path.exists(directory_name)==False:
        os.makedirs(directory_name)

def create_directory_if_exist_delete(directory_name):
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    os.makedirs(directory_name)