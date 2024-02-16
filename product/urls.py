from django.urls import path
from .views import *

urlpatterns = [

path('auto/<int:pk>/', AutoAPIUpdate.as_view()),
path('auto/', AutoAPIList.as_view()),
path('autodelete/<int:pk>/', AutoAPIDestroy.as_view()),

# path('house/<int:pk>/', HouseAPIUpdate.as_view()),
# path('house/', HouseAPIList.as_view()),
# path('housedelete/<int:pk>/', HouseAPIDestroy.as_view()),

]


