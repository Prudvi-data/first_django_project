from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,WebPage,Topic

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    my_dict = {'acc_records': webpage_list}
    return render(request,'first_app/index1.html',context=my_dict)
