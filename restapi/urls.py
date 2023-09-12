from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.PersonList.as_view(), name='person_list'),
   
    path('<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
    #  path('<str:name>/', views.PersonDetailName.as_view(), name='person_detail_name'),
]
