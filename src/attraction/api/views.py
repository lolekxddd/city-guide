from django.db.models import Q
from rest_framework import generics, mixins
from attraction.models import Attraction
from .serializers import AttractionSerializer


class AttractionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    
    
    def get_queryset(self):
        qs = Attraction.objects.all()
        query = self.request.GET.get("city")
        query1 = self.request.GET.get("category")
        if query is not None:
            qs = qs.filter(Q(city=query))
        if query1 is not None:
            qs =qs.filter(Q(category=query1))    
        return qs

    

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AttractionRUDView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field      = 'pk'
    serializer_class  = AttractionSerializer
    

    def get_queryset(self):
        return Attraction.objects.all()