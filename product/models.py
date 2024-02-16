from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



RANTING_CHOICE = {
        'FROM 6 TO 24 HOURS': 'От 6 до 24 часов',
        'FROM 1 TO 7 DAYS': 'От 1 до 7 дней',
        'FROM 1 WEEK TO MONTH': 'От 1 недели до месяца'
    }


class Auto(models.Model):
    
    TYPE_OF_BODY_CHOICES = {
        'SEDAN': 'Седан',
        'HATCHBACK': 'Хетчбек',
        'UNIVERSAL': 'Универсал',
        'CROSSOVER': 'Кроссовер',
        'SUV': 'Внедорожник',
        'CABRIOLET': 'Кабриолет'
    }

    TRANSMISSION_CHOICES = {
        'MECHANICS': 'Механика',
        'AUTOMAT': 'Автомат'
    }

    WHEEL_CHOICES = {
        'LEFT': 'Левый',
        'RIGTH': 'Правый',
    }

    COLOR_CHOICES = {
        'BLACK': 'Черный',
        'WHITE': 'Белый',
        'BROWN': 'Коричневый',
        'SILVER': 'Серебристый',
        'GREEN': 'Зеленый',
        'RED': 'Красный',
        'YELLOW': 'Желтый'
    }

    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    mark = models.CharField(verbose_name='Марка', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    type_of_body = models.CharField(verbose_name='Тип кузова', max_length=15, choices=TYPE_OF_BODY_CHOICES, null=True)
    transmission = models.CharField(verbose_name='Коробка передач', max_length=15, choices=TRANSMISSION_CHOICES, null=True)
    wheel = models.CharField(verbose_name = 'Руль', max_length=10, choices=WHEEL_CHOICES, null=True)
    color = models.CharField(verbose_name='Цвет', max_length=50, choices=COLOR_CHOICES, null=True)
    photo = models.ImageField(upload_to='auto_photos/', null=True, blank=True)
    location = models.CharField(verbose_name='локация', max_length=100, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    ranting = models.CharField(verbose_name='аренда', max_length=60, choices=RANTING_CHOICE, null=True)
    body = models.TextField(verbose_name='СОДЕРЖИМОЕ', null=True)
    number = models.CharField(verbose_name='Номер телефона', null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.mark}, {self.model}, {self.price}'
    

# class House(models.Model):

#     NUMBER_OF_ROOMS = {
#         '1 ROOM': '1 КОМНАТА',
#         '2 ROOMS': '2 КОМНАТЫ',
#         '3 ROOMS': '3 КОМНАТЫ',
#         '4 ROOMS': '4 КОМНАТЫ',
#         '5 ROOMS': '5 КОМНАТЫ',
#     }

#     TYPE_OF_HOUSE_CHOICES = {
#         'APPARTMENT': 'КВАРТИРА',
#         'COMMERCIAL ESTATE': 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ',
#         'PRIVATE HOUSE': 'ЧАСТНЫЙ ДОМ'
#     }

#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     estate = models.CharField(verbose_name='Недвижимость', max_length=100, choices=TYPE_OF_HOUSE_CHOICES, null=True)
#     floor = models.IntegerField(verbose_name='Этаж', validators=[MinValueValidator(1), MaxValueValidator(15)])
#     number_of_rooms = models.CharField(verbose_name='Количество комнат',max_length=100, choices=NUMBER_OF_ROOMS)
#     photo = models.ImageField(upload_to='house_photos/', null=True, blank=True)
#     location = models.CharField(verbose_name='Локация', max_length=100)
#     price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
#     ranting = models.CharField(verbose_name='аренда', max_length=60, choices=RANTING_CHOICE, null=True)
#     body = models.TextField(verbose_name='СОДЕРЖИМОЕ')
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.estate}, {self.location}'