from django.db import models
import uuid


class Make(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex[:8], editable=False
    )
    make_name = models.CharField(max_length=50)

    def __str__(self):
        return self.make_name


class Model(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex[:8], editable=False
    )
    model_name = models.CharField(max_length=50)
    make_name = models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Part(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex[:8], editable=False
    )
    part_name = models.CharField(max_length=50)
    part_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=50, default="N/A")

    def __str__(self):
        return self.part_name
