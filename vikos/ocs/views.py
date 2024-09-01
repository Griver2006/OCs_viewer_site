from django.views.generic import ListView


class HomePage(ListView):
    template_name = 'ocs/home.html'

    def get_queryset(self):
        pass
