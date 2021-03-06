from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Truck
from .serializers import TruckSerializer

class TruckAPIView(APIView):

    def get(self, request):
        truck = Truck.objects.all()
        serializer = TruckSerializer(truck, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TruckSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TruckDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Truck.objects.get(id=id)
        except Truck.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        truck = self.get_object(id)
        serializer = TruckSerializer(truck)
        return Response(serializer.data)

    def put(self, request, id):
        truck = self.get_object(id)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        truck = self.get_object(id)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
