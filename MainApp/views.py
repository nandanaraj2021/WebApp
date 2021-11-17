from django.shortcuts import render

# Create your views here.
def index(request):
    #get requesting from database
    #post post information to the database
    return render(request, 'MainApp/index.html')