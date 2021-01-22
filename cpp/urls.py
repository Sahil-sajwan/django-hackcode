
from django.urls import path
from . import views
app_name = 'cpp'
urlpatterns = [

    path('',views.topics,name='all_topics'),

    path('<int:topic_id>/', views.detail, name='detail'),

]