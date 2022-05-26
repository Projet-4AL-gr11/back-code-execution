from django.test import TestCase
import subprocess
from subprocess import STDOUT, check_output, PIPE, check_call

class TestJSExecuteCode(TestCase):

    def testJs(self):
        r = check_output(['docker', 'run', '--rm', 'sanbox_test'], stderr=STDOUT, timeout=5, shell=True)
        print("output ----->> ", r)

    def testJs2(self):
        r = check_call(['docker', 'run', '--rm', 'sanbox_test'], stderr=STDOUT, timeout=5, shell=True)
        print("output ----->> ", r)

    def test_js(self):
        r = subprocess.run(
            "docker run --rm sanbox_test",
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=5
        )
        print("message output : ", r)

    def test_py(self):
        r = subprocess.run(
            "pwd",
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=5
        )
        print("message output : ", r)
