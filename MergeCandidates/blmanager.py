from . import dbmanager
from . import utils
import copy

def save_user(user_obj):
    try:
        dbmanager.save(user_obj)
        return utils.get_response_obj(None, 'user added successfully', 200)
    except:
        return utils.get_response_obj(None, 'unable to add user', 100)

def update_user(user_obj):
    try:
        dbmanager.update(user_obj)
        return utils.get_response_obj(None, 'user updated successfully', 200)
    except:
        return utils.get_response_obj(None, 'unable to update user', 100)

def get_user_list():
    try:
        user_list = dbmanager.get_user_list()
        return utils.get_response_obj(user_list, 'user list fetched successfully', 200)
    except:
        return utils.get_response_obj(None, 'unable to fetch user list', 100)

def get_potential_merge_candidates(user_id):
    try:
        user_detail = dbmanager.get_user_detail(user_id)
        if len(user_detail['contactList']) == 0:
            return utils.get_response_obj(None, 'potential merge candidates doest not exists', 200)

        potential_merge_candidates = []
        traced_contact = {}
        current_index = 0
        for contact_name, contact_value in user_detail['contactList'].items():
            temp1 = copy.copy(traced_contact)
            temp2 = copy.copy(traced_contact)
            exists = False
            fill_index = -1
            for contact_info in contact_value:
                if contact_info['value'] in traced_contact:
                    exists = True
                    fill_index = traced_contact[contact_info["value"]]

                temp1[contact_info["value"]] = current_index
                temp2[contact_info["value"]] = current_index + 1
            if exists:
                traced_contact = copy.copy(temp1)
                potential_merge_candidates[fill_index - 1].append(contact_name)
            else:
                traced_contact = copy.copy(temp2)
                potential_merge_candidates.append([contact_name])
                current_index = current_index + 1

        return utils.get_response_obj(potential_merge_candidates, 'potential merge candidates fetched successfully', 200)
    except Exception as e:
        return utils.get_response_obj(None, 'unable to fetch potential merge candidates', 100)


