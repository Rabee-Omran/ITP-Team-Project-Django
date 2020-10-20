from django import forms
from .models import Post
from django.contrib.auth.models import User
from app.models import SessionYear, Subject

CHOISES=(
    (1,'الأولى'),
(2,"الثانية"),
(3,"الثالثة"),
(4,"الرابعة"),
(5,"الخامسة"),
)


SESSION =(
    (1,' الأول'),
(2," الثاني"),

)

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(label='العنوان')
    url = forms.URLField(label='الرابط')
    session_year__year_date = forms.ModelChoiceField(label=" العام الدراسي",required=True, widget=forms.Select, queryset=SessionYear.objects.all())
    class Meta:
        model = Post
        fields = [ 'content','url','session_year__year_date']



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
    session_year__year_date = forms.ModelChoiceField(label=" العام الدراسي",required=True, widget=forms.Select, queryset=SessionYear.objects.all())
    class Meta:
        model = Post
        fields = ['subject__year_num__year','session','subject__subject', 'content','url','session_year__year_date']

