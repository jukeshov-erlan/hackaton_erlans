from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(Bookmark)