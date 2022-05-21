from django.contrib import admin

# Register your models here.

from .models import ProjectModel,  LearntModel, StyleModel, SkillsModel, SEO


admin.site.register(ProjectModel)
admin.site.register(LearntModel)
admin.site.register(StyleModel)
admin.site.register(SkillsModel)
admin.site.register(SEO)