from django.urls import path
from .views import home, person_loc_update_view, load_states, load_cities, continue_to_main_view

app_name = 'front_page_ip'

urlpatterns = [
    path('ip-home/', home, name='users_auth_home'),
    path('ip-home/continue', continue_to_main_view, name='continue-food'), 
    path('ip-home/get_loc', person_loc_update_view, name='get-loc-form'),
    path('ajax/load-states/', load_states, name='ajax_load_states'), # AJAX
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'), # AJAX
]