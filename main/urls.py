from django.urls import path
from main.views import show_main, create_material_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_material
from main.views import delete_material, add_material_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_material_entry', create_material_entry, name='create_material_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-material/<uuid:id>', edit_material, name='edit_material'),
    path('delete/<uuid:id>', delete_material, name='delete_material'), # sesuaikan dengan nama fungsi yang dibuat
    path('add-material-entry-ajax/', add_material_entry_ajax, name='add_material_entry_ajax'),
]