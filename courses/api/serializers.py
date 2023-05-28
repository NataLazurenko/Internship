from rest_framework import serializers
from courses.models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
