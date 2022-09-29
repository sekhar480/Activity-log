from django.urls import path
from . import views
app_name = 'activitylog_app'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('detail/<int:pk>', views.comment_detail, name='comment_detail'),
    path('form/', views.new_comment, name='new_comment'),
    path('update_comment/<int:pk>', views.update_comment, name='update_comment'),
    ]