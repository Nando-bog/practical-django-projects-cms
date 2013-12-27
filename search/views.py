#coding=utf-8
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
    #results = FlatPage.objects.filter(content__icontains=query)
    #template = loader.get_template('search.html')
    #context = Context({'query': query, 'results': results })
    #response = template.render(context)
    #return HttpResponse(response)
    return render_to_response(
        'search.html',
        {'query': query, 'results': results}
    )