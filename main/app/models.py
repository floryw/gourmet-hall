from django.db import models
from django.contrib.auth.models import User

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')

class Category(models.Model):
    category = models.CharField(max_length=200, verbose_name='Категория')


class CardFood(models.Model):

    STATUS_CHOICES = {
    1: "Доступно",
    2 : "Нет в наличии",}

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(verbose_name='Фото')
    name = models.CharField(max_length=200, verbose_name='Название блюда')
    description = models.CharField(max_length=200, verbose_name='Описание')
    weight = models.CharField(max_length=200, verbose_name='Вес')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='Статус')


class Order(models.Model):
    
    STATUS_CHOICES = {
    1: "Новый",
    2 : "Подтвержден",
    3 : "Готовится",
    4 : "Готов к выдаче",
    5 : "Передан курьеру",
    6 : "Доставлен",
    7 : "Отменен",
    }


    RECEIVING_TYPE_CHOICES = {
    1: "Доставка",
    2 : "Самовывоз",
    }

    PAYTYPE_CHOICES = {
    1: "Наличные",
    2 : "Оплата курьеру",
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='Статус')
    receiving = models.IntegerField(choices=RECEIVING_TYPE_CHOICES, verbose_name='Тип доставки')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    description = models.CharField(max_length=200, verbose_name='Описание')
    pay_type = models.IntegerField(choices=PAYTYPE_CHOICES, verbose_name='Тип оплаты')
    date = models.DateTimeField(verbose_name='Дата заказа')
    adress = models.CharField(max_length=200, blank=True, verbose_name='Адрес')
    finalprice = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена')


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    CardFood = models.ForeignKey(CardFood, on_delete=models.CASCADE, verbose_name='Товар')
    CardFoodCount = models.IntegerField()


class reservation(models.Model):


    STATUS_CHOICES = {
    1: "Ожидает подтверждения",
    2: "Подтверждена",
    3 : "Отклонена",
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Статус')
    date = models.DateTimeField(verbose_name='Дата брони')
    personcount = models.IntegerField(verbose_name='Кол-во персон')



