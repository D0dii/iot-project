from django.shortcuts import render

from .serializers import QuestionSerializer, UserAnswerSerializer, UserSerializer
from .models import Question, User, UserAnswer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .mqtt_client import publish_message
from .mqtt_client import client

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        publish_message(client, "backend", serializer.data["id"])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "pk"
    def update(self, request, *args, **kwargs):
        publish_message(client, "backend", "-2")
        return super().update(request, *args, **kwargs)

class UserAnswerListCreate(generics.ListCreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def list(self, request, *args, **kwargs):
        userAnswers = UserAnswer.objects.all()
        serializedUserAnswers = self.get_serializer(userAnswers, many=True)

        questions = Question.objects.all()
        serializedQuestions = QuestionSerializer(questions, many=True)

        userAnswersQuestions = {}

        for question in serializedQuestions.data:
            userAnswersQuestions[question['id']] = []

        for userAnswer in serializedUserAnswers.data:
            userAnswersQuestions[userAnswer['question']].append(userAnswer['answer'])

        userAnswersResponse = []
        for question in serializedQuestions.data:
            userAnswersResponse.append({
                'id': question['id'],
                'title': question['title'],
                'question': question['question'],
                'za': userAnswersQuestions[question['id']].count('za'),
                'przeciw': userAnswersQuestions[question['id']].count('przeciw'),
                'wstrzymal sie': userAnswersQuestions[question['id']].count('wstrzymal sie')
            })

        return JsonResponse(userAnswersResponse, safe=False)

class UserAnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    lookup_field = "pk"