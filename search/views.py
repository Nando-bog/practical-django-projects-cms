#coding=utf-8
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect

def search(request):
    query = request.GET.get('q', '')
    keyword_results = results = []
    if query:
        keyword_results=FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        if keyword_results.count() == 1:
            return HttpResponseRedirect(keyword_results[0].get_absolute_url())
        results = FlatPage.objects.filter(content__icontains=query)
        if results.count() == 1:
            return HttpResponseRedirect(results[0].get_absolute_url())
    #results = FlatPage.objects.filter(content__icontains=query)
    #template = loader.get_template('search.html')
    #context = Context({'query': query, 'results': results })
    #response = template.render(context)
    #return HttpResponse(response)
    return render_to_response(
        'search.html',
        {'query': query,
         'keyword_results':keyword_results,
         'results': results}
    )

def home(request):
    return render_to_response(
        'home.html',
        {"all_pages": FlatPage.objects.all()}
    )