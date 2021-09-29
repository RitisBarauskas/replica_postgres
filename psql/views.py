from django.http import HttpResponse
from .models import Worker


def create_data(request):
    for i in range(15):
        worker = Worker(fio=f'Иван Иваныч Иванов #{i}')
        worker.save()

    return HttpResponse('Мы трудоустроили 15 сотрудников')


def db_up(request):
    workers = Worker.objects.all()
    res = '<h1>Данные из основной базы данных</h1>'
    for worker in workers:
        res += f'{worker}<br>'
    return HttpResponse(res)

def use_replica():
    pass


def db_down():
    pass
