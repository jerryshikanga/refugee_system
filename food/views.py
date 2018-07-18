from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Food, DistributionUnit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import IncreaseReservesForm


# Create your views here.
class CreateFood(LoginRequiredMixin, CreateView):
    model = Food
    template_name = "food/food_create_form.html"
    fields = ("name", "description", "unit")


class FoodList(ListView):
    model = Food
    template_name = 'food/food_list.html'


class FoodDetail(DetailView):
    model = Food
    template_name = 'food/food_detail.html'


class UpdateFood(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = 'food/update_food_form.html'


class DeleteFood(LoginRequiredMixin,DeleteView):
    model = Food
    success_url = reverse_lazy("food:success_delete")


@login_required
def success_delete_food(request):
    return render(request, 'food/success_delete_food.html')


class IncreaseReserves(View):
    def get(self, *args, **kwargs):
        form = IncreaseReservesForm()
        food = get_object_or_404(Food, id=self.kwargs.get("food_id"))
        context = {"food":food, "form":form}
        return render(self.request, "food/increase_reserves_form.html", context)

    def post(self, *args, **kwargs):
        form = IncreaseReservesForm(data=self.request.POST)
        food = get_object_or_404(Food, id=self.kwargs.get("food_id"))
        if form.is_valid():
            form.increase_reserves(food)
            return redirect(reverse_lazy("food:success_increase_reserve", kwargs={"food_id": food.id}))
        else:
            context = {"food": food, "form": form}
            return render(self.request, "food/increase_reserves_form.html", context)


@login_required
def success_increase_reserves(request, *args, **kwargs):
    food = get_object_or_404(Food, id=kwargs["food_id"])
    context = {
        "food": food
    }
    return render(request, "food/success_increase_reserves.html", context)


class CreateDistributionUnit(CreateView):
    model = DistributionUnit
    template_name = 'distribution_unit/create_form.html'
    fields = ("name", "abbreviation", "description")


class UpdateDistributionUnit(UpdateView) :
    model = DistributionUnit
    template_name = 'distribution_unit/update_form.html'
    fields = ("name", "abbreviation", "description")


class DeleteDistributionUnit(DeleteView) :
    model = DistributionUnit
    success_url = reverse_lazy('food:success_delete_unit')


@login_required
def success_delete_food_unit(request):
    return render(request, 'food/success_delete_food.html')


class DistributionUnitList(ListView) :
    model = DistributionUnit
    template_name = 'distribution_unit/list.html'


class DistributionUnitDetail(DetailView) :
    model = DistributionUnit
    template_name = 'distribution_unit/detail.html'
