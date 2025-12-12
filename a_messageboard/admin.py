from django.contrib import admin
from .models import MessageBoard, Message

admin.site.register(MessageBoard)
admin.site.register(Message)