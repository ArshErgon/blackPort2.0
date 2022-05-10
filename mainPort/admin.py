from django.contrib import admin

# Register your models here.

from .models import ProjectModel, AboutMeModel, LearntModel, StyleModel, SkillsModel


admin.site.register(ProjectModel)
admin.site.register(AboutMeModel)
admin.site.register(LearntModel)
admin.site.register(StyleModel)
admin.site.register(SkillsModel)