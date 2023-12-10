from django.shortcuts import render, HttpResponse


def fio(request):
    return HttpResponse(f'Я Титов Данил Сергеeвич, 2007 года рождения, '
                        f'Программирую')


def about(request):
    return HttpResponse(f'Я не приехал, я уже был, по учебе отличник, '
                        f'учиться не люблю')


def contacts(request):
    return HttpResponse(f'Мой гитхаб: Killuaac'
                        f'Писать мне можно голубями')
