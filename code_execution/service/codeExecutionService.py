from code_execution.models import CodeExecutionResponse
from code_execution.domain.codeRunnerEngine import CodeRunnerEngine


class CodeExecutionService:

    def __int__(self, instance: CodeExecutionResponse, runner: CodeRunnerEngine):
        self.instance = instance
        self.runner = runner

    def exec_before_insert(self):
        self.runner.create_file()
        return self.runner.execute()

    def insert(self, obj: dict):
        self.instance.code_result = obj['returnCode']
        self.instance.result = obj['result']
