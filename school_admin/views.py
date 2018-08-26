from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, reverse
from .models import Lesson, User, Attend, Price_plan, Invoice
from .forms import UserForm, AttendForm

# トップページ
def index(request):
    return render(request, 'school_admin/index.html')

# レッスン受講記録
def attend(request):
    context = {
        'attend_list': Attend.objects.all(),
    }
    return render(request, 'school_admin/attend.html', context)

# レッスン受講登録
def add_attend(request):
    form = AttendForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('school_admin:attend')
    context = {
        'form': form,
    }
    return render(request, 'school_admin/add_attend.html', context)

# レッスン更新
def update_attend(request, pk):
    attend = get_object_or_404(Attend, pk=pk)
    form = AttendForm(request.POST or None, instance=attend)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('school_admin:attend')
    context = {
        'form': form
    }
    return render(request, 'school_admin/add_attend.html', context)

# ユーザ一覧画面
def user(request):
    context = {
        'user_list': User.objects.all(),
    }
    return render(request, 'school_admin/user.html', context)

# 新規ユーザー登録画面
def add_user(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('school_admin:users')

    context = {
        'form': form
    }
    return render(request, 'school_admin/add_userForms.html', context)

# ユーザー編集
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('school_admin:user')
    context = {
        'form': form
    }
    return render(request, 'school_admin/add_user.html', context)

# 月別請求一覧画面
def invoice_list(request):
    invoice_list = Attend.objects.all()
    context = {
        'invoice_list': invoice_list,
    }
    return render(request, 'school_admin/invoice_list.html', context)

# レポート画面
def report(request):
    report_list = Attend.objects.all()
    context = {
        'report_list': report_list.all()
    }
    return render(request, 'school_admin/report.html', context)
