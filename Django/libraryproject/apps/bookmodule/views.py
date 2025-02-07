from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.db.models import Q, Count, Sum, Avg, Max, Min

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def links(request):
    return render(request, 'bookmodule/links.html')
def show_text_formatting(request):
    return render(request, "bookmodule/text_formatting.html")
def listing(request):
    return render(request, "bookmodule/listing.html")
def tables(request):
    return render(request, "bookmodule/tables.html")
def serachBook(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte = 50))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    books_stats = Book.objects.aggregate(
        total_books = Count('id'),
        total_price = Sum('price'),
        average_price = Avg('price'),
        max_price = Max('price'),
        min_price = Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'books_stats': books_stats})

def lab9_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})

def lab9_part1_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('lab9_part1_listbooks')
    return render(request, 'bookmodule/lab9_part1_add_book.html')

def lab9_part1_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('lab9_part1_listbooks')
    return render(request, 'bookmodule/lab9_part1_edit_book.html', {'book': book})


def lab9_part1_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab9_part1_listbooks')

def lab9_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})

def lab9_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2_add_book.html', {'form': form})

def lab9_part2_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_edit_book.html', {'form': form, 'book': book})


def lab12_task1(request):
    return render(request, 'bookmodule/lab12_task1.html')

def lab12_task2(request):
    return render(request, 'bookmodule/lab12_task2.html')

def lab12_task3(request):
    return render(request, 'bookmodule/lab12_task3.html')

def lab12_task4(request):
    return render(request, 'bookmodule/lab12_task4.html')


# def index2(request, val1 = 0): #add the view function (index2)
#  return HttpResponse("value1 = "+str(val1))

# def viewbook(request, bookId):
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#     context = {'book':targetBook} # book is the variable name accessible by the template
#     return render(request, 'bookmodule/show.html', context)
