from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import *
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProjects, paginateProjects

# Create your views here.

projectList = [
    {
        'id' : '1',
        'title' : 'Ecommerce Website',
        'description' : 'Fully functional ecommerce website'},
    {
         'id' : '2',
        'title' : 'Portfolio Website',
        'description' : 'A personal website to write articles and display work'
    },
    {
        'id' : '3',
        'title' : 'Social Network',
        'description' : 'An open source project built by the community'
    }
]

'''def projects(request):
    project_list, search_query = searchProject(request)
    #project_list = Project.objects.all()
    context = {
                'projects': project_list,
                'search_query': search_query,
    }
    return render(request, 'projs/projects.html', context)'''

def projects(request):
    project_list, search_query = searchProjects(request)
   #project_list = Project.objects.all()  
    project_list, custom_range, paginator, page = paginateProjects(
        request,project_list,3)

    context = {'projects': project_list,
               'search_query': search_query,
               'custom_range': custom_range,
               'paginator' : paginator,
               'page' : page,
    }
    return render(request,'projs/projects.html',context)

def project(request, pk):
    proj = None
    proj = Project.objects.get(id=pk)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.project = proj
            review.owner = request.user.profile
            review.save()
            proj.getVoteCount


            messages.success(request,'Comment added successfully')
            return redirect('project:project',pk=proj.id)
        else:
            messages.error(request,'Some error occured')

       
    
    context = {
                'proj':proj,
                'review_form':review_form,
               }
    
    return render(request, 'projs/single-project.html', context)
    


def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request,'Project created successfully')
            return redirect('users:account')
        else:
            messages.error(request,'Some error occured')
    context = {'form':form}
    return render(request, 'projs/create-project.html', context)

@login_required(login_url= 'users:login')
def updateProject(request, pk):
    profile = request.user.profile
    proj = Project.objects.get(id=pk)
    proj_form = ProjectForm(instance=proj)
    if request.method == 'POST':
        proj_form = ProjectForm(request.POST, request.FILES, instance=proj)
        if proj_form.is_valid():
            project = proj_form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request,'Project updated Successfully')
            return redirect('users:account')
        else:
            messages.error(request,'Some error occured')
    context = {
        'project_form':proj_form,
    }
    return render(request, 'projs/update-project.html', context)

@login_required(login_url= 'users:login')
def deleteProject(request, pk):
    profile = request.user.profile
    proj = profile.project_set.get(id=pk)
    if request.method == 'POST':
        proj.delete()
        messages.success(request,'Project deleted Successfully')
        return redirect('users:account')
    
    context = {
            'object':proj,
    }
    return render(request, 'projs/delete-project.html', context)