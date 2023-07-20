from django.contrib import admin
from .models import * # para cargar en el panel de adm.

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#Configurar el titulo del panel adm

admin.site.site_header="Master en Python" #Cambiar nombre del panelAdm
admin.site.site_title="Master en Python Sub"
admin.site.index_title="Panel de Gestion"
