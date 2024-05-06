import django
import os

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

# Настройте Django
django.setup()

# Импортируйте модель пользователя
from django.contrib.auth.models import User

# Создание суперпользователя
user = User.objects.create_superuser(username='admin', password='admin')

# Сохранение пользователя
user.save()
