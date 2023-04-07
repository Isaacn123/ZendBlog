from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('policy', views.PolicyPage.as_view(), name='policy')
    path('policy', views.Policy, name='policy' ),
    path('contact', views.Contact, name='contact'),
    
  
]