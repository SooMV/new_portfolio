from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from Main.forms import  PDFUploadForm
from Main.models import MyCV, Project
from new_portfolio import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# Choix de langues
def change_language(request, lang_code):
    response = redirect('index')  
    print('La langue est :',lang_code)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 
                        lang_code, 
                        max_age=60*60, 
                        httponly=True,
                        samesite='Lax'
                        )
    return response

# Choix du thème
def change_theme(request, ** kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def ios_detail(request, id):
    project = get_object_or_404(Project, id=id, type='ios')
    context = {
        'project' : project
    }
    
    return render(request,'main/ios_detail.html' ,context)


def download_my_cv(request):
    cv = get_object_or_404(MyCV)  # Récupérez le CV depuis la base de données
    response = HttpResponse(cv.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.title}"'  
    return response
        

def android_detail(request, id):
    project = get_object_or_404(Project, id=id, type='android')
    context = {
        'project' : project
    }
    
    return render(request,'main/android_detail.html' ,context)

def python_detail(request, id):
    project = get_object_or_404(Project, id=id, type='python')
    context = {
        'project' : project
    }
    
    return render(request,'main/python_detail.html' ,context)
    
def paginate_projects(request, projects, per_page=3):
    paginator = Paginator(projects, per_page)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

 
def all_ios_projects(request):
    projects = Project.objects.filter(type='ios')
    page_obj = paginate_projects(request, projects)
    context = {
        'projects': page_obj
    }
    return render(request, 'main/ios_project.html', context)

def all_android_projects(request):
    projects = Project.objects.filter(type='android')
    page_obj = paginate_projects(request, projects)
    context = {
        'projects': page_obj
    }
    return render(request, 'main/android_project.html', context)

def all_python_projects(request):
    projects = Project.objects.filter(type='python')
    page_obj = paginate_projects(request, projects)
    context = {
        'projects': page_obj
    }
    return render(request, 'main/python_project.html', context)

def my_profile(request):
    return render(request, 'main/my_profile.html')


def my_cv(request):
    return render(request, 'main/my_cv.html')


def language_learn(request):
    return render(request, 'main/language_learn.html')