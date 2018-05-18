# -*- coding: utf-8 -*-
from docxtpl import DocxTemplate
import re
import os

def transliterate(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',}

    capital_letters_transliterated_to_multiple_letters = {u'Ж': u'Zh',
                                                          u'Ц': u'Ts',
                                                          u'Ч': u'Ch',
                                                          u'Ш': u'Sh',
                                                          u'Щ': u'Sch',
                                                          u'Ю': u'Yu',
                                                          u'Я': u'Ya',}


    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'ё': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ъ': u'',
                       u'ы': u'y',
                       u'ь': u'',
                       u'э': u'e',
                       u'ю': u'yu',
                       u'я': u'ya',}

    for cyrillic_string, latin_string in capital_letters_transliterated_to_multiple_letters.items():
        string = re.sub(r"%s([а-я])" % cyrillic_string, r'%s\1' % latin_string, string)

    for dictionary in (capital_letters, lower_case_letters):

        for cyrillic_string, latin_string in dictionary.items():
            string = string.replace(cyrillic_string, latin_string)

    for cyrillic_string, latin_string in capital_letters_transliterated_to_multiple_letters.items():
        string = string.replace(cyrillic_string, latin_string.upper())

    return string



def generate(fname, sname, fathername, sex, spec, groupnum, experc, oksem, achlist):
    sourcePath = os.path.dirname(os.path.realpath(__file__))
    savePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    doc = DocxTemplate(sourcePath+"/SOURCE.docx")
    useperc = experc
    useachlist = achlist
    shortName = sname + ' ' + fname[0] + '.' + fathername[0] + '.'
    if sex == 'MALE':
        studSex = 'Студент'
        joinSex = 'поступил'
    elif sex == 'FEMALE':
        studSex = 'Студентка'
        joinSex = 'поступила'
    if oksem == 'ALL':
        semesters = 'На протяжении всего периода обучения'
    elif oksem == '1':
        semesters = 'Последний семестр'
    elif oksem == '2':
        semesters = 'Последние 2 семестра'
    elif oksem == '3':
        semesters = 'Последние 3 семестра'
    elif oksem == '4':
        semesters = 'Последние 4 семестра'
    elif oksem == '5':
        semesters = 'Последние 5 семестров'
    elif oksem == '6':
        semesters = 'Последние 6 семестров'
    elif oksem == '7':
        semesters = 'Последние 7 семестров'
    elif oksem == '8':
        semesters = 'Последние 8 семестров'
    if experc[-1] == '%':
        useperc = experc[:-1]
    if achlist[-1] == '.':
        useachlist = achlist[:-1]

    context = {'fullName' : sname+' '+fname+' '+fathername,
               'studSex' : studSex,
               'groupNum' : groupnum,
               'shortName' : shortName,
               'joinSex' : joinSex,
               'spec' : spec,
               'semesters' : semesters,
               'percentage' : useperc,
               'ach' : useachlist
    }
    doc.render(context)
    docName = 'Zayavka ot ' + transliterate(sname+' '+fname+' '+fathername+'.docx')
    print (str(savePath))

    doc.save(savePath+'/uploads/media/'+docName)
generate('Сев123а', 'Смирнов', 'Алексеевич', 'MALE', '123.123.123 Программирование', '666', '88', '4', 'Имеет орден за самый вырвиглазный код')
