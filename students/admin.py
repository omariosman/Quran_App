from django.contrib import admin

# Register your models here.

from .models import Shaikh, Student, Mentor, Student_Class, Surah_Quran


admin.site.register(Shaikh)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Surah_Quran)
admin.site.register(Student_Class)

