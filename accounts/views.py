from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # Kiểm tra nếu người dùng là admin
                return redirect(reverse('admin:index'))  # Chuyển hướng đến trang admin
            else:
                return redirect('home')  # Chuyển hướng đến trang chủ nếu không phải admin
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
    
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')