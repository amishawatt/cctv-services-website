from django.contrib import admin
from myapp.models import Service,Member,Plans,Review,Payment

# Register your models here.
admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display= ('sname','des','category')
    search_fields = ('category'),
admin.site.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('fname','uname','pw','phone','email')
class PlansAdmin(admin.ModelAdmin):
    list_display = ('plann','plandes','planamt')
admin.site.register(Plans)
admin.site.register(Review)
admin.site.register(Payment)




