from django import template

from app.models import Post, Subject


SESSION_NUM1 = 1


register = template.Library()
@register.inclusion_tag('latest_posts.html')
def latest_posts():
         context = {
        'l_posts': Post.objects.filter( subject__session=SESSION_NUM1)[0:5]
          }
         return context

@register.inclusion_tag('dropdown.html')





def dropdown():
      year_1 = Subject.objects.filter(year_num__year=1,session=SESSION_NUM1)
      year_2 = Subject.objects.filter(year_num__year=2 ,session=SESSION_NUM1)
      year_3 = Subject.objects.filter(year_num__year=3,session=SESSION_NUM1)
      year_4 = Subject.objects.filter(year_num__year=4,session=SESSION_NUM1)
      year_5 = Subject.objects.filter(year_num__year=5,session=SESSION_NUM1)
      context = {
        'year_1':year_1,
         'year_2':year_2,
          'year_3':year_3,
          'year_4':year_4,
           'year_5':year_5
        
          }
      return context

