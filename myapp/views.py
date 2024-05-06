from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess

@login_required  # Применяем декоратор login_required
def index(request):
    return render(request, 'index.html')

@login_required  # Применяем декоратор login_required
def prompts(request):
    return render(request, 'prompts.html')

@login_required
def new_data(request):
    if request.method == 'POST':
        data1 = request.POST.get('data1', '')
        data2 = request.POST.get('data2', '')
        data3 = request.POST.get('data3', '')
        data4 = request.POST.get('data4', '')
        data5 = request.POST.get('data5', '')
        data6 = request.POST.get('data6', '')
        data7 = request.POST.get('data7', '')
        data8 = request.POST.get('data8', '')
        data9 = request.POST.get('data9', '')
        data10 = request.POST.get('data10', '')
        data11 = request.POST.get('data11', '')
        data12 = request.POST.get('data12', '')
        data13 = request.POST.get('data13', '')
        data14 = request.POST.get('data14', '')
        data15 = request.POST.get('data15', '')
        data16 = request.POST.get('data16', '')
        data17 = request.POST.get('data17', '')

        # Создаем папку с названием из data9, если она еще не существует
        data9_folder = os.path.join(os.getcwd(), data9)
        target_folder = os.path.join(data9_folder, 'static')
        os.makedirs(target_folder, exist_ok=True)

        # Сохраняем путь к папке в файл
        with open('path.txt', 'w') as f:
            f.write(data9_folder)

        # Сохраняем данные в файл
        file_path = os.path.join(target_folder, 'data.txt')
        with open(file_path, 'a') as file:
            file.write(f"{data1}\n")
            file.write(f"{data2}\n")
            file.write(f"{data3}\n")
            file.write(f"{data4}\n")
            file.write(f"{data5}\n")
            file.write(f"{data6}\n")
            file.write(f"{data7}\n")
            file.write(f"{data8}\n")
            file.write(f"{data9}\n")
            file.write(f"{data10}\n")
            file.write(f"{data11}\n")
            file.write(f"{data12}\n")
            file.write(f"{data13}\n")
            file.write(f"{data14}\n")
            file.write(f"{data15}\n")
            file.write(f"{data16}\n")
            file.write(f"{data17}\n")

        subprocess.run(["python", "data_to_text.py"])
        subprocess.run(["python", "filler.py"])

        # Возвращаем пустой ответ, если данные успешно сохранены
        return redirect('index')
    else:
        return render(request, 'new_data.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Дополнительная логика аутентификации
            # Возвращаем успешное сообщение или перенаправляем пользователя на другую страницу
            return redirect('index')  # Перенаправляем на главную страницу
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_redirect(request):
    return redirect('login')
