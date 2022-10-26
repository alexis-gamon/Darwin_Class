
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Curso, Comentario, Lenguaje
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin##obliga a que estes logeado para poder visualizar una vista
from django.core.exceptions import PermissionDenied##valida los permisos
from django.http import HttpResponse

class CursoListView(ListView):
    model = Curso
    template_name = 'lista_curso.html'
    context_object_name = 'lista_curso'

 

# Create your views here.
class CursoTemplateView(LoginRequiredMixin, ListView):
    template_name = 'curso.html'
    model = Curso
    context_object_name = 'Todos_curso'

   # success_url = reverse_lazy('lista_curso')

class homeTemplateView(TemplateView):
    template_name = 'home.html'



class CursoPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'curso_detalle.html'
    model = Curso
    context_object_name = 'Curso'

class CursoPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'curso_detalle.html'
    model = Curso
    context_object_name = 'Curso'
    
    login_url = 'login'

   

class CursoPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'curso_nuevo.html'
    model = Curso
    #se tiene que agregar todos los campos execpto los que se asignan en automatico 
    fields = ('Nombre', 'Descripcion','AñosExperiencia','Lenguaje', 'Horas')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponse('<h1> Sin acceso </h1>')


    def form_valid(self, form):
        form.instance.Creador = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    login_url = 'login'

class CursoPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'curso_editar.html'
    model = Curso
    fields = ('Nombre', 'Descripcion')

    success_url = reverse_lazy('lista_curso')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CursoPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'curso_eliminar.html'
    model = Curso
    success_url = reverse_lazy('lista_curso')

    login_url = 'login'

class ComentariosCreateView(LoginRequiredMixin,CreateView):
    template_name = 'agregar_comentario.html'
    model = Comentario
    fields = ('comentario',)
    success_url = reverse_lazy('lista_curso')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.Curso_id = self.kwargs['pk']
        return super().form_valid(form)
        ##obligas a la persona que este logeada

