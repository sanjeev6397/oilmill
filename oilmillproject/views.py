from django.http import HttpResponse
from django.shortcuts import render
from oilapp.models import Emplyoee
from oilapp.models import Production
from oilapp.models import Machine
from oilapp.models import Shift
from oilapp.models import Maintainance
from oilapp.models import Order

def aboutus(request):
	return HttpResponse("welcome to oilmill")

def home(request):
	data = {'tittle':'oilmill'}
	return render(request,"/home/sanjeev/oilmillproject/Templates/oil.html",data)

#def emplyoee(request):
 	#return render(request,"/home/sanjeev/oilmillproject/Templates/emplyoees.html")

def about(request):
	return render(request,"/home/sanjeev/oilmillproject/Templates/about_us.html")

def order(request):
	if request.method == 'POST':
		da=request.POST.get('date2')
		nm=request.POST.get('name')
		nu=request.POST.get('number')
		ad=request.POST.get('address')
		ne=request.POST.get('name1')
		qu=request.POST.get('quantity')
		to=request.POST.get('total')
		me=request.POST.get('method')
		am=request.POST.get('amount')
		st=request.POST.get('status')
		d=request.POST.get('date3')
		er=Order(date_placed=da,customer_name=nm,contact_number=nu,address=ad,product_name=ne,quantity=qu,total_price=to,payment_method=me,total_paid=am,delivery_status=st,expected_del=d)
		er.save()
	return render(request,"/home/sanjeev/oilmillproject/Templates/order_details.html")

def maintainance(request):
	if request.method == 'POST':
		mach=request.POST.get('machine')
		up=request.POST.get('date')
		re=request.POST.get('date1')
		mt=Maintainance(machine=mach,upcoming_maintainance=up,recent_maintainance=re)
		mt.save()
	return render(request,"/home/sanjeev/oilmillproject/Templates/maintainance.html")

def machine(request):
	if request.method == 'POST':
		id=request.POST.get('machineid')
		st=request.POST.get('status')
		out=request.POST.get('output')
		maint=request.POST.get('maintainance')
		sv=Machine(machine_id=id,status=st,current_output=out,last_maintainance=maint)
		sv.save()
	return render(request,"/home/sanjeev/oilmillproject/Templates/Machinedetails.html")

def shift(request):
	if request.method == 'POST':
		sh=request.POST.get('shiftnum')
		da=request.POST.get('date')
		ou=request.POST.get('output')
		iss=request.POST.get('issues')
		shf=Shift(shift=sh,date=da,production_output=ou,issues=iss)
	return render(request,"/home/sanjeev/oilmillproject/Templates/shift.html")



def production(request):
	if request.method=='POST':
		dt=request.POST.get('time')
		shift=request.POST.get('shift')
		total_production=request.POST.get('production')
		machine_in_use=request.POST.get('machine')
		pd=Production(current_time=dt,shift=shift,total_production=total_production,machine_in_use=machine_in_use)
		pd.save()
	return render(request,"/home/sanjeev/oilmillproject/Templates/production.html")

def emplyoees(request):
	if request.method =='POST':
		name=request.POST.get('name')
		id=request.POST.get('id')
		address=request.POST.get('address')
		salary=request.POST.get('salary')
		en=Emplyoee(emplyoee_name=name,emplyoee_id=id,emplyoee_address=address,salary=salary)
		en.save()
	return render(request,"/home/sanjeev/oilmillproject/Templates/emplyoees.html")


