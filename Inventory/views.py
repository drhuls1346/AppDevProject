from django.views import generic


# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'inv_templates/home.html'
