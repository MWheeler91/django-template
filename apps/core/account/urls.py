from django.urls import path
from apps.core.account import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from account.views import RegisterView, LoginView

app_name = 'account'

urlpatterns = [
     path('me/', views.me, name='me'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
     















    # path('logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),

    #NOT USING PASSWORDS RESETS IN THIS PROJECT
#     path('register/', RegisterView.as_view(), name='register'),

#     path('password_reset/',
#          auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html",
#                                               email_template_name="auth/password_reset_email.html",
#                                               success_url=reverse_lazy('account:password_reset_done')
#                                               ), name="reset_password"),

#     path('password_reset_sent/',
#          auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_sent.html",
#                                                   ), name="password_reset_done"),

#     path('reset/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_form.html",
#                                                      success_url=reverse_lazy('account:password_reset_complete')
#                                                      ), name="password_reset_confirm"),

#     path('password_reset_complete/',
#          auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html",
#                                                       ), name="password_reset_complete"),


    # Denis ivy
    # path('reset_password/',
    #      auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"),
    #      name="reset_password"),
    #
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_sent.html"),
    #      name="password_reset_done"),
    #
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_form.html"),
    #      name="password_reset_confirm"),
    #
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_done.html"),
    #      name="password_reset_complete"),

]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''



    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']