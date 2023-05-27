from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User,Contact,Course,Category,Sub_Category,Sub_Sub_Category,Additional_Information



class Additional_Informations(admin.TabularInline):
    model=Additional_Information

class Course_Admin(admin.ModelAdmin):
    inlines=[Additional_Informations]

admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.register(Course,Course_Admin)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Sub_Sub_Category)
admin.site.register(Additional_Information)