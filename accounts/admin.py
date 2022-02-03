from django.contrib import admin

# Register your models here.
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    #account page display
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    # added last after all editable fields
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    search_fields = ('username', 'email',)

    list_filter = ('username', 'date_joined')

    #
    filter_horizontal = ()

    #make the password read-only
    fieldsets = ()

admin.site.register(Account, AccountAdmin)