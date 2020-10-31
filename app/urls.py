
from django.urls import path
from app import views
from app.views import SearchResultsView

urlpatterns = [
    path('',views.home ,name = 'home'),
    path('<int:id>/',views.subject_page ,name='subject_page'),
    path('detail/<int:pk>/update/', views.PostUpdateView.as_view(), name="post_update"),
    path('detail/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post_delete"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('add/',views.add_post, name="add_post"),
    path('get_subject', views.get_subject, name="get_subject"),
    path('profile/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),
    path('search/',  SearchResultsView.as_view(),name = "search"),
    path('advertising/',  views.advertisings_page,name = "advertising"),
    path('advertising/<int:pk>/update/', views.AdvertisingUpdateView.as_view(), name="advertising_update"),
    path('advertising/<int:pk>/delete/', views.delete_advertising, name="advertising_delete"),





]
  