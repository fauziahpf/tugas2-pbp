from django.urls import path
from mywatchlist.views import * 

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('<str:format>/', show_wl, name='show_wl'),
    # path('html/', show_watchlist, name='show_watchlist'),
    # path('xml/', show_xml, name='show_xml'),
    # path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]