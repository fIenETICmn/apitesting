from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from testeg.views import *
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from testeg.api.viewset import UserViewSet, ProductViewSet
from testeg.api import viewset

router = DefaultRouter()

router.register(r'users', viewset.UserViewSet)
router.register(r'products', viewset.ProductViewSet)

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
#
# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    # path('', api_root),
    # path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),

])
urlpatterns += router.urls
