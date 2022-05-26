from django.db import models
from code_execution.domain.codeRunnerEngine import CodeRunnerEngine


class CodeExecutionResponse(models.Model):

    owner_id = models.CharField(max_length=100)
    execution_id = models.CharField(max_length=100)
    language = models.CharField(max_length=2, default='no')
    code = models.TextField(default="null")
    code_test = models.TextField(default="null")
    code_result = models.IntegerField()
    result = models.CharField(max_length=1000)

    def __int__(self):
        return self.language + " " + self.owner_id

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        runner: CodeRunnerEngine = CodeRunnerEngine(
            self.code,
            self.language
        )
        runner.create_file()
        result = runner.execute()
        self.code_result = result['returnCode']
        self.result = result['result']
        return super(CodeExecutionResponse, self).save()
