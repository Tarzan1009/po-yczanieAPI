from django.conf import settings
from django.db import models
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user', unique=True, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


class DebtMonetary(models.Model):
    creditor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='creditorMon',
                                 on_delete=models.CASCADE)
    debtor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='debtorMon', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(default=date.today)
    isActive = models.BooleanField(default=True)


class DebtItem(models.Model):
    name = models.CharField(max_length=30)
    creditor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='creditorItem',
                                 on_delete=models.CASCADE)
    debtor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='debtorItem', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    deadline = models.DateField(blank=True)
    info = models.CharField(max_length=280)
    image = models.ImageField(upload_to='pics', blank=True)
    isActive = models.BooleanField(default=True)