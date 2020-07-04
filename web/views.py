from django.shortcuts import render, redirect
from datetime import datetime

from web.models import Publication

publications_data = [
    {
        'id': 0,
        'title': 'Название',
        'date': datetime.now(),
        'text': 'lalala',
        'comments': [
            {
                'name': 'Vasya',
                'text': 'cool',
                'id': 0,
                'date': datetime.now(),
            }
        ]
    },
    {
        'id': 1,
        'title': 'Название_1',
        'date': datetime.now(),
        'text': 'lalala',
        'comments': [],
    },
]
contact_data = []


def index(request):
    return render(request, 'index.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def publications(request):
    publications_sorted = Publication.objects.order_by('-date')
    return render(request, 'publications.html', {'publications': publications_sorted})


def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/')
    return render(request, 'publication.html', publication)


def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            Publication.objects.create(title=title, text=text)
            return redirect('/publications')
        else:
            return render(request, 'post.html', {
                'error': 'title и text не должны быть пустыми'
            })
    return render(request, 'post.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            contact_data.append({
                'id': len(contact_data),
                'name': name,
                'date': datetime.now(),
                'text': text
            })
            return redirect('/contacts')
        else:
            return render(request, 'contacts.html', {
                'error': 'name и text не должны быть пустыми'
            })
    return render(request, 'contacts.html')


def comment(request, pub_id: int):
    publication = Publication.objects.get(id=pub_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            publication['comments'].append({
                'id': len(publication['comments']),
                'name': name,
                'date': datetime.now(),
                'text': text
            })
            return redirect('/publication/' + str(pub_id))
        else:
            return render(request, 'publication.html', {
                'error': 'name и text не должны быть пустыми',
                'date': publication.date,
                'text': publication.text,
                'title': publication.title,
            })
    return render(request, 'publication.html', {'publication': publication})
