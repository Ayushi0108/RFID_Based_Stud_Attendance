"""
URL configuration for RFID_Attendance_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #, include
from mark_attendance import views as mark_views
from user_authentication import views as user_views
from teacher_dashboard import views as teacher_views
from student_dashboard import views as student_views

handler404 = 'user_authentication.views.error_404'
handler500 = 'user_authentication.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1) user_authentication
    path('', user_views.start, name='start'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('change_pass/', user_views.change_pass, name='change_pass'),

    # 2) teacher_dashboard
    path('teacher_dashboard', teacher_views.dashboard, name='teacher_dashboard'),
    path('download/', teacher_views.download, name='download'),    
    path('send_email/', teacher_views.send_mail, name='send_mail'),

    # 3) student_dashboard
    path('student_dashboard', student_views.dashboard, name='student_dashboard'),

    # 4) mark_attendance
    path('mark/', mark_views.mark, name='mark'),   
    path('test/', mark_views.test, name='test'),
]


# Alternative way is to make separate urls file in each app and include that in this url file
# path('', include('user_authentication.urls')),
# # path('dashboard/',include('dashboard.urls')),
# path('mark/', include('mark_attendance.urls')),