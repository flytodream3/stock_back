from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import StockUser, Profile


class StockUserCreationForm(UserCreationForm):
    class Meta:
        model = StockUser
        fields = ('is_stock_user',)


class StockUserChangeForm(UserChangeForm):
    class Meta:
        model = StockUser
        fields = ('password', 'first_name', 'last_name', 'email', 'is_manager', 'is_stock_user', 'is_staff')


@admin.register(StockUser)
class StockUserAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'phone', 'email', 'is_manager', 'is_stock_user'
    )
    list_filter = ('is_manager', 'is_stock_user')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal', {'fields': ('email', 'first_name', 'last_name', 'phone')}),
        ('Permissions',
         {'fields': (
             'is_active', 'is_staff', 'is_superuser', 'is_stock_user',
             'is_manager', 'groups', 'user_permissions'
         )
          }
         ),
        ('Info', {'fields': ('date_joined', 'last_login')})
    )
    ordering = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')


admin.site.register(Profile)