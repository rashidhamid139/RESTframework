from django.contrib import admin
from .models import User, UserParent, Article, Category, Hero
# Register your models here.
admin.site.register(User)
admin.site.register(UserParent)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Hero)