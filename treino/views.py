from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from treino.forms import TreinoForm
from treino.models import Treino

class Home(TemplateView):
    template_name = 'index.html'

class Listar(ListView):
    template_name = 'listar_treino.html'
    model = Treino
    context_object_name = 'treinos'

class Cadastro(CreateView):
    template_name = 'cadastro_treino.html'
    model = Treino
    form_class = TreinoForm
    success_url = '/'

    def form_valid(self, form):
        treino = form.save(commit=True)
        return super().form_valid(form)
    
class Editar(UpdateView):
    template_name = 'editar.html'
    model = Treino
    form_class = TreinoForm
    success_url = '/listar'
    
    def form_valid(self, form):
        treino = form.save(commit=True)
        return super().form_valid(form)
    
def delete(request, pk):
    treino = Treino.objects.get(pk=pk)
    treino.delete()
    return redirect('treino:listar')
