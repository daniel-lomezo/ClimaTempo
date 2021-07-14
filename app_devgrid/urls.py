from django.urls import path, include
from app_devgrid.views import index_view
from app_devgrid.views import api_get_city_names
from app_devgrid.views import api_get_city_names_filter_data




urlpatterns = [
	path('views/', index_view, name='index'),
	path('get_filter_list_citys/<str:country>/', api_get_city_names_filter_data, name='get_filter_list_citys'),
	path('get_list_citys/', api_get_city_names, name='get_list_citys'),
	
	]
