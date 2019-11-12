import os
import subprocess

class NotFoundError(Exception):
    pass


def get_pid():
    try:
        port = input('port: ')
        data = subprocess.check_output(f'NETSTAT.EXE -ano | findstr.exe :{port}', shell=True)
        data = data.split()
        pid = data[-1].decode("utf-8")
        return pid

    except:
        raise NotFoundError('lol')

def kill_process_by_pid(pid):
    os.system(f'TASKKILL /PID {pid} /F')


while True:
    choice = input('Press any key to continue. Y/n\n> ')
    if choice.lower() == 'n':
        print('GoodBye!')
        break

    try:
        pid = get_pid()
        kill_process_by_pid(pid)
    except NotFoundError:
        print('process not found.')

