from django.urls import path
from .views import *

urlpatterns = [
    path('index_1', index_1.as_view(), name='index'), # CBV
    path('objects', ObjectsView.as_view(), name='objects'), # CBV
    path('detail_object/<pk>', ObjectDetailView.as_view(), name='detail_object'), # CBV
    path('create_object', ObjectCreateView.as_view(), name='create_object'), # CBV
    path('edit_object/<pk>', ObjectUpdateView.as_view(), name='edit_object'), # CBV
    path('delete_object/<pk>', ObjectDeleteView.as_view(), name='delete_object'), # CBV
    path('index_2', index_2, name='index_2'),
]