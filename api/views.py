from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Question, Choice
from .serializers import GetQuestionSerializer, CreateQuestionSerializer, ChoiceSerializer

@api_view(['GET', 'POST'])
def questions(request, **kwargs):
    if request.method == 'GET':
        if "id" in kwargs:
            result = Question.objects.get(pk=kwargs["id"])
            serializer = GetQuestionSerializer(result)
        else:
            result = Question.objects.all()
            serializer = GetQuestionSerializer(result, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['last_activity'] = timezone.now()
            serializer.validated_data['pub_date'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def choices(request, **kwargs):
    if "id" in kwargs:
        result = Choice.objects.get(pk=kwargs["id"])
        serializer = ChoiceSerializer(result)
    else:
        result = Choice.objects.all()
        serializer = ChoiceSerializer(result, many=True)
    return Response(serializer.data)