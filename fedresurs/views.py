from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Guid

from . import search
import json
import uuid


def check_input(company_guid):
    if len(company_guid) == 36:
        return True
    else:
        return False


def make_info(request):
    if request.method == 'POST':
        company_guid = str(request.POST['company_guid'])

        if check_input(company_guid):
            info = search.get_info(company_guid)
            if info == "Company Not Found":
                request.session['msg'] = "Такой компании нет"
                return redirect('/')
            elif not info:
                request.session['msg'] = "Сообщений о банкротстве не найдено"
                return redirect('/')
            else:
                task_guid = str(uuid.uuid4())
                guid_model = Guid.objects.create(task_guid=task_guid, info={"info": info})
                guid_model.save()

                request.session['msg'] = task_guid

                return redirect('/')
        else:
            request.session['msg'] = "Guid компании некорректен"
            return redirect('/')
    else:
        msg = request.session.get('msg', False)
        if msg:
            del(request.session['msg'])
        return render(request, 'fedresurs/make_info.html', {'msg': msg})


def get_info(request, guid):
    obj_check = Guid.objects.filter(task_guid=guid)
    if obj_check:
        obj = Guid.objects.get(task_guid=guid)
        info = obj.info
        return JsonResponse(info)
    else:
        return JsonResponse({"error": "task guid not found"})
