from.import views
from django.urls import path
# from .views import course_selection, courses_by_department



urlpatterns = [

    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('department-courses/', views.department_courses, name='department_courses'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),


]

