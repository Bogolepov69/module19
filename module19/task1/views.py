from django import forms
from django.shortcuts import render, redirect
from .models import Buyer, Game


# Create your views here.
def main(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'main.html', context)


def basket(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'basket.html', context)


def shop(request):
    title = 'Магазин'
    games = Game.objects.all()

    context = {
        'title': title,
        'games': games
    }
    return render(request, 'shop.html', context)

class UserRegister(forms.Form):
    username = forms.CharField(label="Введите логин", max_length=30)
    password = forms.CharField(label="Введите пароль", min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Повторите пароль", min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(label="Введите свой возраст", max_value=150, min_value=0)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            buyer_exists = Buyer.objects.filter(username=username).exists()
            if password == repeat_password and age >= 18 and not buyer_exists:
                Buyer.objects.create(username=username, password=password, age=age)
                info['message'] = f"Приветствуем, {username}!"
                return redirect('register')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                else:
                    info['error'] = 'Пользователь уже существует'
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)

def sign_up_by_django(request):
    info = {}
    # Убираем лишние данные, теперь информация будет из БД
    return render(request, 'registration_page.html', info)

