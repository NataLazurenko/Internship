from rest_framework import generics
from courses.models import Subject
from courses.api.serializers import SubjectSerializer
from django.http import QueryDict
from django.http.multipartparser import MultiPartParser


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer