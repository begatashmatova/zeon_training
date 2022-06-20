from django.urls import include, path
from rest_framework import routers
from rest_framework import renderers
from .views import *


router = routers.DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'posts', PostViewSet)
router.register(r'news', NewsViewSet)
router.register(r'publicoffer', PublicOfferViewSet)
router.register(r'products', ProductViewSet)
router.register(r'novelty-products', NoveltyProductViewSet)
router.register(r'favorite-products', FavoriteProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'),),
    path(
        'similar-products/<int:pk>/<str:item>',
        SimilarProductViewSet.as_view({'get': 'list'})
    ),
    path(
        'products-collection/<int:collection_id>/<str:collection>',
        ProductCollectionViewSet.as_view({'get': 'list'})
    ),
    path('help/', HelpViewSet.as_view()),
    path('call-form/', call)
]
