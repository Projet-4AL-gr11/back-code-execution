from django.test import TestCase
import subprocess


class TestJSExecuteCode(TestCase):

    def test_py(self):
        r = subprocess.Popen(["cat", "./pyDockerExec/entryTest.py"], stdout=subprocess.PIPE)
        output = subprocess.run(["docker", "run", "--rm", "-i", "sandbox_py"],
                                stdin=r.stdout,
                                capture_output=True, text=True)

        print("message output : ", output)
