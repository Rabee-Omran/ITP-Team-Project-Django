from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from app.models import Post, SessionYear, Subject
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import PostCreateFormAdmin
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

SESSION_YEAR_ID = 1
SESSION_YEAR = SessionYear.objects.get(id=SESSION_YEAR_ID)
SESSION_NUM1 = 1
def home(request):
    year_1 = Subject.objects.filter(year_num__year=1,session=SESSION_NUM1)
    year_2 = Subject.objects.filter(year_num__year=2 ,session=SESSION_NUM1)
    year_3 = Subject.objects.filter(year_num__year=3,session=SESSION_NUM1)
    year_4 = Subject.objects.filter(year_num__year=4,session=SESSION_NUM1)
    year_5 = Subject.objects.filter(year_num__year=5,session=SESSION_NUM1)

   
    

    return render(request, 'home.html', {'title':'الرئيسية','year_1':year_1, 'year_2':year_2, 'year_3':year_3,'year_4':year_4, 'year_5':year_5})


def subject_page(request, id):
    sub = get_object_or_404( Subject,id = id)
    posts = Post.objects.filter( subject = sub, session_year =SESSION_YEAR)

    if request.method == 'POST':
        post_form = PostCreateForm(data=request.POST)     
        if post_form.is_valid():    
            session_year_id = post_form.cleaned_data["session_year__year_date"]   
            session_year=SessionYear.objects.get(id=session_year_id.id)  
            new_post = post_form.save(commit=False)        
            new_post.owner = request.user
            new_post.subject = sub 
            new_post.session_year = session_year 
            new_post.save()      
            post_form.is_valid = False
            post_form = PostCreateForm()

    else:
       
        post_form = PostCreateForm()

    
    title = sub.subject
    paginator = Paginator(posts, 25)
    page = request.GET.get('page')


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
  
    
    return render(request,'detail.html', {'title':title,'posts':posts,'page': page,'form':post_form})









class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):   
    model = Post
   
    template_name = 'post_update.html'
    form_class = PostCreateForm
    login_url = 'login' 
    def get_context_data(self, **kwargs):  #more than one context  [sea list.html]
        context = super().get_context_data(**kwargs)
        context['title'] =  'تحرير'
       
        return context
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        
        
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == self.request.user:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    login_url = 'login' 
    template_name = 'post_confirm_delete.html'


    def get_context_data(self, **kwargs):  #more than one context  [sea list.html]
        context = super().get_context_data(**kwargs)
        context['title'] =  'حذف'
       
        return context

    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        post = self.get_object()
        print(post.id)
        post_obj = Post.objects.get( id = post.id, session_year =SESSION_YEAR) 
        self.object.delete()
        return HttpResponseRedirect(success_url+str(post.subject.id))
     
    def test_func(self):
        post = self.get_object()
        if self.request.user == self.request.user:
            return True
        return False




def login_user(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'هناك خطأ في اسم المستخدم او كلمة المرور')
    return render(request, 'login.html', {
        'title': 'تسجيل الدخول',
    }
    )

def logout_user(request):
    logout(request)
    return render(request, 'logout.html', {
        "title": 'تسجيل الخروج'})

@login_required(login_url='login')
def add_post(request):
    
   

    if request.method == 'POST':
        post_form = PostCreateFormAdmin(data=request.POST)     
        if post_form.is_valid():  
            content = name = post_form.cleaned_data.get('content')
            new_post = post_form.save(commit=False)
            year_id = post_form.cleaned_data.get('session_year__year_date')
            year_obj = SessionYear.objects.get(id=year_id.id)

            subject_id = post_form.cleaned_data.get('subject__subject')
            subject_obj = Subject.objects.get(id=subject_id.id)

            new_post.session_year = year_obj
            new_post.subject = subject_obj
            # new_post.subject.session = session_id
            

           
            new_post.owner = request.user
            new_post.save()
            messages.success(request, '  تم إضافة " {} "  في مادة " {} " '.format(content,subject_obj.subject))
            
           
          
            post_form.is_valid = False
            post_form = PostCreateFormAdmin()

    else:
       

        post_form = PostCreateFormAdmin()


    return render(request, 'add_post.html', {
        'title': ' إضافة منشور','form':post_form
    }
    )


@csrf_exempt 
def get_subject(request):
   
    year_num_id=request.POST.get("year_num_id")
    session_id=request.POST.get("session_id")

    subjects =Subject.objects.filter(session=session_id,year_num__year = year_num_id)
    print(subjects)
    list_data=[]

    for sub in subjects:
        data_small={"id":sub.id,"name":sub.subject}
        list_data.append(data_small)
    print(list_data)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)   



@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(owner=request.user, session_year =SESSION_YEAR)
    post_list = Post.objects.filter(owner=request.user, session_year =SESSION_YEAR)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    num =  Post.objects.filter(owner=request.user,  session_year =SESSION_YEAR).count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'profile.html', {
        "title": "الملف الشخصي",
        "posts": posts,
        'page': page,
        'num': num,
        'post_list': post_list,
    })


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
       
        if user_form.is_valid() :
            user_form.save()
            messages.success(request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')


    else:
        user_form = UserUpdateForm(instance=request.user)
      

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        

    }

    return render(request, "profile_update.html", context)

