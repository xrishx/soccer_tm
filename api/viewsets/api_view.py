from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

class APILogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
