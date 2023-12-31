from django.urls import path
from . import views


urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('articulo/<slug:articulo_slug>/',
         views.ArticuloDetailView.as_view(), name='articulo'),

    path('categoria/<slug:categoria_slug>/',
         views.ArticulosByCategoriaView.as_view(), name='categoria'),

    path('autor/<str:autor>/', views.ArticulosByAutorView.as_view(), name='autor'),

    path('archivo/<int:year>/<int:month>',
         views.ArticulosByArchivoView.as_view(), name='archivo'),

    path('crear_articulo/', views.ArticuloCreateView.as_view(),
         name='crear_articulo'),

    path('actualizar_articulo/<slug:articulo_slug>',
         views.ArticuloUpdateView.as_view(), name='actualizar_articulo'),

    path('eliminar_articulo/<slug:articulo_slug>',
         views.ArticuloDeleteView.as_view(), name='eliminar_articulo'),

    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('confirmacion/<str:code>/<str:user>/',
         views.ConfirmationView.as_view(), name='confirmacion'),

    path('editar_comentario/<int:comment_id>/', 
         views.editar_comentario, name='editar_comentario'),

    path('eliminar_comentario/<int:comment_id>/', 
         views.eliminar_comentario, name='eliminar_comentario'),

    path('editar_categoria_imagen/<slug:articulo_slug>/', 
         views.editar_categoria_imagen, name='editar_categoria_imagen'),               
]
