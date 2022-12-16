from django.urls import path
from . import views

app_name = 'channel'

urlpatterns = [
    path('', views.channel_list, name="list"),
    path('create/', views.channel_create, name="create"),
    path('my_channel/', views.my_channel, name="myChannel"),

    path('update/<int:channel_id>', views.update_channel, name="update"),
    path('delete/<int:channel_id>', views.delete_channel, name="delete"),
    path('<slug:slug>/', views.channel_detail, name="detail"),
]