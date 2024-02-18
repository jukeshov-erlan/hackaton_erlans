from rest_framework import views, status
from rest_framework.response import Response
from api.serializers import CodeExplainSerializer
from django.contrib.auth import get_user_model
from .models import CodeExplainer


User = get_user_model()


class CodeExplainView(views.APIView):
    serializer_class = CodeExplainSerializer

    def get(self, request, format=None):
        queryset = CodeExplainer.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class UserVIew(views.APIView):
#     serializer_class = UserSerializer
#     def get(self, request, format=None):
#         queryset = User.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
# class TokenView:
#     pass