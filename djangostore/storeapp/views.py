import random
from itertools import chain
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CollectionSerializer, PostSerializer, NewsSerializer, PublicOfferSerializer, ProductSerializer, SimilarProductSerializer, ProductCollectionSerializer, FavoriteProductSerializer, HelpImageSerializer, HelpSerializer, MainPageSerializer, BenefitSerializer, FooterSerializer
from .pagination import CustomPageNumberPagination, CustomCollectionPagination
from .forms import CallForm
from .models import Collection
from .models import Post
from .models import News
from .models import PublicOffer
from .models import Product
from .models import Help
from .models import HelpImage
from .models import MainPage
from .models import Benefit
from .models import Footer

from django.core.paginator import Paginator

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    pagination_class = CustomPageNumberPagination
    serializer_class = CollectionSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    pagination_class = CustomPageNumberPagination
    serializer_class = NewsSerializer


class PublicOfferViewSet(viewsets.ModelViewSet):
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination


class SimilarProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SimilarProductSerializer

    def list(self, request, *args, **kwargs):
        coll_id = Product.objects.get(pk=kwargs['pk']).collection_id
        item = Product.objects.get(pk=kwargs['pk'])
        items = Product.objects.filter(collection_id=coll_id).exclude(id=item.id)
        if items.count() > 5:
            queryset = items.order_by('-id')[:5]
        else:
            queryset = items
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductCollectionViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCollectionSerializer

    def list(self, request, *args, **kwargs):
        items = Product.objects.filter(collection_id=kwargs['collection_id'])
        if items.count() > 12:
            queryset = items.order_by('-id')[:12]
        else:
            queryset = items
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NoveltyProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCollectionSerializer

    def list(self, request, *args, **kwargs):
        items = Product.objects.filter(novelty=True)
        if items.count() > 5:
            queryset = items.order_by('-id')[:5]
        else:
            queryset = items
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FavoriteProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = FavoriteProductSerializer

    def list(self, request, *args, **kwargs):
        items = Product.objects.filter(favorite=True)

        if len(items) == 0:
            items = []
            coll_list = list(Product.objects.values('collection_id').distinct())
            coll_amount = len(coll_list)
            i = 0
            collections = []
            while i < coll_amount:
                collections.append(coll_list[i]['collection_id'])
                i += 1

            for coll in collections:
                coll_items = Product.objects.filter(collection_id=coll)
                random_range = len(coll_items)
                item = coll_items[random.randrange(0, random_range)]
                items.append(item)

        if len(items) > 5:
            queryset = items.order_by('-id')[:5]
        else:
            queryset = items

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super(FavoriteProductViewSet, self).get_serializer_context()
        context.update({
            "favs": Product.objects.filter(favorite=True).count()
        })
        return context


class HelpViewSet(APIView):
    def get(self, request, *args, **kwargs):
        q1 = Help.objects.all()
        q2 = HelpImage.objects.all()

        ser1 = HelpSerializer(q1, many=True)
        ser2 = HelpImageSerializer(q2, many=True)

        return Response({'image': ser2.data, 'questions': ser1.data})


def call(request):
    form = CallForm
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'call.html', {'form': form})


class SearchProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        
        if queryset.count() == 0:
            items = []
            coll_list = list(Product.objects.values('collection_id').distinct())
            coll_amount = len(coll_list)
            i = 0
            collections = []
            while i < coll_amount:
                collections.append(coll_list[i]['collection_id'])
                i += 1

            for coll in collections:
                coll_items = Product.objects.filter(collection_id=coll)
                random_range = len(coll_items)
                item = coll_items[random.randrange(0, random_range)]
                items.append(item)

            if len(items) > 5:
                queryset = items.order_by('-id')[:5]
            else:
                queryset = items

        return queryset


class MainSlider(APIView):
    def get(self, request, *args, **kwargs):
        main_page = MainPage.objects.all()

        hits = Product.objects.filter(hits=True)
        if hits.count() > 8:
            hits = hits.order_by('-id')[:8]

        novelties = Product.objects.filter(novelty=True)
        if novelties.count() > 4:
            novelties = novelties.order_by('-id')[:4]

        collections = Collection.objects.all()
        if collections.count() > 4:
            collections = collections.order_by('-id')[:4]

        benefits = Benefit.objects.all()
        if benefits.count() > 4:
            benefits = benefits.order_by('-id')[:4]

        ser1 = MainPageSerializer(main_page, many=True)
        ser2 = ProductCollectionSerializer(hits, many=True)
        ser3 = ProductCollectionSerializer(novelties, many=True)
        ser4 = CollectionSerializer(collections, many=True)
        ser5 = BenefitSerializer(benefits, many=True)

        return Response({'main_page': ser1.data, 'hits': ser2.data, 'novelties': ser3.data, 'collections': ser4.data, 'benefits': ser5.data})


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
