from django.contrib import admin
from .models import(
    Cliente, Funcionario,
    MarcaRoupa, TipoRoupa,
    Roupa, Valor,
    Sessao  
)

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(MarcaRoupa)
admin.site.register(TipoRoupa)
admin.site.register(Roupa)
admin.site.register(Valor)
admin.site.register(Sessao)
