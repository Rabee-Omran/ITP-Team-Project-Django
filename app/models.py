from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

SESSION = (
('1',"فصل أول"),
('2',"فصل ثاني"),
)


SUBJECT_TYPE = (
("نظري","نظري"),
("عملي","عملي"),
)

POST_TYPE = (
("محاضرة","محاضرة"),
("تسجيل","تسجيل"),
("تفريغ","تفريغ"),
)

CHOISES=(
    ('1',"الأولى"),
    ('2',"الثانية"),
    ('3',"الثالثة"),
    ('4',"الرابعة"),
    ('5',"الخامسة"),
)

class YearNum(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    session = models.CharField(max_length=15, choices=SESSION) 
    year_num = models.ForeignKey(YearNum, related_name='session_year', on_delete=models.CASCADE,)
    def __str__(self):
        return self.subject

    

class Post(models.Model):
    owner = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, related_name='subject_c', on_delete=models.CASCADE,)
    content = models.CharField(max_length=150)
    url = models.URLField()
    subject_type = models.CharField(max_length=15, choices=SUBJECT_TYPE) 
    post_type = models.CharField(max_length=15, choices=POST_TYPE) 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
   

   
    def __str__(self):
        return self.owner.username
    class Meta:
        ordering = ('-created_at',)
    
    def get_absolute_url(self):
        #return '/detail/{}'.format(self.pk)
        return reverse('subject_page', args=[self.subject.pk])



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile'.format(self.user.username)


class Advertising(models.Model):
    
    year = models.CharField(max_length=20, choices=CHOISES ,blank=True, null=True) 
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        #return '/detail/{}'.format(self.pk)
        return reverse('advertising')
    
   

   
    def __str__(self):
        return str(self.year)
    class Meta:
        ordering = ('-created_at',)
 


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)



