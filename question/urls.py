from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('<int:id>/detail/',views.detail,name='detail'),
    path('<int:id>/comment/create/',views.comment_create,name='comment_create'),
]

