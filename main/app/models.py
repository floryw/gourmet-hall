from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=200)




class MasterClass(models.Model):

    TYPE_CHOICES = (
        (1, "Онлайн"),
        (2, "Очная встреча"),
    )

    PAYTYPE_CHOICES = (
        (1, "банковская карта"),
        (2, "онлайн-перевод"),
    )

    STATUS_CHOICES = (
        (1, "Доступно"), # Скорее всего здесь опечатка (скопировано с PAYTYPE), но пока оставляю так же
        (2, "Нет в наличии"),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название курса')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.CharField(max_length=200, verbose_name='Описание')
    count = models.CharField(max_length=200)
    date_event = models.DateField(verbose_name='Дата события')
    type_event = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Формат')
    time_event = models.CharField(max_length=200, verbose_name='Длительность')
    price = models.CharField(max_length=200, verbose_name='Цена')
    paytype = models.IntegerField(choices=PAYTYPE_CHOICES, verbose_name='Способ оплаты')
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='Статус')



