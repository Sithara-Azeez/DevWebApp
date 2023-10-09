from .models import Project
from django.db.models import Q
from .models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

'''def searchProject(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('seach_query')

    project_list = Project.objects.filter(title__icontains=search_query)
    return project_list, search_query'''

def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags_list = Tag.objects.filter(name__icontains=search_query)

    

    project_list = Project.objects.filter(Q(title__icontains=search_query) | 
                                          Q(owner__username__icontains=search_query) |
                                          Q(tags__in=tags_list)).distinct()

    return project_list,search_query

def paginateProjects(request,project_list,project_per_page):

    paginator = Paginator(project_list,project_per_page)

    page = request.GET.get('page')
    #page = ''

    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        project_list = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        project_list = paginator.page(page)

    leftIndex = int(page)-4
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page)+4
    if rightIndex >= paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)
    print('page=',page)
    return project_list,custom_range,paginator,page
