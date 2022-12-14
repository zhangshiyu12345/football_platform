from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from user.models import NewUser

# Register your models here.

class NewUserAdmin(UserAdmin):

    #做表格切割(字段集标题,字段集信息)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name', 'sex', 'age', 'weight', 'stature', 'position', 'avatar', 'body', 'football_tream', 'defend', 'speed', 'hotshot', 'pass_football', 'control', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'roles')}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )

    list_display = ('id', 'username', 'roles', 'email', 'phone', 'age', 'sex', 'weight', 'stature', 'position', 'football_tream', 'body', 'defend', 'speed', 'control', 'speed', 'hotshot', 'pass_football', 'score', 'is_active', 'create_time', 'last_login')
    list_display_links = ('id', 'username', 'roles', 'email', 'body', 'football_tream', 'defend', 'speed', 'control', 'hotshot', 'pass_football', 'score', 'last_login') #跳转到修改页
    search_fields = ('username', 'email', 'sex', 'age', 'position', 'football_tream', 'score', 'roles',) #搜索框的提示文字

admin.site.register(NewUser, NewUserAdmin)


#class NoticeAdmin(admin.ModelAdmin):
    #list_display = ('id', 'title', 'author')
    #list_display_links = ('id', 'title') #要在list_display中出现
    #search_fields = ('title',)

#admin.site.register(Notice, NoticeAdmin)

