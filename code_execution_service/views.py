from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomeView(APIView):

    def get(self, request):
        return Response("api up and working", status=status.HTTP_200_OK)