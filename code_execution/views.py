from rest_framework.viewsets import ModelViewSet
from code_execution.domain.codeRunnerSerializer import CodeRunnerSerializer
from code_execution.models import CodeExecutionResponse


class CodeRunnerViewSet(ModelViewSet):

    serializer_class = CodeRunnerSerializer

    def get_queryset(self):
        queryset = CodeExecutionResponse.objects.all()
        return queryset
