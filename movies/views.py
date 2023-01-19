# from django.shortcuts import render
from django.http import HttpResponse
import time 
from .models import Movies, Theatres
from asgiref.sync import sync_to_async
import asyncio
# Create your views here.

def get_movies():
    print('getting movies...')
    time.sleep(5)
    qs = Movies.objects.all()
    print(qs)
    print('all movies fetched')

def get_theatres():
    print('getting theatres...')
    time.sleep(5)
    qs = Theatres.objects.all()
    print(qs)
    print('all theatres fetched')

@sync_to_async
def get_movies_async():
    print('getting movies ...')
    time.sleep(2)   
    qs = Movies.objects.all()
    print(qs)
    print('all movies fetched') 

@sync_to_async
def get_theatres_async():
    print('getting theatres ...')
    time.sleep(5)   
    qs = Theatres.objects.all()
    print(qs)
    print('all movies fetched') 

def sync_view(request):
    start_time = time.time()
    get_movies()
    get_theatres()
    total = time.time() - start_time
    return HttpResponse(f'time taken { total }')

async def async_view(request):
    # approach 1
    # movie_task = asyncio.ensure_future(get_movies_async())
    # theatres_task = asyncio.ensure_future(get_theatres_async())
    # await asyncio.wait([movie_task, theatre_task])
    # approach 2 using gather
    await asyncio.wait(get_movies_async, get_theatres_async)
    total = time.time() - start_time
    return HttpResponse(f'time taken async { total}')








