from django.contrib import admin
from .models import News, Users, Appeals, Schedulefile

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'surname', 'patronymic', 'email', 'recordbook',)
admin.site.register(Users, UsersAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
admin.site.register(News, NewsAdmin)

class AppealsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'content')
admin.site.register(Appeals, AppealsAdmin)

class SchedulefileAdmin(admin.ModelAdmin):
    pass
    # list_display = ()
admin.site.register(Schedulefile, SchedulefileAdmin)
