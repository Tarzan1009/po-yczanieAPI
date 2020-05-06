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
    path('users/<int:pk1>/sum/<int:pk2>', MonetarySumWith),

    path('users/<int:pk>/monetary_debts', UserDebtMonetary.as_view()),
    path('users/<int:pk1>/monetary_debts/<int:pk2>', UserDebtMonetaryWith.as_view()),
    path('users/<int:pk>/monetary_debts/sum', DebtsMonetarySum),

    path('users/<int:pk>/monetary_credits', UserCreditMonetary.as_view()),
    path('users/<int:pk1>/monetary_credits/<int:pk2>', UserCreditMonetaryWith.as_view()),
    path('users/<int:pk>/monetary_credits/sum', CreditsMonetarySum),

    path('users/<int:pk>/item_debts', UserDebtItem.as_view()),
    path('users/<int:pk1>/item_debts/<int:pk2>', UserDebtItemWith.as_view()),
    path('users/<int:pk>/item_debts/count', DebtsItemCount),

    path('users/<int:pk>/item_credits', UserCreditItem.as_view()),
    path('users/<int:pk1>/item_credits/<int:pk2>', UserCreditItemWith.as_view()),
    path('users/<int:pk>/item_credits/count', CreditsItemCount),

    path('monetary', MonetaryList.as_view()),
    path('monetary/<int:pk>', MonetaryDetails.as_view()),

    path('item', ItemList.as_view()),
    path('item/<int:pk>)', ItemDetails.as_view()),

    path('current_user', CurrentUser),
]
