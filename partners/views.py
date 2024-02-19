from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import DivisionSerializer

from .models import Division


@api_view(['GET'])
def get_divisions(request):
    divisions = Division.objects.order_by('code')
    query1 = request.GET.get('search')

    if query1 is None:
        query1 = ''

    divisions = divisions.filter(
        Q(code__icontains=query1)|
        Q(name__icontains=query1)
    )
    page = request.GET.get('page')
    paginator = Paginator(divisions, 150)

    try:
        divisions = paginator.page(page)
    except PageNotAnInteger:
        divisions = paginator.page(1)
    except EmptyPage:
        divisions = paginator.page(paginator.num_pages)

    if page is None:
        page = 1
    page = int(page)
    serializer = DivisionSerializer(divisions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_division(request):
    if request.method == 'POST':
        serializer = DivisionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
