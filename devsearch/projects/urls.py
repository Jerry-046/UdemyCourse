from django.urls import path
from .import views
urlpatterns = [
    path('products/<str:pk>', views.products,name="products"),
    path('', views.index,name="Homepage"),
    path('product/', views.product,name="product"),
    path('create/', views.createProject,name="createProject"),
    path('update/<str:pk>', views.updateProject,name="updateProject"),
    path('delete/<str:pk>', views.deleteProject,name="deleteProject"),
    
    
]
