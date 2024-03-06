from django.urls import path
from .views import NewsList, UserLoginView


urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('login/', UserLoginView.as_view(), name='user-login')
]
