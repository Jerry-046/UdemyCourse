from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def product(request):
    projects = Project.objects.all()
    params ={'projects' : projects}
    return render(request,'projects/single-project.html', params)

    

def products(request,pk):
        projectObj = Project.objects.get(id=pk)
        tags = projectObj.tags.all()
        return render(request,'projects/projects.html',{'a':projectObj,'tags':tags})

def index(request):
    return render(request,'projects/home.html')

def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product")
        
    context ={'form' : form}
    return render(request,'projects/pform.html',context)


def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("product")    
    context ={'form' : form}
    return render(request,'projects/pform.html',context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('product')    
    context={'obj':project}
    return render(request,'projects/delete_object.html',context)