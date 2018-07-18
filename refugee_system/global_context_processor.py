from account.models import Account
from distribution.models import Distribution
from food.models import Food
from refugee.models import Refugee

def get_context(request):
    context = dict()
    context['site_title'] = "Site Name"
    context["site_title_long"] = " Site Name Long"
    context["site_author"] = "Jerry Shikanga"
    context["site_description"] = "Site description"

    context['num_foods'] = Food.objects.count()
    context['num_agents'] = Account.objects.count()
    context['num_distribution'] = Distribution.objects.count()
    context['num_refugees'] = Refugee.objects.count()
    return context