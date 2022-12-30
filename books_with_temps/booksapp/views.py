from django.shortcuts import render,HttpResponse,redirect
from . import models


def index(request):
    context = {
        'books' : models.get_all_books
    }
    return render(request,"index.html",context)


def addbook(request):
    book=request.POST
    models.add_book(book['title'],book['desc'])
    return redirect('/')

def viewbook(request,id):
    context={
        'book':models.get_bookbyid(id)
        
    }
    return render(request,'single_book.html',context)



def addauthor(request):
    author=request.POST
    models.add_author(author['firstname'],author['lastname'],author['notes'])
    return redirect('/author')

def author(request):
    context = {
        'authors' : models.get_all_authors
    }
    return render(request,"authors.html",context)

def authordesc(request,id):
    context = {
        'author':models.get_authorbyid(id)
    }
    return render(request,'single_author.html',context)