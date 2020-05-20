from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.conf.urls import include
from django.conf.urls.static import static

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
    url('^users/search/(?P<username>.+)/$', SearchUserList.as_view()),


    path('users', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),
    path('users/<int:pk>/friends', UserFriends.as_view()),

    path('users/<int:pk>/monetary', UserMonetary.as_view()),
    path('users/<int:pk>/monetary/sum', MonetarySum),
    path('users/<int:pk1>/monetary/<int:pk2>', UserMonetaryWith.as_view()),
    path('users/<int:pk1>/monetary/sum/<int:pk2>', MonetarySumWith),

    path('users/<int:pk>/monetary/debts', UserDebtMonetary.as_view()),
    path('users/<int:pk1>/monetary/debts/<int:pk2>', UserDebtMonetaryWith.as_view()),
    path('users/<int:pk>/monetary/debts/sum', DebtsMonetarySum),

    path('users/<int:pk>/monetary/credits', UserCreditMonetary.as_view()),
    path('users/<int:pk1>/monetary/credits/<int:pk2>', UserCreditMonetaryWith.as_view()),
    path('users/<int:pk>/monetary/credits/sum', CreditsMonetarySum),

    path('users/<int:pk>/item', UserItem.as_view()),
    path('users/<int:pk1>/item/<int:pk2>', UserItemWith.as_view()),

    path('users/<int:pk>/item/debts', UserDebtItem.as_view()),
    path('users/<int:pk1>/item/debts/<int:pk2>', UserDebtItemWith.as_view()),
    path('users/<int:pk>/item/debts/count', DebtsItemCount),

    path('users/<int:pk>/item/credits', UserCreditItem.as_view()),
    path('users/<int:pk1>/item/credits/<int:pk2>', UserCreditItemWith.as_view()),
    path('users/<int:pk>/item/credits/count', CreditsItemCount),

    path('monetary', MonetaryList.as_view()),
    path('monetary/<int:pk>', MonetaryDetails.as_view()),

    path('item', ItemList.as_view()),
    path('item/<int:pk>', ItemDetails.as_view()),

    path('proposition', PropositionList.as_view()),
    path('proposition/<int:pk>', PropositionDetails.as_view()),

    path('users/<int:pk>/proposition/sender', UserPropositionSender.as_view()),
    path('users/<int:pk>/proposition/receiver', UserPropositionReceiver.as_view()),

    path('current_user', CurrentUser),
]
