from django.urls import path

from movieapp import views
app_name='movieapp'
urlpatterns = [
    path('', views.function, name="function"),
    path('movie/<int:movie_id>/', views.details, name="details"),
    path('add/', views.add, name='add'),
    path('update/<int:movie_id>/', views.update, name="update"),
    path('delete/<int:movie_id>/',views.delete,name='delete')
]
