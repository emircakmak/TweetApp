from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'), # tweet.com/tweetapp/
    path('addtweet/', views.addtweet, name='addtweet'), # tweet.com/tweetapp/addtweet
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet")
]
