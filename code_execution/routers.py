from rest_framework import routers
from .views import CodeRunnerViewSet


def get_router():
    router = routers.SimpleRouter()
    router.register("code", CodeRunnerViewSet, basename="code-runner")
    return router
