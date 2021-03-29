from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    @action(detail=False)
    def count(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        person_cnt = queryset.count()
        # person_cnt = Person.objects.annotate(Count('person_id'))
        content = {'count' : person_cnt}
        return Response(content)
