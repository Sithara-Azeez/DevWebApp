from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
#from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings




def createProfile(sender, instance, created, **kwarg):
    
    if created:
        userobj = instance
        profile = Profile.objects.create(
            user = userobj,
            
            name = userobj.username,
            email = userobj.email,
        )
        print('Same record created in profile')

        subject = "Welcome to Developer's Web Application"
        message = "We are glad you are here"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )

def deleteUser(sender, instance, **kwarg):
    try:
        profile = instance
        user = profile.user
        user.delete()
        print('User also got deleted')
    except:
        print('User already deleted')


post_delete.connect(deleteUser, sender=Profile)
post_save.connect(createProfile, sender=User)