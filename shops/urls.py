from django.urls import path
from .views import (
    shop_map,
    create_shop,
    update_shop,
    delete_shop,
    view_shops,
    custom_login,
    signup_view,
    custom_logout,
)

urlpatterns = [
    # Dashboard / Map
    path('', shop_map, name='shop_map'),

    # Authentication
    path('login/', custom_login, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', custom_logout, name='logout'),

    # Shop CRUD
    path('create-shop/', create_shop, name='create_shop'),
    path('update-shop/<int:pk>/', update_shop, name='update_shop'),
    path('delete-shop/<int:pk>/', delete_shop, name='delete_shop'),
    path('view-shops/', view_shops, name='view_shops'),
]


