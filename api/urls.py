from django.urls import path
from api.v1.product import *
# from api.methodizm.views import MainView

from api.v1.auth import *

urlpatterns = [
    path('register/', RegisView.as_view()),
    path('login/', LoginView.as_view()),
    path('crud/', CrudView.as_view()),
    path('crud/<int:pk>/', CrudView.as_view()),
]