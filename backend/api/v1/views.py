from rest_framework.views import APIView
from rest_framework.response import Response
from http import HTTPStatus


class TestAPIView(APIView):
    def get(self, request):
        return Response({'status': HTTPStatus.OK})
