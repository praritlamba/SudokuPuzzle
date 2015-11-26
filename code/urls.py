from django.conf.urls import patterns, url
from code import views

urlpatterns = patterns('',
	url(r'^home/$', views.input_sudoku, name='input'),
	url(r'^display/$', views.display_sudoku, name='display'),
	url(r'^solution/$', views.solve_sudoku, name='solution'),
	url(r'^nosolution/$', views.no_solution, name='no_solution'),
)
