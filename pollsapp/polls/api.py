from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import Question, Choice,Track

class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')

class QuesViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
class TrackListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id','name')
class TrackListCreateViewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
