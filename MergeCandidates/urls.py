from django.urls import path

from . import controller

urlpatterns = [
    path('save-user', controller.save_user, name='save-user'),
    path('update-user', controller.update_user, name='update-user'),
    path('get-user-list', controller.get_user_list, name='get-user-list'),
    path('get-potential-merge-candidates', controller.get_potential_merge_candidates, name='get-potential-merge-candidates')
]