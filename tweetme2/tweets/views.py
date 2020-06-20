import random
from django.shortcuts import render, redirect 
from .models import Tweet
from django.http import JsonResponse
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html', {})


def tweet_list_view(request, *args, **kwargs):
    qs =Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 1234)} for x in qs ]

    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next", None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'tweets/form.html', {'form': form})

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, 'tweets/home.html', {})