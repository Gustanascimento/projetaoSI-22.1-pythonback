from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def cliente(data):
    ...

def loja(data):
    category = data['NotificationDto']['category']

    for user in data['NotificationDto']['userData']:
        user_info = payload_email_info(user)
        send_email_notification_loja(user_info, category)

def payload_email_info(data):
    return {
        "name": data['name'],
        "email": data['email']
    }


def send_email_notification_loja(user_data, category):
    subject = f'A categoria {category} está em alta!!'
    message = render_to_string(template_name='template_email/template_mercado.html', context={
        'name': user_data['name'].title(),
        'email': user_data['email'],
        'category': category
    })
    recipient_list = [user_data['email']]
    from_email = settings.EMAIL_HOST_USER
    response = send_mail(
                    subject=subject,
                    message='Ihuuuuuuuuu',
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                    html_message=message
                )
    
    #pprint("response: ", response) # email não pode ser enviado, email inválido ou inexistente
    return response


class SendEmailView(APIView):
    def post(self, request, format=None):
        if request.data:
            response = loja(request.data) if request.data['NotificationDto']['isMarket'] else cliente(request.data)

            if response == 1:
                return Response({'message': 'Email enviado com sucesso!'})

            return Response({'message': 'Erro ao enviar email!'})

        return Response({'message': 'Sem dados a enviar!'}, status=status.HTTP_400_BAD_REQUEST)
    
