from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StockRoom
from .serializers import StockRoomSerializer


@api_view(['GET'])
def get_stockrooms(request):
    srockrooms = StockRoom.object.order_by('name')
    serializer = StockRoomSerializer(srockrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_stockroom(request, room_id):
    stockroom = StockRoom.objects.get(id=room_id)
    serializer = StockRoomSerializer(stockroom, many=False)
    return Response(serializer.data)
