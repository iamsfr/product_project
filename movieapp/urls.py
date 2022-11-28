from . import views
from django.urls import path
app_name = 'movieapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('movie/<int:id>/',views.detail,name='movie'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]