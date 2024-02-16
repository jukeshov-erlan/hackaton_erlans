from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *

class AutoAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3

class AutoAPIList(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = AutoAPIListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['mark', 'model']
    ordering_fields = ['price', 'mark']

    

class AutoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication)

class AutoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAdminOrReadOnly, )




# class HouseAPIList(generics.ListCreateAPIView):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )


# class HouseAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#     permission_classes = (IsAuthenticated, )
#     # authentication_classes = (TokenAuthentication)

# class HouseAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#     permission_classes = (IsOwnerOrReadOnly, )






