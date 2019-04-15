import subprocess

def save_file(path, data):
    """保存文件到filepath指定的路径中"""
    with open(path, 'w') as up:
        up.write(data)

def compile(filepath, message, outpath):
    save_file(filepath, message['data'])
    cmd = "gcc -g " + filepath + " -o " + outpath
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_output, err_output) = proc.communicate()
    return (err_output, std_output)

def start():
    cmd = "./files/source.out"
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return proc