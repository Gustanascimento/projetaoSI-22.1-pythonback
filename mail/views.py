# from django.conf import settings
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .service.mail import EmailService


class SendEmailView(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: openapi.Response(
            description='Email sent successfully',
            examples={
                "application/json": {
                    'message': 'Email enviado com sucesso'
                }
            })},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'NotificationDto': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'category': openapi.Schema(type=openapi.TYPE_STRING),
                        'isMarket': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'userData': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'name': openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                    'email': openapi.Schema(
                                        type=openapi.TYPE_STRING
                                    ),
                                },
                            ),
                        ),
                        'marketProduct': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'marketName': openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                'productName': openapi.Schema(
                                    type=openapi.TYPE_STRING
                                ),
                                'price': openapi.Schema(
                                    type=openapi.TYPE_NUMBER
                                ),
                                'quantity': openapi.Schema(
                                    type=openapi.TYPE_NUMBER
                                ),
                            },
                        ),
                    },
                )
            },
        )
    )
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
