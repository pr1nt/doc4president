# -*- coding: utf-8 -*-
from django import forms
from multiupload.fields import MultiFileField
from .models import Record, Attachment


SEX = (
    ('MALE', u'Мужской'),
    ('FEMALE', u'Женский'),
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


class FIOForms(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'father_name', 'sex', 'groupNum', 'specialization', 'excellentPercent', 'ok_semesters', 'achievementsList']  # not attachments!

    first_name = forms.CharField(
        max_length=30,
        label=u'Имя'
    )
    last_name = forms.CharField(
        max_length=30,
        label=u'Фамилия'
    )
    father_name = forms.CharField(
        max_length=30,
        label=u'Отчество'
    )
    sex = forms.ChoiceField(
        choices=SEX,
        widget=forms.RadioSelect(),
        label=u'Пол'
    )
    groupNum = forms.CharField(
        max_length=3,
        help_text=u'Например, если ваша группа КЭ-303, введите 303',
        label=u'Номер группы'
    )
    specialization = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'cols': '40', 'rows': '5'}),
        help_text=u'Пример "010400.62 Прикладная математика и информатика <br /> факультета Вычислительной математики и информатики"',
        label=u'Код и специальность'
    )

    excellentPercent = forms.CharField(
        max_length=3,
        label=u'Процент оценок "Отлично"'
    )
    ok_semesters = forms.ChoiceField(
        choices=OK_SEMESTERS,
        label=u'Семестры на "Хорошо"',
        help_text=u'Колличество семестров подряд, в которых получены оценки не менее "Хорошо"'
    )
    achievementsList = forms.CharField(
        max_length=3000,
        widget=forms.Textarea(attrs={'cols': '70', 'rows': '9'}),
        label=u'Список достижений',
        help_text=u'Пример "Имеет диплом II степени за победу в заключительном туре <br /> Открытой международной студенческой Интернет – олимпиады по дисциплине <br /> «Экономика» профиль «Техника и технологии» (Йошкар-Ола,2013)." <br /> и далее через запятую'
    )


    files = MultiFileField(
        min_num=1, max_num=3,
        max_file_size=1024*1024*5,
        label=u'Загрузите файлы'
    )

    def save(self, commit=True):
        instance = super(FIOForms, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, message=instance)

        return instance

    '''def clean(self):
        cleaned_data = super(FIOForms, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')'''