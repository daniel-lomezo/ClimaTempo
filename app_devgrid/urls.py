from django.urls import path, include
from app_devgrid.views import curriculo_inicio
from app_devgrid.views import viewexperiencia
from app_devgrid.views import submitemail
from app_devgrid.views import submit_telegram



urlpatterns = [
	path('dadospessoais/', curriculo_inicio, name='curriculo_inicio'),
	path('experiencias/', viewexperiencia, name='view_experiencia'),
	path('enviatelegram/submit/', submit_telegram, name='envia_telegram'),
	path('enviaemail/submit/', submitemail, name='envia_email'),


	]
