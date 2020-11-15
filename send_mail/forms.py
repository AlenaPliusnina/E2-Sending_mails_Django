from django import forms
from send_mail.models import Mail


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = '__all__'
