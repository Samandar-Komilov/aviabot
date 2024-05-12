from django.urls import path
from .views import NewsList, NewsDetail, UserLoginView


urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('login/', UserLoginView.as_view(), name='user-login')
]
