from django.db import models
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from category.models import Category

class Attraction(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    city        = models.CharField(max_length=50)
    rate        = models.PositiveIntegerField()
    price       = models.PositiveIntegerField()
    category    = models.OneToOneField(Category, on_delete=models.CASCADE)
    
    latitude    = models.IntegerField()
    longitude   = models.IntegerField()

    start_h     = models.TimeField()
    end_h       = models.TimeField()

    

    def __str__(self):
        return self.name

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type