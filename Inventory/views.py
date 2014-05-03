from django.views import generic
from .models import GPS
# This is the view for my home page. It is a list view because it needs to display a list of all
# of the GPS units that are currently in the database.
class HomeView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/home.html'
    context_object_name = 'unit'

# This is the view for my add item page.
class Add_ItemView(generic.TemplateView):
    model = GPS
    template_name = 'inv_templates/add_item.html'

# This is the view for my remove item page. It is a list view because it needs to display a
# list of all of the GPS units that are currently in the database.
class Remove_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/remove_item.html'
    context_object_name = 'unit'

# This is the view for my update item page. It is a list view because it needs to display a
# list of all of the GPS units that are currently in the database.
class Update_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/update_item.html'
    context_object_name = 'unit'

# This is the view for my check out item page. It is a list view because it needs to display a
# list of all of the GPS units that are currently checked in.
class Check_Out_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/check_out_item.html'
    context_object_name = 'checkedin_units'
    queryset = GPS.objects.filter(status=False)

# This is the view for my check in item page. It is a list view because it needs to display a
# list of all of the GPS units that are currently checked out.
class Check_In_ItemView(generic.ListView):
    model = GPS
    template_name = 'inv_templates/check_in_item.html'
    context_object_name = 'checkedout_units'
    queryset = GPS.objects.filter(status=True)
