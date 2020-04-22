from django.contrib.auth import get_user_model
from django.views import View
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    token = Token.objects.create(user=serializer.instance)
    token_data = {"token": token.key}
    user_profile = UserProfile()
    user_profile.save()
    return Response(
        {**serializer.data, **token_data},
        status=status.HTTP_201_CREATED,
        headers=headers
    )


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)



class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DebtMonetaryList(generics.ListCreateAPIView):
    queryset = DebtMonetary.objects.all()
    serializer_class = DebtMonetarySerializer

class DebtMonetaryDetails(generics.RetrieveAPIView):
    serializer_class = DebtMonetarySerializer
    queryset = DebtMonetary.objects.all()

class ItemList(generics.ListCreateAPIView):
    serializer_class = DebtItemSerializer
    queryset = DebtItem.objects.all()

class ItemDetails(generics.RetrieveAPIView):
    serializer_class = DebtItemSerializer
    queryset = DebtItem.objects.all()

class FriendsList(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)
        friends_profiles = user_profile.friends.get()
        friends = friends_profiles.user.get()
        return friends





class MyDebtsMonetary(generics.ListAPIView):
    serializer_class = DebtMonetarySerializer

    def get_queryset(self):
        user = self.request.user
        return DebtMonetary.objects.filter(debtor=user)


class MyCreditsMonetary(generics.ListAPIView):
    serializer_class = DebtMonetarySerializer

    def get_queryset(self):
        user = self.request.user
        return DebtMonetary.objects.filter(creditor=user)


class MyDebtsItem(generics.ListAPIView):
    serializer_class = DebtItemSerializer

    def get_queryset(self):
        user = self.request.user
        return DebtItem.objects.filter(debtor=user)


class MyCreditsItem(generics.ListAPIView):
    serializer_class = DebtItemSerializer

    def get_queryset(self):
        user = self.request.user
        return DebtItem.objects.filter(creditor=user)


class MyDebtsMonetaryWith(generics.ListAPIView):
    serializer_class = DebtMonetarySerializer

    def get_queryset(self):
        user = self.request.user
        username = self.kwargs['username']
        return DebtMonetary.objects.filter(debtor=username).filter(creditor__username=username)


class MyCreditsMonetaryWith(generics.ListAPIView):
    serializer_class = DebtMonetarySerializer

    def get_queryset(self):
        user = self.request.user
        username = self.kwargs['username']
        return DebtMonetary.objects.filter(creditor=username).filter(debtor__username=username)


class MyDebtsItemWith(generics.ListAPIView):
    serializer_class = DebtItemSerializer

    def get_queryset(self):
        user = self.request.user
        username = self.kwargs['username']
        return DebtItem.objects.filter(debtor=username).filter(creditor__username=username)


class MyCreditsItemWith(generics.ListAPIView):
    serializer_class = DebtItemSerializer

    def get_queryset(self):
        user = self.request.user
        username = self.kwargs['username']
        return DebtItem.objects.filter(creditor=username).filter(debtor__username=username)


class DebtsMonetaryList(generics.ListCreateAPIView):
    serializer_class = DebtMonetarySerializer
    queryset = DebtMonetary.objects.all()


class DebtsItemList(generics.ListCreateAPIView):
    serializer_class = DebtItemSerializer
    queryset = DebtItem.objects.all()


@api_view(['GET'])
def MyDebtsMonetarySum(request):
    mySum = DebtMonetary.objects.filter(debtor=request.user).aggregate(Sum('amount'))
    return Response(mySum)

@api_view(['GET'])
def MyCreditsMonetarySum(request):
    mySum = DebtMonetary.objects.filter(creditor=request.user).aggregate(Sum('amount'))
    return Response(mySum)

@api_view(['GET'])
def MyMonetarySum(request):
    credits_sum = DebtMonetary.objects.filter(creditor=request.user).aggregate(Sum('amount'))
    debts_sum = DebtMonetary.objects.filter(debtor=request.user).aggregate(Sum('amount'))
    mySum = credits_sum["amount__sum"] - debts_sum["amount__sum"]
    return Response({'sum': mySum})

@api_view(['GET'])
def MyDebtsItemCount(request):
    myCount = DebtItem.objects.filter(debtor=request.user).count()
    return Response({'count':myCount})

@api_view(['GET'])
def MyCreditsItemCount(request):
    myCount = DebtItem.objects.filter(creditor=request.user).count()
    return Response({'count':myCount})