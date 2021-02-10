from django.db import models

class Chess_post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикции')
    content = models.TextField(max_length=100000)

class News_post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикции')
    content = models.TextField(max_length=100000)

class Lib_post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикции')
    content = models.TextField(max_length=100000)

class Media_post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикции')
    content = models.TextField(max_length=100000)

class Guest_post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикции')
    content = models.TextField(max_length=100000)