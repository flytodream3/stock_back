from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.models import Category
from warehouse.models import Product

from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.order_by('name')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    products = Product.objects.all()
    query1 = request.GET.get('search')

    if query1 == None:
        query1 = ''

    products = products.filter(
        Q(name__icontains=query1)|
        Q(as_key__icontains=query1)|
        Q(p_num__icontains=query1)
    )
    page = request.GET.get('page')
    paginator = Paginator(products, 50)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page is None:
        page = 1
    page = int(page)
    serializer = ProductSerializer(products, many=True)
    return Response(
        {
            'products': serializer.data,
            'page': page,
            'pages': paginator.num_pages
        }
    )


@api_view(['GET'])
def get_product(request, prod_id):
    product = Product.objects.get(id=prod_id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
