"""word_kurd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views


from django.conf import settings
# from .views import register_view, activate


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("words/", include("words.urls")),
    # re_path(r'^register/$', register_view, name='signup'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         activate, name='users_activate'),
    # re_path('login/', auth_views.LoginView, {
    #     'template_name': "users/registration/login.html"},
    #     name='login'),
    # re_path('logout/', auth_views.LogoutView,
    #     {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),

    # re_path(r'^password_reset/$', auth_views.PasswordResetView,
    #     {'template_name': "users/registration/password_reset_form.html"},
    #     name='password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView,
    #     {'template_name': "users/registration/password_reset_done.html"},
    #     name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView,
    #     {'template_name': "users/registration/password_reset_confirm.html"},
    #     name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView,
    #     {'template_name': "users/registration/password_reset_complete.html"},
    #     name='password_reset_complete'),
]
