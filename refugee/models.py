from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from refugee_system.ModelMixins import ModelMixin


# Create your models here.
class Gender(ModelMixin, models.Model):
    name = models.CharField(max_length=10, verbose_name="Gender Name")

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Gender"
        verbose_name_plural = "Gender"
        ordering = ("name",)
        permissions = (
            ("custom_can_add_gender", "Custom Can add Gender"),
            ("custom_can_update_gender", "Custom Can update Gender"),
            ("custom_can_delete_gender", "Custom Can delete Gender")
        )


class Refugee(ModelMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name="Refugee Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, verbose_name="Gender")
    telephone = models.BigIntegerField(verbose_name="Telephone Number")
    address = models.TextField(verbose_name="Physical Address")
    date_time_registered = models.DateTimeField(default=timezone.now, verbose_name="Time of Registration")

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Refugee"
        verbose_name_plural = "Refugees"
        ordering = ("date_time_registered", "name")
        permissions = (
            ("custom_can_add_refugee", "Custom Can add Refugee"),
            ("custom_can_update_refugee", "Custom Can update Refugee"),
            ("custom_can_delete_refugee", "Custom Can delete Refugee")
        )

    def get_absolute_url(self):
        return reverse_lazy("refugee:detail", kwargs={"pk":self.pk})
