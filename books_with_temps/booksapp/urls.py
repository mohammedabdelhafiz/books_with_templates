from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    # path('showauthor', views.showauthor),	   
    path('addauthor', views.addauthor),
    path('author', views.author),	   
    path('viewbook/<int:id>', views.viewbook ,name="view_book"),
    path('viewauthor/<int:id>', views.authordesc ,name="view_author"),	   

]