from django.contrib import admin
from .models import Emplyoee 
from .models import Production
from .models import Machine
from.models import Shift
from .models import Maintainance
from .models import Order

class EmplyoeeAdmin(admin.ModelAdmin):
	list_display=('emplyoee_name','emplyoee_id','emplyoee_address','salary')


admin.site.register(Emplyoee,EmplyoeeAdmin)	

class ProductionAdmin(admin.ModelAdmin):
	list_display=('current_time','shift','total_production','machine_in_use')

admin.site.register(Production,ProductionAdmin)	

class MachineAdmin(admin.ModelAdmin):
	list_display=('machine_id','status','current_output','last_maintainance')

admin.site.register(Machine,MachineAdmin)

class ShiftAdmin(admin.ModelAdmin):
	list_display=('shift','date','production_output','issues')

admin.site.register(Shift,ShiftAdmin)

class MainAdmin(admin.ModelAdmin):
	list_display=('machine','upcoming_maintainance','recent_maintainance')

admin.site.register(Maintainance,MainAdmin)	

class OrderAdmin(admin.ModelAdmin):
	list_display=('date_placed','customer_name','contact_number','address','product_name','quantity','total_price','payment_method','total_paid','delivery_status','expected_del')	

admin.site.register(Order,OrderAdmin)


#Register your model here