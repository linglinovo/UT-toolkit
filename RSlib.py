from ctypes import windll
from sys import exit
from sys import platform
from sys import executable
import psutil
import os
from win32com.client import GetObject
from tqdm import tqdm
import zipfile
def doadmin():
    if platform.startswith('win'):
        isadmin = windll.shell32.IsUserAnAdmin()
        if not isadmin:
            windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
            exit()
def dokilltask(process_name):
    try:
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.terminate()
    except:
        return False
def find(filename,root,step,a):
    root = str(root)
    step = int(step)
    filename = str(filename)
    runningstep = 0
    if step == 0:
        return False
    for path, dirs, files in os.walk(root, topdown=True):
        runningstep = runningstep + 1
        print(path)
        print(dirs)
        print(files)
        if filename in files:
            if a:
                outputpath = path+"/"+filename
                return outputpath
            else:
                outputpath = path
                return outputpath
        if runningstep > step:
            return False
def checktask(process_name):
    wmi = GetObject('winmgmts:')
    processes = wmi.InstancesOf('Win32_Process')
    for process in processes:
        if process.Name.lower() == process_name.lower():
            return True
    return False


def dozipfile(src_dir, save_name='default'):
    if save_name == 'default':
        zip_name = src_dir + '.zip'
    else:
        if save_name is None or save_name == '':
            zip_name = src_dir + '.zip'
        else:
            zip_name = save_name + '.zip'

    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print(0)
        return False
    return True


def gettaskpath(taskname):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['name'] == taskname:
            return proc.info['exe']
    return None


def replace_line_in_file(file_path, line_number, new_line):
    with open(file_path, "r",errors = 'ignore') as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        lines[line_number - 1] = new_line + "\n"

        with open(file_path, "w") as file:
            file.writelines(lines)
