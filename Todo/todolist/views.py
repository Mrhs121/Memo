from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from collections import OrderedDict
from todolist.models import *
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,HttpResponse
from django.core import serializers

class Info(View):

    def get(self, request):
        print("index GET")
        page = request.GET.get('page', 1)
        datas = Informations.objects.all().order_by('-id')

        for data in datas:
            print(data)


        paginator = Paginator(datas, 5)  # Show 5 contacts per page
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        print("contacts types", type(contacts),contacts)
        response = {}
        response['list'] = json.loads(serializers.serialize("json", datas),object_pairs_hook=OrderedDict)
        response['msg'] = 'success'
        response['status'] = 0
        print(datas.query)
        return JsonResponse(response,safe=False)

    def post(self, request):
        msg = request.POST.get('data', None)
        info = Informations(text=msg)
        info.save()
        r = {
            'status': 0,
            'msg': 'success'
        }
        response = JsonResponse(r)

        return response


class Del(View):
    def post(self,request):
        id = request.POST.get('id')
        print("====> ",id)
        Informations.objects.filter(id=id).delete()
        r = {
            'status': 0,
            'msg': 'success'
        }
        response = JsonResponse(r)

        return response
#
#
class Edit(View):
    def post(self,request):
        id = request.POST.get('id')
        text = request.POST.get('text')
        Informations.objects.filter(id=id).update(text=text)
        r = {
            'status': 0,
            'msg': 'success'
        }
        response = JsonResponse(r)

        return response

class Flag(View):
    def get(self, request):
        try:
            if request.GET["flag"] == "True":
                print("no :",request.GET['no'])
                Informations.objects.filter(id=request.GET['no'].replace('/','')).update(flag=1)
            else:
                print("no :",request.GET['no'])
                Informations.objects.filter(id=request.GET['no'].replace('/','')).update(flag=0)
        except Exception as err:
            print(err)
        return HttpResponse(u'True')





class Login(View):
    def get(self, request):
        return HttpResponseRedirect('/Login')

    @csrf_exempt
    def post(self, request):
        print(request)
        name = request.POST.get('name', None)
        pwd = request.POST.get('password', None)
        print("name:",name)
        try:
            user = User.objects.get(username=name)
            if user.password == pwd:
                r = {
                    'status': 0,
                    'msg': '登录成功！'
                }
                response = JsonResponse(r)
                response.set_cookie('username', name, expires=60 * 15)
                return response
            else:
                r = {
                    'status': 1,
                    'msg': '密码错误！'
                }
                response = JsonResponse(r)
                return response

        except Exception as e:
            r = {
                'status': 2,
                'msg': '用户未注册！'
            }

        print('username:' + name)
        print('password:' + pwd)
        print(r)
        return JsonResponse(r)

class Register(View):
    def get(self, request):
        return HttpResponseRedirect('/Login')

    @csrf_exempt
    def post(self, request):
        print(request)
        name = request.POST.get('name', None)
        pwd = request.POST.get('password', None)
        print("name:",name)
        try:
            u = User(username=name , password=pwd)
            u.save()
            r = {
                    'status': 0,
                    'msg': '注册成功！'
            }
            response = JsonResponse(r)
            response.set_cookie('username', name, expires=60 * 15)
            return response

        except Exception as e:
            r = {
                'status': 2,
                'msg': '注册失败！'
            }

        print('username:' + name)
        print('password:' + pwd)
        print(r)
        return JsonResponse(r)
