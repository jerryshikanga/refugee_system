from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from refugee.models import Refugee
from distribution.models import Distribution
import math


@login_required
def index(request):
    context = {
        "successful_distributions": Distribution.objects.filter(status=True).count(),
        "refugee_latest": Refugee.objects.all()[:10],
        "distribution_rate": math.ceil(Distribution.objects.filter(status=True).count()/Distribution.objects.all().count()*100),
    }
    return render(request, 'index.html', context)