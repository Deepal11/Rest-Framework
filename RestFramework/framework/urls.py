from django.urls import path
from . import views

urlpatterns = [
    path('',views.viewList.as_view(),name='viewlist'),
    path('<int:pk>/',views.viewDetail.as_view(),name='viewdetail')
]