from .models import Truck
from .serializers import TruckSerializer
from rest_framework import mixins, generics

class GenericAPIView(generics.GenericAPIView, 
            mixins.ListModelMixin, 
            mixins.CreateModelMixin, 
            mixins.RetrieveModelMixin, 
            mixins.UpdateModelMixin, 
            mixins.DestroyModelMixin):

    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):

        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
