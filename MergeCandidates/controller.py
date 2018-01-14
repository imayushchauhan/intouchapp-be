from django.http import HttpResponse
from . import blmanager
from . import utils
import json

def save_user(request):
    request_obj = json.loads(request.body.decode('utf-8'))

    save_user_response = blmanager.save_user(request_obj)

    return HttpResponse(json.dumps(save_user_response))

def update_user(request):
    request_obj = json.loads(request.body.decode('utf-8'))

    update_user_response = blmanager.update_user(request_obj)

    return HttpResponse(json.dumps(update_user_response))

def get_user_list(request):

    get_user_list_response = blmanager.get_user_list()

    return HttpResponse(json.dumps(get_user_list_response))

def get_potential_merge_candidates(request):
    request_obj = json.loads(request.body.decode('utf-8'))

    get_potential_merge_candidates_response = blmanager.get_potential_merge_candidates(request_obj['userID'])

    return HttpResponse(json.dumps(get_potential_merge_candidates_response))
