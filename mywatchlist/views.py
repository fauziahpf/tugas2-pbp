from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create views here
def show_watchlist(request):
    data_film_watchlist = MyWatchlist.objects.all()

    x=0
    for film in data_film_watchlist:
        if film.watched == "Done":
            x+=1

    flag = ''
    if x < 5:
        flag = 'Wah, kamu masih sedikit menonton!'
    else:
        flag = 'Selamat, kamu sudah banyak menonton!'

    context = {
        'list_film': data_film_watchlist,
        'nama': 'Fauziah Putri Fajrianti',
        'id': '2106707435',
        'flag': flag,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Acknowledgement
# Review data source: https://www.rottentomatoes.com 