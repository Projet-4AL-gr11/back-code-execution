from django.db import models
from code_execution.domain.codeRunnerEngine import CodeRunnerEngine


class CodeExecutionResponse(models.Model):
    execution_id = models.IntegerField(unique=True)
    language = models.CharField(max_length=2, default='py')
    code = models.TextField(null=True, blank=True)
    code_result = models.IntegerField(null=True, blank=True)
    result = models.CharField(max_length=1000, null=True, blank=True)

    def __int__(self):
        return self.language + " " + str(self.execution_id)

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
