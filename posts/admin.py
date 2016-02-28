from django.contrib import admin
from .models import Section , Post , tags 

class InlineTags(admin.StackedInline):
    extra = 3
    model = tags

class CustomPost(admin.ModelAdmin):
    post_tag = ['title']
    inlines = [InlineTags]




admin.site.register(Section)
admin.site.register(Post,CustomPost)
admin.site.register(tags)


