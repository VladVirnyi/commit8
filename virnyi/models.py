from django.db import models
from django.utils import timezone
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class MenuCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(verbose_name="Опис категорії", blank=True)
    is_available = models.BooleanField(default=True, verbose_name="Доступна")
    display_order = models.IntegerField(default=0, verbose_name="Порядок відображення")

    class Meta:
        verbose_name = "Категорія меню"
        verbose_name_plural = "Категорії меню"
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    image = ProcessedImageField(
        upload_to='menu_items/',
        processors=[ResizeToFill(640, 480)],
        format='JPEG',
        options={'quality': 60},
        verbose_name="Зображення",
        blank=True,
        null=True
    )

    TEMPERATURE_CHOICES = [
        ('hot', 'Гарячий'),
        ('cold', 'Холодний'),
        ('both', 'Гарячий/Холодний'),
    ]

    SIZE_CHOICES = [
        ('S', 'Маленький (180 мл)'),
        ('M', 'Середній (250 мл)'),
        ('L', 'Великий (350 мл)'),
    ]


    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва позиції")
    description = models.TextField(verbose_name="Опис", help_text="Детальний опис складу та приготування")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базова ціна")
    is_available = models.BooleanField(default=True, verbose_name="Доступно до замовлення")
    temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURE_CHOICES,
        default='hot',
        verbose_name="Температура подачі"
    )
    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        default='M',
        verbose_name="Стандартний розмір"
    )
    ingredients = models.TextField(verbose_name="Інгредієнти", help_text="Перелік основних інгредієнтів")
    calories = models.IntegerField(default=0, verbose_name="Калорійність",
                                   help_text="Калорійність на стандартну порцію")
    preparation_time = models.IntegerField(
        default=5,
        verbose_name="Час приготування (хв)",
        help_text="Приблизний час приготування в хвилинах"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання в меню")
    is_special = models.BooleanField(default=False, verbose_name="Спеціальна пропозиція")

    class Meta:
        verbose_name = "Позиція меню"
        verbose_name_plural = "Позиції меню"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_size_display()})"

class Order(models.Model):
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name="Товар", default=1)
    customer_name = models.CharField(max_length=100, verbose_name="Ім'я замовника", blank=True, null=True)
    customer_phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    customer_email = models.EmailField(verbose_name="Email", blank=True, null=True)
    address = models.TextField(verbose_name="Адреса доставки")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення", blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="Примітки до замовлення")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення {self.id} - {self.customer_name}"

