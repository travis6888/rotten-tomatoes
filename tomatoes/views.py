import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie


def home(request):
    return render(request, 'tomatoes_base.html')

@csrf_exempt
def view_favorites(request):
    if request.method == 'GET':
        favorites = Movie.objects.all()
        data = {'favorites': favorites}
        return render_to_response('favorites.html', data)

@csrf_exempt
def new_movie_json(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],

            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score']
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score

        }
        return HttpResponse(json.dumps(movie_info), content_type='application/json')

@csrf_exempt
def new_movie_html(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],

            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score']
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score

        }

        return render_to_response('movie_template.html', movie_info)
    else:
        redirect('home')

@csrf_exempt
def delete_favorite(request):
    if request.method == 'POST':
        movie_title = json.loads(request.body)
        Movie.objects.get(title=movie_title).delete()
        movies = Movie.objects.all()
        data = {'movies': movies}

        return render_to_response('favorites.html', data)