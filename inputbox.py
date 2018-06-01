import subprocess
import os
def myrun(cmd):
    """from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    import subprocess
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    p.stdin.write(b"input")
    p.stdout.readline()
    p.stdin.write(b"input")
    stdout = []
    while True:

        line = p.stdout.readline()
        stdout.append(line)
        print(line.decode())
        if line == '' and p.poll() != None:
            break

    return ''.join(stdout)

myrun("D:\\EPA\\AERScreen\\aerscreen_code\\AERSCREEN")



