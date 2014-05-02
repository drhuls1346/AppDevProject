from django.views import generic
from .models import GPS

# Create your views here.

class HomeView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/home.html'
    context_object_name = 'unit'

class Add_ItemView(generic.TemplateView):
    model = GPS
    template_name = 'inv_templates/add_item.html'

class Remove_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/remove_item.html'
    context_object_name = 'unit'

class Update_ItemView(generic.TemplateView):
    model = GPS
    template_name = 'inv_templates/update_item.html'

class Check_Out_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/check_out_item.html'
    context_object_name = 'checkedin_units'
    queryset = GPS.objects.filter(status=False)

class Check_In_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/check_in_item.html'
    context_object_name = 'checkedout_units'
    queryset = GPS.objects.filter(status=True)
