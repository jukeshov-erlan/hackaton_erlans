from django.urls import path
from api.views import *

urlpatterns = [
    path('code-explain/', CodeExplainView.as_view(), name='code-explain')
]