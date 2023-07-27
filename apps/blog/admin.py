from django.contrib import admin
from . import models

admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'


########################
#### Perfil Usuario ####
########################

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'user_group')
    search_fields = ('user__name', 'user__groups__name')
    list_filter = ('user__groups',)

    def user_group(self, obj):
        return '-'.join([grupo.name for grupo in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'


admin.site.register(models.Perfil, PerfilAdmin)


################
#### Acerca ####
################


class AcercaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('descripcion', 'creacion')


admin.site.register(models.Acerca, AcercaAdmin)


########################
#### Redes Sociales ####
########################

class RedAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'url', 'icono')


admin.site.register(models.Red, RedAdmin)


###################
#### Categoría ####
###################

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
    prepopulated_fields = {'slug': ('nombre', )}


admin.site.register(models.Categoria, CategoriaAdmin)


##################
#### Etiqueta ####
##################

class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')


admin.site.register(models.Etiqueta, EtiquetaAdmin)


##################
#### Articulo ####
##################

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('titulo', 'categoria', 'publicado',
                    'autor', 'creacion', 'articuloEtiquetas')
    prepopulated_fields = {'slug': ('titulo', )}
    ordering = ('autor', '-creacion')
    search_fields = ('titulo', 'contenido',
                     'autor__username', 'categoria__nombre')
    list_filter = ('autor', 'categoria', 'etiquetas')

    def articuloEtiquetas(self, obj):
        return ' - '.join([etiqueta.nombre for etiqueta in obj.etiquetas.all().order_by('nombre')])

    articuloEtiquetas.short_description = 'Etiquetas'


admin.site.register(models.Articulo, ArticuloAdmin)
