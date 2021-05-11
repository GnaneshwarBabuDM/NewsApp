from django.urls import path
from . import views

print('urls_file_visit')
urlpatterns = [
    path('', views.login, name ='home'),
    path('searchresult', views.index, name ='searchresult'),
    path('login_page', views.login, name = 'login'),
    path('login', views.user_login_check, name = 'check_login'),
    path('signup',views.signup_page, name ='signup_page'),
    path('updated_signup',views.check_and_update_new_signin_data_to_db, name = 'update_new_signin'),
    # path('logout', views.logout, name ='logout')
]