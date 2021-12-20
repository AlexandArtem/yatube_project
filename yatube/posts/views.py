from typing import Text
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    title = 'последния обновления сайта'
    text = "это главнаня страница проэкта Yatube"
    context ={
        "text" : text,
        'title': title,
    }
    return render(request, template,context)

def group_posts(request , slug):
    template = 'posts/group_list.html'
    title = 'посты выбраной групы'
    text = "здесь будут информация о групах пректа Yatube"
    context = {
        'text': text,
        'title': title,
        }
    return render(request, template,context)




