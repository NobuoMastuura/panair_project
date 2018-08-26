from django.contrib import admin

from .models import Lesson, User, Attend, Price_plan, Invoice
# from .models import User

admin.site.register(Lesson)
admin.site.register(User)
admin.site.register(Attend)
admin.site.register(Price_plan)
admin.site.register(Invoice)
