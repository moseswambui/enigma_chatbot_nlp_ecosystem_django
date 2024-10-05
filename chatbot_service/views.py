from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserQuery
from .serializers import UerQuerySerializer
from chatbot_service.ml_model import chatbot_model


class ChatbotView(APIView):

    def post(self, request):
        question = request.data.get("question")
        response = chatbot_model.get_response(question)
        UserQuery.objects.create(user=request.user,
                                 question=question,
                                 response=response
                                )

        return Response({"question":question, "response": response})