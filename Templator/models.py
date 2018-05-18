# -*- coding: utf-8 -*-

import os
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

class Record(models.Model):
    SEX = (
        ('MALE', u'Мужской'),
        ('FEMALE', u'Женский')
    )
    OK_SEMESTERS = (
        ('ALL', u'Все семестры'),
        ('1', u'1 семестр'),
        ('2', u'2 семестра'),
        ('3', u'3 семестра'),
        ('4', u'4 семестра'),
        ('5', u'5 семестров'),
        ('6', u'6 семестров'),
        ('7', u'7 семестров'),
        ('8', u'8 семестров'),
    )
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    father_name = models.CharField(
        max_length=30
    )
    sex = models.CharField(
        max_length=6,
        choices=SEX,
    )
    groupNum = models.CharField(
        max_length=3
    )
    specialization = models.CharField(
        max_length=500
    )
    excellentPercent = models.CharField(
        max_length=3
    )
    ok_semesters = models.CharField(
        max_length=3,
        choices=OK_SEMESTERS
    )
    achievementsList = models.CharField(
        max_length=3000
    )

    '''def send(self):
        self.send_date = timezone.now()
        self.save()'''

    def __str__(self):
        return self.first_name


class Attachment(models.Model):
    dirname = datetime.now().strftime(u'%Y.%m.%d %H.%M.%S') #2010.08.09.12.08.45
    message = models.ForeignKey(Record, verbose_name=_('Message'), on_delete=models.CASCADE)
    realPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    os.mkdir(realPath + '/uploads/media/' + dirname)

    file = models.FileField(_('Attachment'), upload_to=realPath + '/uploads/media/' + dirname)

