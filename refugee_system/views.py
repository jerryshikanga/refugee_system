from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from refugee.models import Refugee
from distribution.models import Distribution
import math


@login_required
def index(request):
    successful_distributions = Distribution.objects.filter(status=True).count()
    refugee_latest = Refugee.objects.all()[:10]
    total_distributions = Distribution.objects.all().count()
    distribution_rate = 0
    if total_distributions != 0 :
        distribution_rate = successful_distributions/total_distributions
    context = {
        "successful_distributions": successful_distributions,
        "refugee_latest": refugee_latest,
        "distribution_rate": math.ceil(distribution_rate*100),
    }
    return render(request, 'index.html', context)