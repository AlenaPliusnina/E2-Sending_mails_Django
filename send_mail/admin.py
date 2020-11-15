from django.contrib import admin
from send_mail.models import Mail


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    pass

