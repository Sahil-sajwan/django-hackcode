
from django.urls import path
from . import views
app_name = 'topics'
urlpatterns = [

    path('',views.topics,name='all_topics'),

    path('<int:topic_id>/', views.detail, name='detail'),

]