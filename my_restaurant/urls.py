from django.urls import path
from my_restaurant import views
from .views import RegisterAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/danirestaurant/', views.dani_restaurants, name='danirestaurant'),
    path('api/danirestaurant/<int:id>/', views.dani_restaurant, name='danirestaurant'),
    path('api/customers/', views.customers, name='customers'),
    path('api/customers/<int:id>/', views.customer, name='customer'),
    path('api/order/', views.orders, name='order'),
    path('api/order/<int:id>/', views.order, name='order'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]