from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('products/<str:pk>', views.products,name="products"),
    path('', views.index,name="Homepage"),
    path('product/', views.product,name="product"),
    path('create/', views.createProject,name="createProject"),
    path('update/<str:pk>', views.updateProject,name="updateProject"),
    path('delete/<str:pk>', views.deleteProject,name="deleteProject"),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
