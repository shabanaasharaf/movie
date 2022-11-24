from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform

# Create your views here.
def function(request):
    content=movie.objects.all()
    context={
        'movie_list':content
    }
    return render(request,"index.html",context)
def details(request,movie_id):
    number=movie.objects.get(id=movie_id)
    return render (request,"details.html",{'num':number})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        about = request.POST.get('about')
        year = request.POST.get('year')
        img = request.FILES['img']
        Movie=movie(name=name,about=about,year=year,img=img)
        Movie.save()
    return render(request,'add.html')
def update(request,movie_id):
    Movie= movie.objects.get(id=movie_id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form .save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'Movie':Movie})
def delete(request,movie_id):
    if request.method=='POST':
        Movie=movie.objects.get(id=movie_id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
