# File encoding: utf-8

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from models import Bug, Company, Project, Tester
from forms import BugForm


def bugs_list(request):
    bugs = Bug.objects.all()
    return render_to_response('buglist.html', {'bugs': bugs})


def add_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bugs/')
    else:
        form = BugForm()
    return render_to_response('addbug.html',{'form': form})

       
# авторизация
def login(request):
    return render_to_response('login.html')


def logout(request):
    return render_to_response('logout.html')


# компании
def company_registraion(request):
    return render_to_response('company_registraion.html')


def company_detail(request, pk):
    try:
	company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
	raise Http404
    projects = company.projects.all()
    return render_to_response('company_detail.html', locals())

       
# тестеры
def tester_registraion(request):
    return render_to_response('tester_registraion.html')


def tester_detail(request, pk):
    try:
        tester = Tester.objects.get(pk=pk)
    except Tester.DoesNotExist:
        raise Http404
    projects = tester.projects.all()
    return render_to_response('tester_detail.html', locals())


# проекты
def new_project(request):
    return render_to_response('new_project.html')


def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404
    testers = project.testers.all()
    bugs = project.bugs.all()
    return render_to_response('project_detail.html', locals())


