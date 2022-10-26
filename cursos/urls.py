from django.urls import path, include

from .views import CursoListView, CursoTemplateView, CursoPageDetail, CursoPagesCreate, CursoPageUpdate, CursoPageDelete, ComentariosCreateView

urlpatterns = [

    path('Curso/',CursoTemplateView.as_view(), name='Curso'),
    path('', CursoListView.as_view(), name='lista_curso'),
### Detalle
    path('<int:pk>/', CursoPageDetail.as_view(), name='curso_detalle'),
### Crear
    path('nuevo/', CursoPagesCreate.as_view(), name="curso_nuevo"),
### Modificar
    path('<int:pk>/editar/', CursoPageUpdate.as_view(), name="curso_editar"),
### Borrar 
    path('<int:pk>/eliminar/', CursoPageDelete.as_view(), name="curso_eliminar"),

    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),


]