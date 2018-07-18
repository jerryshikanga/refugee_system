from django.db import models
from django.urls import reverse_lazy
from refugee_system.ModelMixins import ModelMixin


# Create your models here.
class DistributionUnit(ModelMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="Unit Name")
    abbreviation = models.CharField(max_length=5, verbose_name="Abbreviation")
    description = models.TextField(verbose_name="Unit Description")

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Distribution Unit"
        verbose_name_plural = "Distribution Units"
        ordering = ("name",)
        permissions = (
            ("custom_can_add_food_unit", "Custom Can add Food Unit"),
            ("custom_can_delete_food_unit", "Custom Can delete Food Unit"),
            ("custom_can_update_food_unit", "Custom can update Food Unit")
        )

    def get_absolute_url(self):
        return reverse_lazy('food:unit_detail', kwargs={"pk":self.pk})


class Food(ModelMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="Food Name")
    description = models.TextField(verbose_name="Food Description or Remarks")
    unit = models.ForeignKey(DistributionUnit, on_delete=models.SET_NULL, null=True, verbose_name="Distribution Units")
    quantity = models.IntegerField(verbose_name="Quantity_available", default=0)

    def get_absolute_url(self):
        return reverse_lazy("food:detail" , kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Food"
        verbose_name_plural = "Food"
        ordering = ("name",)
        permissions = (
            ("custom_can_add_food", "Custom Can add Food"),
            ("custom_can_delete_food", "Custom Can delete Food"),
            ("custom_can_update_food", "Custom can update Food")
        )
