import subprocess


class CodeRunnerEngine:

    def __init__(self, code: str, language: str):
        self.language = language
        self.code = code
        self.output = {}

    def create_file(self):
        if self.language == 'py':
            file = open("executable.py", "w")
            file.write(self.code + "\n")
            file.close()

        if self.language == 'js':
            file = open("executable.js", "w")
            file.write(self.code + "\n")
            file.close()

    def execute(self) -> dict:
        if self.language is not None and self.code is not None:
            if self.language == 'py':
                r = subprocess.Popen(["cat", "executable.py"], stdout=subprocess.PIPE)
                output = subprocess.run(["docker", "run", "--rm", "-i", "sandbox_py"],
                                        stdin=r.stdout,
                                        capture_output=True, text=True)
                self.output['returnCode'] = output.returncode
                if output.stderr == '':
                    self.output['result'] = output.stdout
                else:
                    self.output['result'] = output.stderr
                return self.output

            elif self.language == 'js':
                r = subprocess.Popen(["cat", "executable.js"], stdout=subprocess.PIPE)
                output = subprocess.run(["docker", "run", "--rm", "-i", "sandbox_js"],
                                        stdin=r.stdout,
                                        capture_output=True, text=True)
                self.output['returnCode'] = output.returncode
                if output.stderr == '':
                    self.output['result'] = output.stdout
                else:
                    self.output['result'] = output.stderr
                return self.output
            else:
                raise Exception('Cannot execute file with this extension: {}', self.language)
