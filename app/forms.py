from django import forms
from .models import Post
from django.contrib.auth.models import User
from app.models import Advertising, Subject

CHOISES=(
    (1,"الأولى"),
    (2,"الثانية"),
    (3,"الثالثة"),
    (4,"الرابعة"),
    (5,"الخامسة"),
)
CHOISES2=(
    ('', '----'),
    (1,"الأولى"),
    (2,"الثانية"),
    (3,"الثالثة"),
    (4,"الرابعة"),
    (5,"الخامسة"),
)


SESSION =(
    (1,' الأول'),
(2," الثاني"),

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

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(label='العنوان')
    url = forms.URLField(label='الرابط')
    subject_type = forms.ChoiceField(label="نظري / عملي",choices = SUBJECT_TYPE )
    post_type = forms.ChoiceField(label="النوع",choices = POST_TYPE )
    
    class Meta:
        model = Post
        fields = [ 'content','url','subject_type','post_type']



class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label="البريد الإلكتروني")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "email")



class PostCreateFormAdmin(forms.ModelForm):
    content = forms.CharField(label='العنوان')

    url = forms.URLField(label='الرابط')
    subject__year_num__year = forms.ChoiceField(label="السنة",choices = CHOISES )
    session = forms.ChoiceField(label="الفصل",choices = SESSION )
    subject__subject = forms.ModelChoiceField(label="  المادة", widget=forms.Select, queryset=Subject.objects.all())
    subject_type = forms.ChoiceField(label="نظري / عملي",choices = SUBJECT_TYPE )
    post_type = forms.ChoiceField(label="النوع",choices = POST_TYPE )

    class Meta:
        model = Post
        fields = ['subject__year_num__year','session','subject__subject', 'content','url','subject_type','post_type']




class AdvertisingCreateForm(forms.ModelForm):
    year = forms.ChoiceField(label="السنة",choices = CHOISES2 , required = False ,help_text= "تجاوز هذا الحقل إذا كان الإعلان عام")
    content = forms.CharField(label='الإعلان',widget= forms.Textarea)
    
    class Meta:
        model = Advertising
        fields = ['year', 'content']

