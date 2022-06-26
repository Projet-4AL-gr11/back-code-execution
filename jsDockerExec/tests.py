from django.test import TestCase
import subprocess


class TestJSExecuteCode(TestCase):

    def test_js(self):
        r = subprocess.Popen(["cat", "./jsDockerExec/entryTest.js"], stdout=subprocess.PIPE)
        output = subprocess.run(["docker", "run", "--rm", "-i", "sandbox_js"],
                                stdin=r.stdout,
                                capture_output=True, text=True, timeout=1)
        print("message output : ", output)
