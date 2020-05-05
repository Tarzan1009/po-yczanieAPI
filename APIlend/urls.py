from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.conf.urls import include

urlpatterns = [
    url(r'^auth/login/$',
        obtain_auth_token,
        name='auth_user_login'),
    url(r'^auth/register/$',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    url(r'^auth/logout/$',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout'),

    path('users', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),
    path('users/<int:pk>/friends', UserFriends.as_view()),
    path('users/<int:pk>/sum', MonetarySum),

    path('users/<int:pk>/monetaryDebts', UserDebtMonetary.as_view()),
    path('users/<int:pk1>/monetaryDebts/<int:pk2>', UserDebtMonetaryWith.as_view()),
    path('users/<int:pk>/monetaryDebts/sum', DebtsMonetarySum),

    path('users/<int:pk>/monetaryCredits', UserCreditMonetary.as_view()),
    path('users/<int:pk1>/monetaryCredits/<int:pk2>', UserCreditMonetaryWith.as_view()),
    path('users/<int:pk>/monetaryCredits/sum', CreditsMonetarySum),

    path('users/<int:pk>/itemDebts', UserDebtItem.as_view()),
    path('users/<int:pk1>/itemDebts/<int:pk2>', UserDebtItemWith.as_view()),
    path('users/<int:pk>/itemDebts/count', DebtsItemCount),

    path('users/<int:pk>/itemCredits', UserCreditItem.as_view()),
    path('users/<int:pk1>/itemCredits/<int:pk2>', UserCreditItemWith.as_view()),
    path('users/<int:pk>/itemCredits/count', CreditsItemCount),

    path('monetary', MonetaryList.as_view()),
    path('monetary/<int:pk>', MonetaryDetails.as_view()),

    path('item', ItemList.as_view()),
    path('item/<int:pk>)', ItemDetails.as_view()),

    path('currentUser', CurrentUser),
]
