# 入力フォーム
from django import forms
from .models import User, Lesson, Attend, Invoice
import datetime



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class AttendForm(forms.ModelForm):

    class Meta:
        model = Attend
        fields = '__all__'
