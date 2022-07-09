import os


def on_server_start():
    os.system("docker build ./jsDockerExec -t sandbox_js")
    os.system("docker build ./pyDockerExec -t sandbox_py")
