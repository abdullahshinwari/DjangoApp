from django.urls import path
from Article import views


urlpatterns = [
    path('', views.hello_world),
    path('hello', views.hello_world),
    path('create-user', views.create_user),
    path('show-all-users', views.show_all_users),
    path('show-user', views.show_user),
    path('update-user', views.update_user),
    path('delete-user', views.delete_user),
    path('moralis-api', views.moralis_api),
]
