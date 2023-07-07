from django.shortcuts import render
from .models import Post


def home(request):
	context = {
    	'posts': Post.objects.all()
	}
	return render(request, 'home.html', context)
#    return HttpResponse('<h1>Главная</h1>')

def about(request):
	return render(request, 'about.html', {'title': 'О клубе Python Bytes'})
#    return HttpResponse('<h1>Наш клуб</h1>')


# Create your views here.

