from django.contrib import admin

# Register your models here.
from .models import Flags, User, Submissions, Clue

admin.site.register(Flags)
admin.site.register(User)
admin.site.register(Submissions)
admin.site.register(Clue)