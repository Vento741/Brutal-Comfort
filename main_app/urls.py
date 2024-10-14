from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('services/', views.services, name='services'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('contact/', views.contact, name='contact'),
    path('consultation/', views.consultation, name='consultation'),
]