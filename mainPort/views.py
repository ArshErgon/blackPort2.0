from django.shortcuts import render

# Create your views here.

from .models import ProjectModel, AboutMeModel, LearntModel, StyleModel


def homeView(request):
    project, about, learn = '', '', ''
    projects = ProjectModel.objects.all()
    aboutinfos = AboutMeModel.objects.all()
    learns = LearntModel.objects.all()
    for project in projects:
        pass
    for about in aboutinfos:
        pass
    for learn in learns:
        pass

    return render(request, 'index.html', {'project':project, 'about':about, 'learn':learn, 'styleShow':StyleModel.objects.all()})