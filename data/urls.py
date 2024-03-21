from django.urls import path
from data import views

urlpatterns = [
    path('', views.process_data, name='process_data'),
    path('getdetails/',views.get_details, name='getdetails'),
    path('delete/<int:id>', views.delete_rec, name='delete'),
    path('<int:id>', views.update_content, name='update')
]