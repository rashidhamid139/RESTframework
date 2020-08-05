from django.db import models

# Create your models here.


class InputImage(models.Model):
    comparison_set_name = models.CharField(max_length=100)
    input_image = models.ImageField(upload_to='/path/InputImages/', max_length=254, blank=True, null=True)
    standard_image = models.ImageField(upload_to='/path/StandardImages/', max_length=254, blank=True, null=True)

    def __str__(self):
        return self.comparison_set_name