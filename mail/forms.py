
from django import forms
from django.conf import settings
from django.core.mail import send_mail


class PayloadEmail(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    from_email = forms.EmailField(required=False)
    recipient_list = forms.CharField(widget=forms.Textarea)

    def send_email(self, market):
        cl_data = super().clean()
        name = cl_data.get('name').strip()
        from_mail = cl_data.get('from_email')
        subject = cl_data.get('subject')
        msg = f'{name} with email {from_mail} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg        

        def send(self):
            subject, msg = self.get_info()
            send_mail(
                subject=subject,
                msg=msg,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
