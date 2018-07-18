from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Refugee
from django.contrib.auth.mixins import LoginRequiredMixin
from refugee_system.utils import render_template_to_pdf


# Create your views here.
class CreateRefugee(LoginRequiredMixin, CreateView):
    model = Refugee
    template_name = "refugee/refugee_create_form.html"
    fields = ("name", "date_of_birth", "gender", "telephone", "address")


class RefugeeList(ListView):
    model = Refugee
    template_name = "refugee/refugee_list.html"


class RefugeeDetail(DetailView):
    model = Refugee
    template_name = "refugee/refugee_detail.html"


class UpdateRefugee(LoginRequiredMixin, UpdateView):
    model = Refugee
    fields = ("name", "date_of_birth", "gender", "telephone", "address")
    template_name = "refugee/refugee_update_form.html"


class DeleteRefugee(LoginRequiredMixin,DeleteView):
    model = Refugee
    success_url = reverse_lazy('refugee:success_delete')


@login_required
def success_delete_refugee(request):
    return render(request, 'refugee/success_delete_refugee.html')


def refugee_list_pdf(request, *args, **kwargs):
    context = {
        "refugee_list": Refugee.objects.all(),
    }
    pdf = render_template_to_pdf('refugee/refugee_list_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')