from django.urls import path
from .views import UserRegisterView

# urls come here
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', UserRegisterView.as_view(), name='register'),( don't need because django sambhal lega)
]