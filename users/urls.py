from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import teacher_login, teacher_dashboard

urlpatterns = [
    path('login/', teacher_login, name='teacher_login'),
    path('dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('logout/', LogoutView.as_view(next_page='teacher_login'), name='logout'),
]
