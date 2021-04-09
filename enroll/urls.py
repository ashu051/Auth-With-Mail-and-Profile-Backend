from django.contrib import admin
from django.urls import path
from enroll import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',views.regi,name="regi"),
    path('user_login/',views.user_login,name="userlogin"),
    path('profile/',views.user_profile,name="userprofile"),
    path('logout/',views.user_logout,name="userlogout"),
    path('change_pass',views.changepass,name="changepass"),
    ##############forget password
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name='enroll/password_reset.html'),name='reset_password'),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='enroll/password_reset_done.html'),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='enroll/password_reset_confirm.html'),name='password_reset_confirm'),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='enroll/password_reset_done.html'),name='password_reset_complete'),\
         path('set/',views.setcookie,name="setcookie"),
                 path('get/',views.getcookie,name="getcookie"),
path('del/',views.delcookie,name="delcookie"),
path('mail/',views.user_mail,name="mail")

    
]
