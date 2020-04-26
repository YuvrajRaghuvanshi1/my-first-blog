from django.urls import path
from blog import views

urlpatterns = [
   path('', views.post_list, name='post_list'),
   path('post/<int:pk>/', views.post_detail, name='post_detail'),
   path('post/new/', views.post_new, name='post_new'),
   path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
   path('about/', views.About, name='about'),
   path('search/',views.search,name='search'),
   path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
   path('post/<int:pk>/comments/', views.new_comment, name='comment_form'),

]
