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
    path('users/<int:pk>/monetaryDebts', UserDebtMonetary.as_view()),
    path('users/<int:pk>/monetaryCredits', UserCreditMonetary.as_view()),
    path('users/<int:pk>/itemDebts', UserDebtItem.as_view()),
    path('users/<int:pk>/itemCredits', UserCreditItem.as_view()),
    path('users', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),
    path('monetary', DebtMonetaryList.as_view()),
    path('monetary/<int:pk>', DebtMonetaryDetails.as_view()),
    path('item', ItemList.as_view()),
    path('item/<int:pk>)', ItemDetails.as_view()),

    path('debtsItem', DebtsItemList.as_view()),

    path('currentUser', current_user),
    path('myFriends', FriendsList.as_view()),
    path('debtsMonetarySum', MyDebtsMonetarySum),
    path('creditsMonetarySum', MyCreditsMonetarySum),
    path('debtsItemCount', MyDebtsItemCount),
    path('creditsItemCount', MyCreditsItemCount),

    path('sum', MyMonetarySum),
]

