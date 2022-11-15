
from django.shortcuts import render
from django.http import HttpResponse

# My imports
from .Automata import *

# from pydub import AudioSegment
# from pydub.playback import play


# Create your views here.

def index(request):

    form = PushdownAutomata(request.POST or None)

    result = 'Validando'
    welcome = 'Bienvenido, '
    info = 'aquí podrás validar sus palíndromos de "a y b" Con el uso de un automata de pila'
    validate= 'Ingrese la palabra que desea validar'
    note = 'NOTA: palabras palíndromas son aquellas que se leen igual de izquierda a derecha'
    velocityStack = 'Velocidad de la pila'
    textBotton = 'Validar'
    playAudioValidate = False
    playAudioInValidate = False

    if form.is_valid():

        form_data = form.cleaned_data

        if form.npda.accepts_input(form_data.get('word')):
            result = 'La palabra es palíndroma'
            if result == 'La palabra es palíndroma':
                playAudioValidate = True
            # return redirect('/')
        else:
            result = 'La palabra no es palíndroma'
            if result == 'La palabra no es palíndroma':
                playAudioInValidate = True
            # return redirect('/')

    context = {
        'InvalidAudio': playAudioInValidate,
        'validAudio': playAudioValidate,
        'formWord': form,
        'result': result,
        'welcome': welcome,
        'info': info,
        'validate': validate,
        'note': note,
        'velocityStack': velocityStack,
        'textBotton': textBotton
    }

    return render(request, 'index.html', context)

def index_jap(request):

    form = PushdownAutomata(request.POST or None)

    result = '検証中'
    welcome = 'いらっしゃいませ, '
    info = 'ここでは、スタック オートマトンを使用して、「a と b」の回文を検証できます。'
    validate = '確認したい単語を入力してください'
    note = '注: 回文は、左から右に同じように読める単語です。'
    velocityStack = 'スタック速度'
    textBotton = '検証'
    playAudioValidate = False
    playAudioInValidate = False
    # activate = True

    if form.is_valid():

        form_data = form.cleaned_data

        if form.npda.accepts_input(form_data.get('word')):
            result = '単語は回文です'
            if result == '単語は回文です':
                playAudioValidate = True
            # return redirect('/')
        else:
            result = 'その言葉は回文ではない'
            if result == 'その言葉は回文ではない':
                playAudioInValidate = True
            # return redirect('/')

    context = {
        # 'activate': activateAudio(activate),
        'InvalidAudio': playAudioInValidate,
        'validAudio': playAudioValidate,
        'formWord': form,
        'result': result,
        'welcome': welcome,
        'info': info,
        'validate': validate,
        'note': note,
        'velocityStack': velocityStack,
        'textBotton': textBotton
    }

    return render(request, 'index-jap.html', context)


def index_en(request):

    form = PushdownAutomata(request.POST or None)

    result = 'Validating'
    welcome = 'Welcome, '
    info = 'Here you will be able to validate your palindromes of "a and b" with the use of a stack automata'
    validate= 'Enter the word you want to validate'
    note = 'NOTE: Palindromes are words that read the same from left to right.'
    velocityStack = 'Stack velocity'
    textBotton = 'Validate'
    playAudioValidate = False
    playAudioInValidate = False
    # activate = True

    if form.is_valid():

        form_data = form.cleaned_data

        if form.npda.accepts_input(form_data.get('word')):
            result = 'The word is palindrome'
            if result == 'The word is palindrome':
                playAudioValidate = True
            # return redirect('/')
        else:
            result = 'The word is not palindrome'
            if result == 'The word is not palindrome':
                playAudioInValidate = True
            # return redirect('/')

    context = {
        # 'activate': activateAudio(activate),
        'InvalidAudio': playAudioInValidate,
        'validAudio': playAudioValidate,
        'formWord': form,
        'result': result,
        'welcome': welcome,
        'info': info,
        'validate': validate,
        'note': note,
        'velocityStack': velocityStack,
        'textBotton': textBotton
    }

    return render(request, 'index-en.html', context)

# def activateAudio(activate):
#     if activate == True:
#         activate = False
#         return activate
#     else:
#         activate = False
#         return activate
