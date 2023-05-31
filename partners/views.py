from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    paginator = Paginator(divisions, 15)

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
    return Response(
        {
            'divisions': serializer.data,
            'page': page,
            'pages': paginator.num_pages
        }
    )
