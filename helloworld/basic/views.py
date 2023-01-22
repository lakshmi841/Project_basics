from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

TEMPLATE_DIRS = ('os.path.join(BASE_DIR,"templates"),')
def index(request):
    return render(request, "index.html")