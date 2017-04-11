from django.shortcuts import render
from main.models import Member,Message
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json

# Create your views here.

def signUp(request):
    result = {}
    result['result'] = 0
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            user = data['user']
            password = data['password']
            name = data['name']
            members = Member.objects.filter(user=user)
            if len(members) == 0: # ok to signup
                try:
                    Member.objects.create(name=name,password=password,user=user)
                    result['result'] = 1
                except:
                    result['result'] = 'create fail'
            else:
                result['message'] = 'name is exist'
    except :
        result['message'] = 'key or format error'
    return JsonResponse(result)

    #------------------------

def login(request):
    result = {}
    result['result'] = 0
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = data['user']
        password = data['password']
        members = Member.objects.filter(user=user,password=password).only('id','name')
        if len(members) > 0 :
            m = members[0]
            #result['members'] = list(members)
            result['name'] = m.name
            result['id'] = m.id
            result['result'] = 1

    return JsonResponse(result)
#---------------------------------------
def create_message(request):
    result = {}
    result['result'] = 0
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        #Id = members id
        user = data.get('user', None)
        new_message = data.get('message', None)
        if (user is None) or (new_message is None):
            return JsonResponse({'ero':'No Message'})
        member = Member.objects.get(user = user)
        Message.objects.create(message = new_message, member = member)
        result['result'] = 1
    return JsonResponse(result)
#-------------------------------------------------
def get_message(request):
    result={}
    result['result'] = 0
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        last_id = data.get('last_id',None)
        if last_id is None:
            return JsonResponse({'result':0})
        #message_id = Message.objects.filter(id=last_id)
        #Id = Message.objects.get('id')
        latest_id = Message.objects.order_by('id').last().id
        messages = Message.objects.values('id', 'message', 'created_at', 'member__name').filter(id__range =(last_id + 1, int(latest_id)))
        #member_id = Message.objects.all().values('member_id')
        #member_name = Member.objects.filter(id = member_id).values('name')

        #result['Member'] = message_id.member.name
        result['messages'] = list(messages)
        #result['name'] = list(member_name)
        #result['messages'] = serializers.serialize('json',messages)
        if len(list(messages)) > 0:
            result['result'] = 1
        else:
            result['result'] = 0
        return JsonResponse(result)
    return JsonResponse(result)
