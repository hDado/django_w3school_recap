from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member #import models; "Member class" from DB to populate date in the front-end

"""
    The members view does the following:

Creates a mymembers object with all the values of the Member model.
Loads the all_members.html template.
Creates an object containing the mymembers object.
Sends the object to the template.
Outputs the HTML that is rendered by the template.
"""
def members(request): #name of view can be different
    """ template = loader.get_template('myfirst.html')
    return HttpResponse(template.render()) 
    ============================="""
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))
    
def details(request, id):    
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


"""
def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
"""
def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))