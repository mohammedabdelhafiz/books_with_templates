from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=70)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Author(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    notes=models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



def get_all_books():
    return Book.objects.all()

def add_book(title,desc):
    return Book.objects.create(title=title,desc=desc)

def get_bookbyid(id):
    return Book.objects.get(id=id)

def get_all_authors():
    return Author.objects.all()

def get_authorbyid(id):
    return Author.objects.get(id=id)

def add_author(firstname,lastname,notes):
    mbooks=Book.objects.get(id=1)
    mauthors=Author.objects.get(id=1)

    mauthors.books.add(mbooks)
    return Author.objects.create(firstname=firstname,lastname=lastname,notes=notes)

# def manybooksauthors():
#     mbooks=Book.objects.get(id=1)
#     mauthors=Author.objects.get(id=1)

#     mauthors.books.add(mbooks)
