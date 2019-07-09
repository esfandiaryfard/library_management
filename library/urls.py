from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path

book_list = BookViewset.as_view({
    'get': 'index'
})

urlpatterns = format_suffix_patterns([
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('books', book_list, name='book_list'),
])

