from django.http import HttpResponse
from django.shortcuts import render

#rezultatai = ('pirmas', 'antras', 'trecias', 'ketvirtas', 'penktas')

def home(request):
	return render(request, 'base.html')#, {'results': rezultatai})
	#return HttpResponse('works like candy!')

def contacts(request):
	return render(request, 'contacts.html')#, {'results': rezultatai})