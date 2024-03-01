# core/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    # path('driver/', CustomUserListCreateView.as_view(), name='customuser-list-create'),
    # path('driver/<int:pk>/', CustomUserDetailView.as_view(), name='customuser-detail'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('user_type/<str:user_type>/', UserTypeListView.as_view(), name='user-type-list'),
    path('driver/', CustomUserAPIView.as_view(), name='custom-users-list-create'),
    path('driver/<int:pk>/', CustomUserAPIView.as_view(), name='custom-users-detail'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('update-password/', PasswordUpdateView.as_view(), name='update-password'),
    path('dummy/<int:id>', Dummy.as_view(), name='testfake'),
    path('location/', PDLocationCreateAPIView.as_view(), name='location'),
    path('near/<int:user_id>/', NearbyDriversAPIView.as_view(), name='nearby-drivers'),
    path('testoo/<int:id>/', testoo.as_view(), name='dlaa'),

]
