from rest_framework.serializers import ModelSerializer
from code_execution.models import CodeExecutionResponse


class CodeRunnerSerializer(ModelSerializer):

    class Meta:
        model = CodeExecutionResponse
        fields = "__all__"
