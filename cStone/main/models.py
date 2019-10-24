from django.db import models


class Stone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, default='', unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, default='', unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Processing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, default='', unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stone = models.ForeignKey(Stone, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100)
    slug = models.SlugField(max_length=48, unique=True)
    length = models.DecimalField(verbose_name='Length[CM]', max_digits=4, decimal_places=1)
    width = models.DecimalField(verbose_name='Width[CM]', max_digits=4, decimal_places=1)
    thickness = models.DecimalField(verbose_name='Thickness[MM]', max_digits=3, decimal_places=1)
    stock_units = models.PositiveIntegerField(default=0)
    ordered = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    processing = models.ForeignKey(Processing, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price[NIS]', max_digits=6, decimal_places=1)
    image = models.ImageField(upload_to='products', null=True, blank=True,
                              default='logo-icon.png')
    description = models.TextField(default='')

    @property
    def total_space_m(self):
        return (self.length * self.width)/100

    def __str__(self):
        return self.name



