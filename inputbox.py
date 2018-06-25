import subprocess
import os
# def myrun(cmd):
#     """from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
#     """
#     #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#
#     import subprocess
#     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#     p.stdin.write(b"input\n")
#
#     stdout = []
#     while True:
#
#         line = p.stdout.readline()
#         stdout.append(line)
#         print(line.decode())
#         if line == '' and p.poll() != None:
#             break
#
#     return ''.join(stdout)
#
# myrun("D:\\EPA\\AERScreen\\aerscreen_code\\AERSCREEN")

def create_grid(*commands):
    process = subprocess.Popen(
        ["D:\\EPA\\AERScreen\\aerscreen_code\\AERSCREEN"],
        stdin=subprocess.PIPE)

    process.communicate(bytes('\n'.join(commands) + '\n','UTF-8'))

if __name__ == '__main__':
    create_grid('grid', 'E', 'P','20','20','20','0','1','10','U','10000','3.3','1',
                                                                               'n','y','1000','n','n','10','LATLON','34.6677','12.2222','4')

