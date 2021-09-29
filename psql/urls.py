from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_data, name="create"),
    path("db/", views.db_up, name="db"),
    path("replica/", views.use_replica, name="replica"),
    path("down/", views.db_down, name="create"),
]
