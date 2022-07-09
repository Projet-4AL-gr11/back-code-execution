import os
import subprocess
import sys

file = open("exec.py", "w")
for line in sys.stdin:
    file.write(line + "\n")
file.close()
os.system("chmod 777 exec.py")
subprocess.run(["python", "exec.py"], shell=False, timeout=1)
