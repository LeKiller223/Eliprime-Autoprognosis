from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make.name} - {self.name}"


class CarScanner(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(default="strange noise")
    diagnostic_result = models.TextField()
    suggested_actions = models.TextField()

    def __str__(self):
        return f"{self.car} - {self.report_date}"
