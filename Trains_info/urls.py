
from django.urls import path ,re_path ,include
from Trains_info import views
urlpatterns = [

    re_path(r'^$' , views.home , name='home'),
    re_path(r'^trains_info' , views.collect_train_info, name='train_info'),
    re_path(r'^repots' ,views.report ,name='repots'),

]
