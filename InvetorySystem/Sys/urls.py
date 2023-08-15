from django.urls import path
from . import views
urlpatterns = [
    path ("", views.index),
    path ("order/", views.order),
    path ("staff/", views.staff),
    path ("product/", views.product),


]