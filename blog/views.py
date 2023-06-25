from django.shortcuts import render
from django.http import HttpResponse
from config import *

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]

def home(request):
	context = {
    	'posts': posts
	}
	return render(request, 'home.html', context)
#    return HttpResponse('<h1>Главная</h1>')

def about(request):
	return render(request, 'about.html', {'title': 'О клубе Python Bytes'})
#    return HttpResponse('<h1>Наш клуб</h1>')


# Create your views here.

