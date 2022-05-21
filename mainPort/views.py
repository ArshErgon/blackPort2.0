from django.shortcuts import render

# Create your views here.

from .models import ProjectModel, LearntModel, StyleModel, SkillsModel, SEO


def homeView(request):
    project, about, learn, skills = '', '', '', ''
    projects = ProjectModel.objects.all()
    learns = LearntModel.objects.all()
    for project in projects:
        pass
    
    for learn in learns:
        pass
    for skills in SkillsModel.objects.all():
        pass


    return render(request, 'index.html', {'project':project, 'learn':learn, 'styleShow':StyleModel.objects.all(), 'skills':skills, 'seoField':SEO.objects.all()})


