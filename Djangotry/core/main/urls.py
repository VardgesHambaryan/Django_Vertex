from django.urls import path
from .views import *

urlpatterns = [
   path('' , HommeListView.as_view() , name = 'home')
]

