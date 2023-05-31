from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DivisionSerializer

from .models import Division


@api_view(['GET'])
def get_divisions(request):
    divisions = Division.objects.order_by('code')
    serializer = DivisionSerializer(divisions, many=True)
    return Response(serializer.data)
