from django.urls import path
from fuzail_app.views import index

urlpatterns = [
    path("",index,name="index")
]
