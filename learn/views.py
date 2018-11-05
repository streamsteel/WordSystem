from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse('<center>欢迎来到背死不偿命系统</center>')

def get_data(request):
	lists = []
	import pandas as pd
	data = pd.read_csv('../WordList.csv')
	for row in data.values:
		lists.append(row)
	return render(request, 'index.html', {'data' : lists})

def get_random(request, n=20):
	lists = []
	import pandas as pd
	data = pd.read_csv('../WordList.csv')
	data = data.sample(n)
	for row in data.values:
		lists.append(row)
	return render(request, 'index.html', {'data' : lists})