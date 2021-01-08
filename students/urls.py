from django.conf.urls import url
from django.urls import path


from . import views

app_name="students"

urlpatterns = [
    url(r'^add_student_class/$', views.add_student_class, name='add_student_class'),
    url('', views.home, name='home'),

   

]
