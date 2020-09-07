from django.contrib import admin
from twitteruser.models import TwitterUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = TwitterUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('following',)}),
    )
# Register your models here.
admin.site.register(TwitterUser,MyUserAdmin)


