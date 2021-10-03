from django.contrib import admin

# Register your models here.
from web.models import Curriculo, Skill, Education, Experience, Portifolio, Mensagem

admin.site.register(Curriculo)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Portifolio)
admin.site.register(Mensagem)