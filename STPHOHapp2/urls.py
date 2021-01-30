from django.urls import path
from .views import home, openfiles, projectresults, deletefunc, searchfunc
from accounts.views import (
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('openfiles', openfiles, name='openfiles'),
    path('accounts/register/',register_view, name="register"),
    path('accounts/login/',login_view, name="login"),
    path('logout',logout_view, name="logout"),
    path('<int:id>', projectresults),
    path('delete/<int:id>', deletefunc),
    path('search', searchfunc, name="search"),



]
