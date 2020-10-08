from django.db import models


class Part(models.Model):
    part_name = models.CharField(max_length=50)
    part_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_name
