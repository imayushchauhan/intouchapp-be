from pymongo import MongoClient
from . import utils

def save(user_obj):
    data = get_data_for_saving_user_obj()

    if data['database'] == 1:
        user_obj['_id'] = get_primary_key_value(data['database'])
    else:
        user_obj['_id'] = get_primary_key_value(data['database'])

    return data['collection'].insert_one(user_obj).inserted_id

def get_data_for_saving_user_obj():
    in_touch_app_one = MongoClient('mongodb://in-touch-app-one:in-touch-app-one@ds251197.mlab.com:51197/in_touch_app_one').in_touch_app_one
    in_touch_app_two = MongoClient('mongodb://in-touch-app-two:in-touch-app-two@ds151207.mlab.com:51207/in_touch_app_two').in_touch_app_two

    if in_touch_app_one.user.count() <= in_touch_app_two.user.count():
        return {'database': 1, 'collection': in_touch_app_one.user}
    else:
        return {'database': 2, 'collection': in_touch_app_two.user}

def get_primary_key_value(identifier):
    return str(identifier) + utils.get_random_str(23)

def update(user_obj):
    user_id = user_obj['_id']
    collection = get_data_for_updating_user_obj(user_id)
    user_obj.pop('_id', None)
    return collection.update({'_id': user_id}, {'$set': user_obj}, upsert=False, multi=False)

def get_data_for_updating_user_obj(user_id):
    in_touch_app_one = MongoClient('mongodb://in-touch-app-one:in-touch-app-one@ds251197.mlab.com:51197/in_touch_app_one').in_touch_app_one
    in_touch_app_two = MongoClient('mongodb://in-touch-app-two:in-touch-app-two@ds151207.mlab.com:51207/in_touch_app_two').in_touch_app_two

    if user_id[:1] == '1':
        return in_touch_app_one.user
    else:
        return in_touch_app_two.user

def get_user_list():
    in_touch_app_one = MongoClient('mongodb://in-touch-app-one:in-touch-app-one@ds251197.mlab.com:51197/in_touch_app_one').in_touch_app_one
    in_touch_app_two = MongoClient('mongodb://in-touch-app-two:in-touch-app-two@ds151207.mlab.com:51207/in_touch_app_two').in_touch_app_two

    user_list = []

    in_touch_app_one_user_list = in_touch_app_one.user.find()
    for user_obj in in_touch_app_one_user_list:
        user_list.append(user_obj)

    in_touch_app_two_user_list = in_touch_app_two.user.find()
    for user_obj in in_touch_app_two_user_list:
        user_list.append(user_obj)

    return user_list

def get_user_detail(user_id):
    collection = get_data_for_updating_user_obj(user_id)
    return collection.find_one({'_id': user_id})