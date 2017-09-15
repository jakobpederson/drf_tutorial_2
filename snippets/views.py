# Writing regularr Django views using our Serializer
# Let's see how we can write some API views using our new Serializer class. For the moment we won't use any of REST
# framework's other features, we'll just write the views as regular Django views.
# Edit the snippets/views.py file, and add the following.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# The root of our API is going to be a view that supports listing all the existing snippets, or creating a new snippet.

@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark
# the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views actually use
# more sensible behavior than this, but it'll do for our purposes right now.

# We'll also need a view which corresponds to an individual snippet, and can be used to retrieve, update or delete the
# snippet.'

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
