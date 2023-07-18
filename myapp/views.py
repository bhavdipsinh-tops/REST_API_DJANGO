from .models import Location,Item
from .serializers import ItemSerializer,LocationSerializer
from rest_framework import generics

class ItemList(generics.ListCreateAPIView):
	serializer_class=ItemSerializer

	def get_queryset(self):
		queryset=Item.objects.all()
		location=self.request.query_params.get('location')
		if location is not None:
			queryset=queryset.filter(itemLocation=location)
		return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class=ItemSerializer
	queryset=Item.objects.all()

class LocationList(generics.ListCreateAPIView):
	serializer_class=LocationSerializer
	queryset=Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class=LocationSerializer
	queryset=Location.objects.all()