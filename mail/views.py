# from django.conf import settings
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .service.mail import EmailService


class SendEmailView(APIView):
    def post(self, request, format=None):
        if request.data:
            # return exception(0) or success(1)
            email_service = EmailService(request.data)
            email_service.send_mail_by_user_type()

            if email_service:
                return Response(
                    {'message': 'Email enviado com sucesso!'},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {'message': 'Erro ao enviar email!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {'message': 'Sem dados a enviar!'},
            status=status.HTTP_400_BAD_REQUEST,
        )
