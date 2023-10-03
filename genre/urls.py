from django.urls import path
from . import views

urlpatterns = [
    # genre/
    path('', views.index.as_view(), name='index'),

    #genre/1
    # path('<int:genre_id>', views.details, name='details')
    path('<pk>/', views.details.as_view(), name='details')
]