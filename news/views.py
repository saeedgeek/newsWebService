from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Author,New
from django.forms.models import model_to_dict
from django.utils import timezone
import itertools
# Create your views here.

def set_news(request):
    if  request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        sender=body["name"]
        text=body["text"]
        time=timezone.now()
        authors=Author.objects.all()
        for auth in authors :
            if auth.name==sender:
                n=New(text=text,dt=time,autor_id=auth)
                n.save()
                return JsonResponse({"ok" : "new succesFully add"})       


        return JsonResponse({"error" : "user is not exist"})       
    else:
        return JsonResponse({"error" : "return post request"})       


def set_autor(request):
    if  request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        auth=Author(name=body['name'])
        auth.save()
        return HttpResponse('ok')
    else:
        return JsonResponse({"error" : "return post request"})      

def getAuthorNews(request):
    if  request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        auth=Author(name=body['name'])
        news=New.objects.filter(autor_id=auth) 
        response=[]
        for new in news:
            response.append(model_to_dict(new))
        return JsonResponse({"response":response})
    else:
        return JsonResponse({"error" : "return post request"})          


    

def getAllNews(request):
    if  request.method == 'GET':
        news=New.objects.all()
        anslist=[]
        for new in news:
            anslist.append( model_to_dict(new))
        return JsonResponse({"response":anslist})
    else:
        return JsonResponse({"error" : "return GET request"})          



def DeleteNews(request):
    if  request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name=body["name"] #name shakhs
        newsId=body["newsId"]#id khabar
        news=New.objects.filter(id=newsId)#filter khabar barasas id 

        if not news :
            return JsonResponse({"error" : "the news with this id is not exist"})          
      
        else:
            for n in news :    
                if n.autor_id.name == name:
                    news.delete()
                    return JsonResponse({"ok" : "the news completly removed"})          

                else:
                    return JsonResponse({"error" : "this new is not for that author"})          

    else:
        return JsonResponse({"error" : "return DELETE request"})          


def UpdateNews(request):
    if  request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name=body["name"] #name shakhs
        newsId=body["newsId"]#id khabar
        NewText=body["text"]
        news=New.objects.filter(id=newsId)#filter khabar barasas id 
   
        if not news :
            return JsonResponse({"error" : "the news with this id is not exist"})                
        else:
            for n in news :    
                if n.autor_id.name == name:
                    n.text=NewText
                    n.save()
                    return JsonResponse({"ok" : "the news completly Update"})          

                else:
                    return JsonResponse({"error" : "this new is not for that author"})          
    else:
        return JsonResponse({"error" : "return PUT request"})          

