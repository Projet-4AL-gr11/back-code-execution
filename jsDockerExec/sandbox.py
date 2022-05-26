import os
import subprocess
import sys

file = open("exec.js", "w")
for line in sys.stdin:
    file.write(line + "\n")
file.close()
os.system("chmod 777 exec.js")
subprocess.run(["node", "exec.js"], shell=False, timeout=1)
