from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import teacher_login, teacher_dashboard, claim_booking, tutor_list

urlpatterns = [
    path('login/', teacher_login, name='teacher_login'),
    path('dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('logout/', LogoutView.as_view(next_page='teacher_login'), name='logout'),
    path('claim/<int:booking_id>/', claim_booking, name='claim_booking'),
    path('tutors/', tutor_list, name='tutors'),
]
