from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
# Create your views here.

def members(request):
    member = Member(firstname='Yasir', lastname='Developer')
    member.save()
    mymembers = Member.objects.all().values()
    context = {
    'mymembers': mymembers,
    }
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render(context,request))