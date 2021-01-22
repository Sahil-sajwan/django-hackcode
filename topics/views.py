from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Topic

def topics(request):
    topics=Topic.objects.all().order_by('id')
    paginator=Paginator(topics,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'topics/topic.html',{'topics':page_obj})

def detail(request,topic_id):
    topic=get_object_or_404(Topic,pk=topic_id)
    return render(request,'topics/detail.html',{'topic':topic})
