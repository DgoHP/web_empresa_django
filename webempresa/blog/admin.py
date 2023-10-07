from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #se utiliza para personalizar los campos en el panel de administrador y mostrar los que nosotros queramos del model en cuestion
    list_display = ('title', 'author', 'published', 'created', 'post_categories')

    #se utiliza para ordenar la lista por el campo y subcampo que se señala 
    # en este caso, por autor y cada publicacion de ese autor se ordena por fecha de publicacion
    ordering = ('author', 'published')

    #se utiliza para agregar una barra de busqueda y se señala en el campo que queremos que haga la busqueda(pueden ser varios campos de busqueda)
    #cuando son campos heredados de otros modelos o llaves foraneas se utiliza __nombrecampo de donde se obtiene dicho valor
    # en este caso __username del modelo de user que tiene por defecto django
    search_fields= ('title','author__username', 'categories__name')
    #se utiliza para ordenar los registros por fecha segun el campo que se defina, en este caso fecha de publicacion
    date_hierarchy = 'published'

    #se utiliza para desplegar una lista de filtro por el campo señalado, en este caso por el campo autor
    #es una forma más rapida de seleccionar y aplicar un filtro por algun campo en comun en la lista
    list_filter = ('author__username',)

    #Funcion para desplegar un campo el cual sea una relacion de uno a muchos 
    #para mostrar en este caso todas las categorias a las cuales pertenece cada publicacion
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description="Categorias"    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)