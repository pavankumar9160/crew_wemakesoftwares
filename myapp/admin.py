from django.contrib import admin
from .models import  User, Message , ChatRequest ,ConsentQuestion,ConsentOption,ConsentAnswer,HistoryCapturedImage,Video,CallBackRequest,UserInfo
# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(ChatRequest)
admin.site.register(ConsentQuestion)
admin.site.register(ConsentOption)
admin.site.register(ConsentAnswer)
admin.site.register(HistoryCapturedImage)
admin.site.register(Video)
admin.site.register(CallBackRequest)
admin.site.register(UserInfo)

