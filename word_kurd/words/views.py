import json
from re import split

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Word


from .forms import WordForm
# Create your views here.

def index(request):
    words_list = Word.objects.order_by('word_id')
    return render(request, 'index.html', {'words_list': words_list})


def detail(request, word_id):
    word_details = Word.objects.filter(word_id=word_id).first()
    return render(request, 'details.html', {'name': word_details.name,
                                            'meaning': word_details.meaning,
                                            'describtion': word_details.describtion}
                 )


def get_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
        # I'm gonna let this amazing piece of wated time
            '''word_object = {}
            data = []
            for word in split(r'&', request.body.decode('ascii')):
                word_object[split(r'=', word)[0]] = split(r'=', word)[1].replace('+', ' ').strip()
            data.append(word_object)
            print(data)'''
            name = form.cleaned_data['name']
            describtion = form.cleaned_data['describtion']
            meaning = form.cleaned_data['meaning']
            query = Word(name=name, describtion=describtion, meaning=meaning)
            query.save()
            return HttpResponseRedirect('/words/')
    else:
        form = WordForm()

    return render(request, 'add_word.html', {'form': form})


def vote(request, word_id):
    return HttpResponse("vote the word %s." % word_id)