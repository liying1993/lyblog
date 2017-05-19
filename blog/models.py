# -*-:coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=128,db_index=True)
    content = models.TextField()

class Comment(models.Model):
    comcontent = models.CharField(max_length=512)

class Answer(models.Model):
    anscontent = models.CharField(max_length=512)

class Lovers(models.Model):
    pass
class Collect(models.Model):
    pass
class UserInfo(models.Model):
    ROLETYPE = ((u'1',u'游客'),(u'2',u'作者'))
    role = models.CharField(max_length=8,choices=ROLETYPE,default=u'1')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    article = models.ForeignKey(Article)
    comment = models.ForeignKey(Comment)
    answer = models.ForeignKey(Answer)
    lovers = models.ManyToManyField(Lovers)
    collect = models.ManyToManyField(Collect)

class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s(%s)"%(self.name,self.url)

class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList,null=True,blank=True)

    def __unicode__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(email,
            username = username,
            password = password,
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40,unique=True,db_index=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64,null=True)
    sex = models.CharField(max_length=2,null=True)
    role = models.ForeignKey(RoleList,null=True,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def has_perm(self,perm,obj=None):
        if self.is_active and self.is_superuser:
            return True

