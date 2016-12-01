from __future__ import print_function
from django.shortcuts import render,resolve_url
from ZooApp.forms import AnimalsForm,AnimalSearchForm,BirdSearchForm,DonorForm,\
    UserCreationForm
from django.contrib.auth.forms import AuthenticationForm#,UserCreationForm
from django.urls import reverse
from ZooApp.models import Animal,Species,Bird
from django.http import HttpResponse


#login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    return render(request,template_name="ZooApp/index.html",context={'current':'homepage'})

def animals(request):
    # search for animal
    if request.method =='POST':
        form = AnimalSearchForm(data=request.POST)
        #print form
        if form.is_valid():
            aname = form.cleaned_data['name']
            sp = form.cleaned_data['species']
            try:
                Anmls = Animal.objects.get(name=aname)
            except:
                return HttpResponse("Animal Doesnot Exist<br><a href='/animals'>Go back </a>")
            try:
                spcs = Species.objects.get(common_name=sp)
            except:
                return HttpResponse("Species Doesnot Exist<br><a href='/animals'>Go back </a>")
            frm = AnimalsForm(instance = Anmls)
            if Anmls.species_id.common_name == spcs.common_name:
                cnt = '<br><br>'.join((str(Anmls.name),str(Anmls.species_id.common_name),
                                   str(Anmls.gender),str(Anmls.age)))
                return render(request, template_name='ZooApp/results.html', context={'htodisp': [Anmls, ]})
            else:
                return HttpResponse("NO RESULT EXISTS<br><a href='/animals'>Go back </a>")

        else:
            return HttpResponse("NO RESULT EXISTS<br><a href='/animals'>Go back </a>")

    else:
        tag = "Animals"
        retview = resolve_url(animals)
        retview_fetchall = resolve_url(to=fetchall_animals)
        return render(request,template_name='ZooApp/animals_form.html',
                      context={'tag':tag,'retview':retview,'current':'homepage','fetchall':retview_fetchall,})

def birds(request):
    if request.method == 'POST':
        form = BirdSearchForm(data=request.POST)
        if form.is_valid():
            bname = form.cleaned_data['name']
            sp = form.cleaned_data['species']
            try:
                brds = Bird.objects.get(name=bname)
            except:
                return HttpResponse("Bird Does not exist<br><a href='/birds/'>Go back </a>")
            try:
                spcs = Species.objects.get(common_name=sp)
            except:
                return HttpResponse("Species Doesnot Exist<br><a href='/birds/'>Go back </a>")
            if brds.species_id.common_name == spcs.common_name:
                cnt = '<br><br>'.join((str(brds.name), str(brds.species_id.common_name)
                                       , str(brds.gender), str(brds.age)))
                return render(request, template_name='ZooApp/results.html', context={'htodisp': [brds, ]})
            else:
                return HttpResponse("NO RESULT EXISTS<br><a href='/birds/'>Go back </a>")

    else:
        tag = "Birds"
        retview = resolve_url(to=birds)
        retview_fetchall = resolve_url(to=fetchall_birds)
        return render(request, template_name='ZooApp/animals_form.html',
                      context={'current':'homepage','tag':tag,'retview':retview,'fetchall':retview_fetchall})

def donor(request):
    if request.method=='POST':
        form = DonorForm(data=request.POST or None)
        if form.is_valid():
            dmodel = form.save(commit=True)
            return HttpResponse("thank you "+str(form.cleaned_data['name'])+"<br><a href='/'>Home</a>")
        else:
            return render(request,template_name='ZooApp/donor_form.html',context={'form':form,'current':'donate',})

    return render(request,template_name='ZooApp/donor_form.html',context={'current':'donate','form':DonorForm()})


def fetchall_animals(request):
    anmls = Animal.objects.all()
    return render(request,template_name='ZooApp/results.html',context={'htodisp':anmls})


def fetchall_birds(request):
    brds = Bird.objects.all()
    return render(request, template_name='ZooApp/results.html', context={'htodisp': brds})


def contact(request):
    return render(request,template_name="ZooApp/contactus.html",context={'current':'contact'})

def empview(request):
    return render(request,template_name='ZooApp/empview.html',context={'current':'employees'})#HttpResponse("YOURE ALREADY LOGGED IN")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return HttpResponse("You're registered. Wait for the "
                                "admin to assign you permissions.<br><a href='/'>Home</a>")
    else:
        form = UserCreationForm()
        return render(request=request, template_name='ZooApp/user_registration_form.html', context={'form':form},)



def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST,)
        if form.is_valid():
            login(request,form.get_user())
            #logout(request)
            return HttpResponseRedirect("/admin")
        else:
            return render(request=request, template_name='ZooApp/login_form.html', context={'form': form}, )
    form = AuthenticationForm()

    return render(request=request, template_name='ZooApp/login_form.html', context={'form': form}, )


def dummy(request):
    return HttpResponse("HELLO")

def search(request,name):
    form=None
    if name == "animals":
        FormType,Klass,tag = AnimalSearchForm,Animal,"Animals"

    elif name == "birds":
        FormType,Klass,tag = BirdSearchForm,Bird,"Birds"

    else:
        return HttpResponse("ERROR <a href='/'>Home</a>")

    if request.method == 'POST':
        form = FormType(data=request.POST)
        if form.is_valid():

            bname = form.cleaned_data['name']
            sp = form.cleaned_data['species']
            errors=False

            try:
                obj = Klass.objects.get(name=bname)
            except:
                errors=True
                form.add_error(field='name',error="%s Does not exist"%name[:-1])

            try:
                spcs = Species.objects.get(common_name=sp)
            except:
                errors=True
                form.add_error(field='species',error="Species Doesnot Exist")

            if not errors:
                if obj.species_id.common_name == spcs.common_name:
                    cnt = '<br><br>'.join((str(obj.name), str(obj.species_id.common_name)
                                       , str(obj.gender), str(obj.age)))
                    return render(request, template_name='ZooApp/results.html', context={'htodisp': [obj, ]})
                else:
                    form.add_error(field='name',error="%s does not belong to this species"%name[:-1])

    fform = form or FormType()
    retview = "/search/%s/"%name
    retview_fetchall = "/search/%s/fetchall/"%name

    return render(request, template_name='ZooApp/animals_form.html',
                      context={'current':'homepage','tag':tag,'retview':retview,'fetchall':retview_fetchall,'form':fform})

