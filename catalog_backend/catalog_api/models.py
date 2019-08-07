from django.db import models


class CarMake(models.Model):
    make_name = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return make_name


class CarModel(models.Model):
    model_name = models.CharField(max_length=30, unique=True, null=False)
    associated_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return model_name


class CarPart(models.Model):
    # Part name might need to be in a foreign table
    part_name = models.CharField(max_length=50, null=False)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    date_added = models.DateField()

    def __str__(self):
        return self.part_name
