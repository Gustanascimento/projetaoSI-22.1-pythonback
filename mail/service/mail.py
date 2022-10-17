from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response


class EmailService:
    def __init__(self, user_notification_data):
        self.user_nd = user_notification_data

    def send_mail_by_user_type(self):
        if self.user_nd['NotificationDto']['isMarket']:
            self.send_mail_to_shops()
        else:
            self.send_mail_to_clients()

    def send_mail_to_shops(self):
        category = self.user_nd['NotificationDto']['category']

        for user in self.user_nd['NotificationDto']['userData']:
            user_info = self.payload_user_info(user)
            self.send_featured_category_notification_to_shops(
                user_info, category
            )

    def send_featured_category_notification_to_shops(
        self, user_data, category
    ):
        subject = f'A categoria {category} está em alta!!'
        message = render_to_string(
            template_name='template_email/template_mercado.html',
            context={
                'name': user_data['name'].title(),
                'email': user_data['email'],
                'category': category,
            },
        )
        recipient_list = [user_data['email']]
        from_email = settings.EMAIL_HOST_USER
        response = send_mail(
            subject=subject,
            message='Ihuuuuuuuuu',
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
            html_message=message,
        )

        # pprint(
        #     'response: ', response
        # )   # email não pode ser enviado, email inválido ou inexistente
        return response

    def payload_user_info(self, data):
        return {'name': data['name'], 'email': data['email']}

    def send_mail_to_clients(self):
        product_info = self.user_nd['NotificationDto']['marketProduct']

        for user in self.user_nd['NotificationDto']['userData']:
            user_info = self.payload_user_info(user)
            self.send_product_notification_to_clients(user_info, product_info)

    def send_product_notification_to_clients(self, user_data, product_info):
        subject = (
            'Opa, opa, para tudo!! O seu produto desejado está em promoção!!'
        )
        message = render_to_string(
            template_name='template_email/template_usuario.html',
            context={
                'userName': user_data['name'].title(),
                'productName': product_info['productName'],
                'itemPrice': product_info['price'],
                'marketName': product_info['marketName'],
            },
        )

        recipient_list = [user_data['email']]
        from_email = settings.EMAIL_HOST_USER

        response = send_mail(
            subject=subject,
            message='Ihuuuuuuuuu',
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
            html_message=message,
        )

        # pprint(
        #     'response: ', response
        # )   # email não pode ser enviado, email inválido ou inexistente
        # pprint("response: ", response) # email não pode ser enviado, email inválido ou inexistente
        return response
