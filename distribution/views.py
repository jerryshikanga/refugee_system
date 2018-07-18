from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from food.models import Food
from django.views.generic import ListView
from refugee.models import Refugee
from .models import Distribution
from refugee_system.utils import render_template_to_pdf
import math


# Create your views here.
def allocate_distribution(request, *args, **kwargs):
    food = get_object_or_404(Food, id=kwargs.get("food_id"))
    quantity_rem = food.quantity
    quantity_dist_ttl = 0.75 * quantity_rem
    refugees = Refugee.objects.all()
    quantity_per_refugee = math.floor(quantity_dist_ttl / refugees.count())
    if quantity_per_refugee <= 0:
        context = {
            "food": food,
            "quantity_rem": quantity_rem,
            "refugees_count": refugees.count()
        }
        return render(request=request, template_name='distribution/distribution_allocation_failed_insufficient.html',
                      context=context)
    else:
        [Distribution.objects.create(refugee=refugee, quantity=quantity_per_refugee, food=food).save() for refugee in
         refugees]
        context = {
            "food": food,
            "quantity_per_refugee": quantity_per_refugee,
            "num_refugees": refugees.count()
        }
        return render(request=request, template_name='distribution/distribution_allocation_success.html',
                      context=context)


class DistributionList(ListView):
    model = Distribution
    queryset = Distribution.objects.filter(status=False)
    template_name = 'distribution/distribution_list.html'


def clear_distribution(request, *args, **kwargs):
    distribution = Distribution.objects.get(id=kwargs["distribution_id"])
    distribution.status = True
    distribution.picking_time = timezone.now()
    distribution.save()
    food = distribution.food
    food.quantity -= distribution.quantity
    food.save()
    context = {
        "distribution":distribution,
    }
    return render(request, 'distribution/distribution_cleared_successfully.html', context)


def cleared_distribution_pdf(request, *args, **kwargs):
    distribution = Distribution.objects.get(id=kwargs["distribution_id"])
    context = {
        "distribution": distribution,
    }
    pdf = render_template_to_pdf('distribution/distribution_clearance_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
