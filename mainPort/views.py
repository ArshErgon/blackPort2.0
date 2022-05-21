from django.shortcuts import render

# Create your views here.

from .models import ProjectModel, AboutMeModel, LearntModel, StyleModel, SkillsModel, SEO, newHome


def homeView(request):
    project, about, learn, skills = '', '', '', ''
    projects = ProjectModel.objects.all()
    aboutinfos = AboutMeModel.objects.all()
    learns = LearntModel.objects.all()
    for project in projects:
        pass
    for about in aboutinfos:
        pass
    for learn in learns:
        pass
    for skills in SkillsModel.objects.all():
        pass


    return render(request, 'index.html', {'project':project, 'about':about, 'learn':learn, 'styleShow':StyleModel.objects.all(), 'skills':skills, 'seoField':SEO.objects.all()})


def newHome(request):
    return render(request, 'newHome.html', {'newhome':newHome.objects.all()})