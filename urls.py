from django.urls import path
from webpage import views


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login1 ,name='login'),
    path('profile',views.profile,name='profile'),
    path('python',views.python,name='python'),
    path('java',views.java,name='java'),
    path('javascript',views.javascript,name='javascript'),
    path('django',views.django,name='django'),
    path('html',views.html,name='html'),

]