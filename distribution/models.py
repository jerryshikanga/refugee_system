from django.db import models
from refugee.models import Refugee
from food.models import Food
from django.utils import timezone


class Distribution(models.Model):
    refugee = models.ForeignKey(Refugee, on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    allocation_time = models.DateTimeField(default=timezone.now)
    picking_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Distribution"
        verbose_name_plural = "Distributions"
        permissions = (
            ("can_allocate_distribution", "Can allocate distribution"),
            ("can_clear_distribution", "Can clear distribution")
        )
        ordering = ("allocation_time", "picking_time")

    def __str__(self):
        if self.status:
            status_verbose = "Picked"
        else:
            status_verbose = "Unpicked"

        return "%s distribution to %s of %d %s" % (status_verbose, self.refugee.name, self.quantity, self.food.name)
