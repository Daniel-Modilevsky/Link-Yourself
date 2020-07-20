from django.utils import timezone
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import path
from .forms import LinkForm
from .forms import ProfileForm
from .models import LinkDB, CATALOG_CHOICES
from .models import Profile
from django.contrib.messages import context_processors

from django.http import HttpResponse
from django.forms import ModelForm


def homepage(request):
    return render(request, 'link/index.html')


def registerProfile2(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        profile_form = ProfileForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user.save()
                temp_profile = profile_form.save(commit=False)
                temp_profile.user = user
                temp_profile.save()
                login(request, user)
                return redirect('home', request.user.id)

            except IntegrityError:
                return render(request, 'link/registerProfile.html', {'form': UserCreationForm(), 'profile_form': profile_form,
                                                                     "errMsg": "User exists. Choose a different one"})
        else:
            profile_form = ProfileForm(request.POST)
            return render(request, 'link/registerProfile.html', {'form': UserCreationForm(), 'profile_form': profile_form,
                                                                "errMsg": "Password didn't match"})
    else:
        return render(request, 'link/registerProfile.html', {'form': UserCreationForm(), 'profile_form':ProfileForm(request.POST)})


def login1(request):
    if request.method == 'GET':
        return render(request, 'link/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'link/login.html', {'form': AuthenticationForm()})
        else:
            login(request, user)
            return redirect('home', request.user.id)


@login_required()
def home(request, user_id):
    profile = Profile.objects.get(user_id=request.user.id)
    link_dbs = LinkDB.objects.filter(user_id=profile.user.id)
    size = len(link_dbs)
    counter = link_dbs.count()

    link_all = LinkDB.objects.exclude(user_id=profile.user.id, isPrivate=True)

    if size < 6:
        return render(request, "link/home.html", {'link_dbs': link_dbs, 'counter': counter, 'link_all': link_all})
    else:
        return render(request, "link/home.html", {'link_dbs': link_dbs[size - 6: size + 1], 'counter': counter,
                                                  'link_all': link_all[size - 6: size + 1]})


@login_required()
def logout1(request):
    logout(request)
    return redirect('homepage')

# =======================================
# CRUD
# =======================================

@login_required()
def create(request):
    profile = Profile.objects.get(user_id=request.user.id)
    choices = [(key, value) for key, value in CATALOG_CHOICES if key in profile.catalogChoice]

    if request.method == 'GET':
        return render(request, 'link/create.html', {'form': LinkForm(choices)})
    else:
        try:
            isPrivate2 = request.POST.get('isPrivate', False)

            if isPrivate2 != False:
                isPrivate2 = True

            link  = LinkDB(user_id = request.user, name = request.POST["name"], url = request.POST["url"], isPrivate = isPrivate2, catalogChoice = request.POST["catalogChoice"])
            link.save()

            return redirect('show', request.user.id)
        except ValueError:
            return render(request, 'link/create.html', {'form': LinkForm(), 'errMsg': 'Data mismatch'})


@login_required()
def show(request, user_id):
    profile = Profile.objects.get(user_id=request.user.id)
    link_dbs = LinkDB.objects.filter(user_id=profile.user.id)
    my_catalog = profile.catalogChoice
    size = len(my_catalog)
    print(size)
    print(my_catalog)
    return render(request, "link/show.html", {'link_dbs': link_dbs, 'my_catalog': my_catalog, 'size':size})


@login_required()
def update(request, id):
    link = get_object_or_404(LinkDB, pk=id, user_id=request.user)
    if request.method == 'GET':
        link.delete()
        return redirect('create')
    else:
        try:
            form = LinkForm(request.GET, instance=link)
            return render(request, 'link/create.html', {'link': link, 'form': form})
        except ValueError:
            return render(request, 'link/create.html', {'form': LinkForm(), 'errMsg': 'Data mismatch'})



@login_required()
def destroy(request, id):
    link = get_object_or_404(LinkDB, pk=id, user_id=request.user)
    if (request.method == 'POST'):
        link.delete()
        return redirect('show', request.user.id)

# =======================================
# Extra
# =======================================
@login_required()
def listAll(request):
    users = User.objects.all()
    Profiles = Profile.objects.all()
    link_dbs = LinkDB.objects.filter(isPrivate=False)
    choices = [key for key, value in CATALOG_CHOICES]
    return render(request, 'link/listall.html', {'link_dbs': link_dbs, 'users': users,'choices': choices})


@login_required()
def catalog(request):
    return render(request, 'link/catalog.html')


@login_required()
def cataloglist(request):
    return render(request, 'link/cataloglist.html')


@login_required()
def copyToMe(request, user_id):
    linkFromUser = get_object_or_404(LinkDB, id = user_id)
    link = LinkDB(user_id_id = request.user.id, name = linkFromUser.name, url = linkFromUser.url, isPrivate = False, catalogChoice = linkFromUser.catalogChoice)
    link.save()
    return redirect('listAll')

