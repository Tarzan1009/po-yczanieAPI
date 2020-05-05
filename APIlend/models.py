from django.conf import settings
from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user', unique=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    friends = models.ManyToManyField("self", blank=True)


class DebtMonetary(models.Model):
    creditor = models.ForeignKey(UserProfile, null=True, related_name='creditorMon',
                                 on_delete=models.CASCADE)
    debtor = models.ForeignKey(UserProfile, null=True, related_name='debtorMon',
                               on_delete=models.CASCADE)
    # amount = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField()
    date = models.DateField(default=date.today)
    isActive = models.BooleanField(default=True)
    objects = models.Manager()


class DebtItem(models.Model):
    name = models.CharField(max_length=30)
    creditor = models.ForeignKey(UserProfile, null=True, related_name='creditorItem', on_delete=models.CASCADE)
    debtor = models.ForeignKey(UserProfile, null=True, related_name='debtorItem', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    deadline = models.DateField(blank=True)
    info = models.CharField(max_length=280)
    image = models.ImageField(upload_to='pics', blank=True)
    isActive = models.BooleanField(default=True)
