from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'users'
urlpatterns = [
    path('', views.profiles, name='profiles-all'),
    path('profile/<str:pk>/', views.profile, name='single-profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('delete-account/', views.deleteAccount, name='delete-account'),

    path('create-skill/', views.createSkill, name='create-skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),

    path('inbox/',views.inbox,name='inbox'),
    path('view-message/<str:pk>/',views.viewMessage,name='view-message'),
    path('create-message/<str:pk>/',views.createMessage,name='create-message'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)