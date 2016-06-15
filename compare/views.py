from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
# Create your views here.
import json
from django.shortcuts import render_to_response
from compare.models import MobileDetail
from compare.models import UserDetail
import urllib2
from bs4 import BeautifulSoup
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
    #response = {'success': True, 'data': [1, 2, 3, 4, 5, 6]}
    data = MobileDetail.objects.all()
    response = {'data': data}
    obj = render_to_response('main.html', response)
    return HttpResponse(obj)
	#    return HttpResponse(json.dumps(response))
	
@csrf_exempt
def add_to_db(request):
	import pdb; pdb.set_trace();
    #read the form
	#store it in database
	if request.method == 'POST': 
		data = UserDetail()
		data.user_name = request.POST.get('name','')
		data.user_email = request.POST.get('Email','')
		data.save()
		data1 = UserDevice()
		data1.user_name = request.POST.get('name','')
		data1.minimum_price = request.POST.get('price','')
		data1.device_name = request.POST.get('phone','')
		#Detail = UserDetail.(user_name = user, user_email = email)
		data1.save()
	response = {'success': True}
	return HttpResponse(json.dumps(response))	
	
	
def open_page(url):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	response = opener.open(url)
	page = response.read()
	return page

def get_price_from_flipkart(url):
	page = open_page(url)
	soup = BeautifulSoup(page, 'html.parser')
	val = soup.find_all('span', {'class': 'selling-price omniture-field'})
	val = int(str(val[0].get_text()).split(" ")[1].replace(",", ""))
	return val

def get_price_from_snapdeal(url):
	page = open_page(url)
	soup = BeautifulSoup(page, 'html.parser')
	val = int(str(soup.find_all('span', {'class': 'payBlkBig'})[0].get_text()).replace(",", ""))
	return val

	
def get_price_from_amazon(url):
	page = open_page(url)
	soup = BeautifulSoup(page, 'html.parser')
	val = soup.find_all('span', {'id': 'priceblock_ourprice'})
	if not val:
		val = soup.find_all('span', {'id': 'priceblock_saleprice'})
	val = int(float(str(val[0].get_text().replace(" ", "").replace(",", "").encode('utf-8').replace("\xc2", "").replace("\xa0", ""))))
	return val

def update_values():
	devices = MobileDetail.objects.all()
	for device in devices():
		if device.source_website == "flipkart":
			price = get_price_from_flipkart(device.device_url)
			device.price= price
			device.save()
		elif device.source_website == "amazon":
			price = get_price_from_amazon(device.device_url)
			device.price= price
			device.save()
		elif device.source_website == "snapdeal":
			price = get_price_from_snapdeal(device.device_url)
			device.price= price
			device.save()
		else:
			device.price= 0
			device.save()