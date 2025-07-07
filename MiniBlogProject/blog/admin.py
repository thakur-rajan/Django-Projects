from django.contrib import admin
from .models import postModel
# Register your models here.
@admin.register(postModel)
class PostAdmin(admin.ModelAdmin):
    list_display=['title']