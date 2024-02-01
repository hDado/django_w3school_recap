from django.contrib import admin
from .models import Member
# Register your models here.


class MemberAdmin(admin.ModelAdmin): #horizontal bar member admin
    list_display = ("firstname", "lastname", "joined_date")


admin.site.register(Member, MemberAdmin)
