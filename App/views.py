from django.shortcuts import render , get_object_or_404 ,redirect
from django import urls
from .models import *
from .forms import *
# Create your views here.
def index(request ):
    return render(request, 'index.html')


def blogdetails(request, id):
    blog = get_object_or_404(Blog, pk=id)
    comments = blog.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # عدم حفظ التعليق مباشرة
            comment.blog = blog  # تعيين القيمة لحقل blog
            comment.save()  # حفظ التعليق بعد تعيين القيمة
            return redirect('blogdetails', id=id)
    else:
        form = CommentForm()
        
    context = {
        'blog': blog,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blogdetails.html', context)


    
def blog(request ):
    blog = Blog.objects.all()
    
    context = {'blog':blog,
               }
    return render(request, 'blog.html',context)

def abut(request ):
    return render(request, 'abut.html')
def us(request ):
    return render(request, 'us.html')