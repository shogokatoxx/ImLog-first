from django.urls import path
from . import views

app_name = 'logapp'

urlpatterns = [
    path('',views.top_page,name='top_page'),
    path('lists/',views.lists,name='lists'),
    path('lists/<int:pk>',views.log_detail,name='log_detail'),
    path('usertitle/',views.user_title,name="user_title"),
    path('new_title/',views.new_title,name='new_title'),
    path('edit_title/<int:pk>',views.edit_title,name='edit_title'),
    path('user_detail<int:pk>',views.user_detail,name='user_detail'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('good/<int:pk>',views.good,name='good'),
]
