import datetime
from django.db import models
from django.utils import timezone

gender_choices = (
    (1, '男'),
    (2, '女'),
)

class User(models.Model):
    user_name = models.CharField('名前', max_length=255)
    gender = models.IntegerField('性別, choices=gender_choices')
    age = models.IntegerField('年齢', default=0)

    def __str__(self):
        return self.user_name


class Lesson(models.Model):
    lesson_name = models.CharField('授業', max_length=255)
    def __str__(self):
        return self.lesson_name

class Attend(models.Model):
    user = models.ForeignKey(User, verbose_name='顧客', on_delete=models.PROTECT)
    lesson = models.ForeignKey(Lesson, verbose_name='授業', on_delete=models.PROTECT)
    time = models.IntegerField('受講時間', default=0)
    attended = models.DateField('受講日', default=timezone.now)

class Invoice(models.Model):
    user = models.ForeignKey(User, verbose_name='顧客', on_delete=models.PROTECT)
    lesson_count = models.IntegerField('レッスン数')
    total = models.IntegerField('合計')

    def get_lesson_count(self):
        return Attend.objects.filter(lesson__attend=self).count()

class Price_plan(models.Model):
    lesson_name = models.ForeignKey(Lesson, verbose_name='授業', on_delete=models.PROTECT)
    charge = models.IntegerField('基本料金')
    basic_charge = models.IntegerField('従量料金')
    over_20h_basic_charge = models.IntegerField('20時間超過料金')
    over_35h_basic_charge = models.IntegerField('35時間超過料金')
    over_50h_basic_charge = models.IntegerField('50時間超過料金')
