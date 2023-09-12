from django.shortcuts import render, HttpResponse
from .serializers import PersonSerializer
from rest_framework import generics, viewsets
from .models import Person

# Create your views here.
class PersonList(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Person.objects.all()
            name = self.request.query_params.get('name')
            if name:
                queryset = queryset.filter(name=name)
            return queryset
        else:
            return HttpResponse('<b>request.method cannot be a POST</b>')

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        id = self.kwargs['pk']
        queryset = Person.objects.all().filter(id=id)
        return queryset
    
class PersonDetailName(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = 'name'
    def get_queryset(self):
        name = self.kwargs['name']
        queryset = Person.objects.all().filter(name=name)
        return queryset