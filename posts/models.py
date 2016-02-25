from __future__ import unicode_literals

from django.db import models
from datetime import  datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Section(models.Model):
    section_name=models.CharField(max_length=100)

class Post (models.Model):
    title=models.CharField(max_length=200)
    content= RichTextField()
    date=models.DateTimeField(default=datetime.now)
    img_path=models.CharField(max_length=200)
    section_name=models.ForeignKey(Section)

class tags(models.Model):
    tag_name=models.CharField(max_length=50)
    post_id=models.ForeignKey(Post)
    
