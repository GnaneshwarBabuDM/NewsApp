from django.shortcuts import render
from newsapi import NewsApiClient
from .models import UserAuthenticationDetails,UserSearchData
import datetime 

# Create your views here.
# Create your views here. 
def search(request):
    return render(request, 'search.html')

def login(request):
    return render(request, 'login.html', {'message' : 'first_time'})

def signup_page(request):
    return render(request, 'signup.html')

def check_and_update_new_signin_data_to_db(request):
    user_exist = False
    try:
        if request.method == 'POST':
            # Getting username and password fron UI
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user_count = UserAuthenticationDetails.objects.filter(user_name__iexact = user_name).count()

            if user_count == 1:
                user_exist = True
                return render(request,'login.html', {'message' : 'user_exists'})
            elif user_count == 0:
                print(user_name, password)
                new_user_db_update = UserAuthenticationDetails()
                new_user_db_update.user_name = user_name
                new_user_db_update.password = password
                new_user_db_update.created_on = datetime.datetime.now()
                new_user_db_update.save()
                return render(request, 'login.html', {'message' : 'user_updated'})
    except Exception:
        print('Error')
'''
@require_http_methods(["POST"]) # This allows only the post method (optional)
@csrf_exempt # This is to avoid exception (hacker setting.py malware related stuff)
'''

def user_login_check(request):
    user_exist = False
    print('user_login')
    try:
        if request.method == 'POST':
            print('user_login_into_method')
            # Getting username and password fron UI
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user_count = UserAuthenticationDetails.objects.filter(user_name__iexact = user_name ,password__iexact = password).count()
            print(user_name, password, user_count)
            # Checking if user credentials are correct
            if user_count == 1:
                user_exist = True
                request.session['user_name'] = user_name
                return render(request, 'index.html')
            elif user_count == 0:
                return render(request, 'signup.html')    
        
    except Exception:
        print('Error')


def index(request):
    if request.method == 'POST':
        searched_text = request.POST['search_text']
        newsapi = NewsApiClient(api_key ='API_KEY')
        # top = newsapi.get_top_headlines(q = searched_text , qintitle = searched_text)
        user_name = request.session['user_name']

        id = UserAuthenticationDetails.objects.only('id').get(user_name = user_name).id

        top = newsapi.get_top_headlines(q = searched_text , qintitle = searched_text)
    else:
        newsapi = NewsApiClient(api_key ='API_KEY')
        top = newsapi.get_top_headlines()

    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def logout(request):
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return render(request, 'login.html', {'message' : 'first_time'})