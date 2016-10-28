from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.searchCourses, name='search_courses'),
    url(r'^load_courses$', views.loadCourses, name='load_courses'),
    url(r'^admin/ip$', views.getIp, name='get_ip'),
    #url(r'^$', views.coursesIndex, name='courses_index'),
]