from django.contrib import admin
from .models import YearNum,Post,Subject,Profile,Advertising
# Register your models here.


admin.site.register(Post)
admin.site.register(YearNum)
admin.site.register(Subject)
admin.site.register(Profile)
admin.site.register(Advertising)