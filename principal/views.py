from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Publicidad

class PublicidadCreateView(CreateView):
	model= Publicidad
	template_name="libro_form.html"
