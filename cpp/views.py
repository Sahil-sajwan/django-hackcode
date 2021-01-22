from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Cpp

def topics(request):
    topics=Cpp.objects.all().order_by('id')
    paginator=Paginator(topics,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'cpp/topic.html',{'topics':page_obj})

def detail(request,topic_id):
    topic=get_object_or_404(Cpp,pk=topic_id)
    return render(request,'cpp/detail.html',{'topic':topic})
