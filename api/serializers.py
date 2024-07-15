from rest_framework import serializers
from polls.models import Question, Choice

class GetQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceSerializer(serializers.ModelSerializer):
    #not bad too
    #question = QuestionSerializer()
    question = serializers.StringRelatedField()
    class Meta:
        model = Choice
        fields = '__all__'