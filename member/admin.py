from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from member.models import Member, BorrowRecord

class CustomUserAdmin(UserAdmin):
    model = Member
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active','is_staff','is_librarian')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','membership_date')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser','is_librarian', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active','is_staff','is_librarian')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('membership_date',)
admin.site.register(Member, CustomUserAdmin)

admin.site.register(BorrowRecord)
