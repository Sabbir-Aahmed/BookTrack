from django.contrib import admin
from .models import Member, BorrowRecord

admin.site.register(Member)
admin.site.register(BorrowRecord)
