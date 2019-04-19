import os
import json
import subprocess

def save_file(path, data: str):
    """保存文件到filepath指定的路径中"""
    with open(path, 'wb') as up:
        up.write(data.encode("utf-8"))

def compile(dir_path, data, file_name):
    file_path = dir_path + file_name
    save_file(file_path, data)
    output_path = os.path.splitext(file_path)[0] + ".out"
    cmd = "gcc -g " + file_path + " -o " + output_path
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_output, err_output) = proc.communicate()
    return (err_output, std_output)

def start(dir_path, file_name):
    cmd = "./" + dir_path + os.path.splitext(file_name)[0] + ".out"
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    (std_output, err_output) = proc.communicate()
    return (err_output, std_output)

def open_file(dir_path, file_name):
    file_path = dir_path + file_name
    with open(file_path) as f:
        message = {
            "task": "openfile",
            "filename": file_name,
            "data": f.read()
        }
    return json.dumps(message)
