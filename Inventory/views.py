from django.views import generic
from .models import GPS

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'inv_templates/home.html'