from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Hood,User,Business,Post,Health,Police
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import HoodForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    business = Business.get_all()
    hood = Hood.get_all()
    post = Post.get_all()
    return render(request,'index.html',{'business':business,'hood':hood, 'post':post})

def hoodhood(request,hood_id):
    hood = Hood.get_all()

    return render(request,'hoodhood.html',{'hood':hood})

# @login_required(login_url='/accounts/login/')
# def hoodpost(request):
#     post = Post.get_all()
#     return render(request,'hoodpost.html',{'post':post})

# @login_required(login_url='/accounts/login/')
# def hoodbusiness(request):
#     business = Business.get_all()
#     return render(request,'business.html',{'business':business})

# @login_required(login_url='/accounts/login/')
# def hood(request):
#     hood = Hood.get_all()
#     return render(request,'hood.html',{'hood':hood,})

# @login_required(login_url='/accounts/login/')
# def hoodhealth(request):
#     health = Health.get_all()
#     return render(request,'health.html',{'health':health,})

# @login_required(login_url='/accounts/login/')
# def hoodpolice(request):
#     police = Police.get_all()
#     return render(request,'police.html',{'police':police,})

# def post(request,post_id):
#     try:
#         post = Post.objects.get(id = post_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"post.html", {"post":post})

# @login_required(login_url='/accounts/login/')
# def new_post(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.writter = current_user
#             post.save()
#         return redirect('indexPage')

#     else:
#         form = PostForm()
#     return render(request, 'new_post.html', {"form": form})

# def new_business(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = BusinessForm(request.POST, request.FILES)
#         if form.is_valid():
#             business = form.save(commit=False)
#             business.save()
#         return redirect('indexPage')

#     else:
#         form = BusinessForm()
#     return render(request, 'new_business.html', {"form": form})

# @login_required(login_url='/accounts/login/')
# def new_health(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = HealthForm(request.POST, request.FILES)
#         if form.is_valid():
#             health = form.save(commit=False)
#             health.user = current_user
#             health.save()
#         return redirect('indexPage')

#     else:
#         form = HealthForm()
#     return render(request, 'new_health.html', {"form": form})

# def profile(request):
#     current_user = request.user
#     profile = User.objects.filter(user=current_user)
    
#     if len(profile)<1:
#         profile = "No profile"
#     else:
#         profile = User.objects.filter(user=current_user)

#     return render(request, 'profile.html',{'profile':profile})


#     #
#     # try:
#     #     profile = Profile.objects.get(profile = current_user)
#     # except ObjectDoesNotExist:
#     #     return redirect('create-profile')

# def edit_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.user = current_user
#             profile.save()
#         return redirect('Profile')
#     else:
#         form = ProfileForm()
#     return render(request,'edit_profile.html',{'form':form})

# def search_results(request):

#     if 'project' in request.GET and request.GET["project"]:
#         search_term = request.GET.get("project")
#         searched_projects = Project.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"projects": searched_projects})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})

# def hood(request,neighborhood_id):
#     try:
#         hood = Hood.objects.get(id = hood_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"hood.html", {"hood":hood})

# def search(request):

#     if 'business' in request.GET and request.GET["business"]:
#         search_term = request.GET.get("business")
#         searched_business = Business.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"business": searched_business})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})

# def search_details(request,business_id):
#     try :
#         business = Business.objects.get(id = business_id)

#     except ObjectDoesNotExist:
#         raise Http404()

#     return render(request, 'search_details.html', {'business':business})