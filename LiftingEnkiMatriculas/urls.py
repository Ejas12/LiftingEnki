from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_menu, name='Pagina Principal'),
    url(r'?P<student_id_selected>[0-9999]+_/$', views.student_detail, name='Detalles del Estudiante')
   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
