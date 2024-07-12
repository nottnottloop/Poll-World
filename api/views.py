from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

@api_view(['GET'])
def questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def choices(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)