from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    date_registration = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name = 'Название')
    desc = models.TextField(verbose_name = 'Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Цена')
    quantity = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Количество')
    date_add = models.DateField(auto_now_add=True, verbose_name = 'Дата создания')
    image = models.ImageField(verbose_name = 'Изображение товара',upload_to='products/', blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client} - {self.total_price}: {self.date_ordered}'