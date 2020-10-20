from django.contrib import admin
from .models import SessionYear,YearNum,Post,Subject,Profile
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(SessionYear , BookAdmin)
admin.site.register(Post)
admin.site.register(YearNum)
admin.site.register(Subject)
admin.site.register(Profile)