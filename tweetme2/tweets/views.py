import random
from django.shortcuts import render, redirect 
from .models import Tweet
from django.http import JsonResponse
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import TweetSerializer, TweetActionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html', {})

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=201)

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists:
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists:
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs:
        return JsonResponse({'message': 'You cannot delete this tweet'}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Tweet Deleted'}, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        qs = Tweet.objects.filter(id=tweet_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == 'like':
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
            obj.likes.add(request.user)
        elif action == 'unlike':
            obj.likes.remove(request.user)
        elif action == 'retweet':
            pass

    # if request.user in obj.likes.all():
    #     obj.likes.remove(request.user)
    return Response({'message': 'Tweet Removed'}, status=200)


def tweet_list_view_pure_django(request, *args, **kwargs):
    qs =Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs ]

    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data, status=200)

@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


def tweet_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next", None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'tweets/form.html', {'form': form})

def tweet_detail_view_pure_django(request, tweet_id, *args, **kwargs):
    return render(request, 'tweets/home.html', {})












