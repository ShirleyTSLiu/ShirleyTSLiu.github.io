# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Stock
import random

# Create your views here.

def index(request):
	quotes = ['You know you’re in love when you can’t fall asleep because reality is finally better than your dreams',
			  'Get busy living or get busy dying.',
			  'The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself.',
			  'When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.']
	quote = random.choice(quotes)
	return render(request, 'index.html', locals())

def about(request):
	return render(request, 'about.html', locals())

def listing(request):
	Stocks = Stock.objects.all()
	return render(request, 'list.html', locals())

def disp_detail(request, stock):
	try:
		p = Stock.objects.get(stock=stock)
	except Stock.DoesNotExist:
		raise Http404('找不到指定的品項編號')
	return render(request, 'disp.html', locals())