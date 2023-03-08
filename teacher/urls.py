from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
  path('home_page',views.t_home,name='hom'),
  path('profile',views.prof,name='prof'),
  path('add_student',views.add_st,name='add_st'),
  path('view_student',views.view_st,name='view_st'),
  path('change_password',views.chg_pwd,name='chg_pwd'),
  path('logout',views.logout, name='logout')
]