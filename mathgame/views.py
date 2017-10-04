# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint, choice
import PIL.Image
import PIL.ImageDraw
from PIL import ImageFont
from random import sample
from string import ascii_letters, digits

from django.shortcuts import render

def compare(request):
    first = randint(0, 20)
    second = randint(0, 20)

    z = request.GET
    if len(z) != 0:
        i = int(z['answer']) + 1
    else:
        i = 1
    url = 'http://127.0.0.1:8000/?answer=' + str(i)

    if first > second:
        answern = 'First is greater'
    elif first < second:
        answern = 'Second is greater'
    else:
        answern = 'The numbers are equal'

    v1 = randint(0, 20)
    v2 = randint(0, 20)
    v3 = randint(0, 20)
    v4 = randint(0, 20)
    actions = ['+', '-', '*', '/']
    a1 = choice(actions)
    a2 = choice(actions)

    if a1 == '+':
        f_result = v1 + v2
        f_res = str(v1) + '+' + str(v2)
    elif a1 == '-':
        f_result = v1 - v2
        f_res = str(v1) + '-' + str(v2)
    elif a1 == '*':
        f_result = v1 * v2
        f_res = str(v1) + '*' + str(v2)
    elif a1 == '/':
        while v2 == 0:
            v2 = randint(0, 20)
        f_result = v1 / v2
        f_res = str(v1) + '/' + str(v2)

    if a2 == '+':
        s_result = v3 + v4
        s_res = str(v3) + '+' + str(v4)
    elif a2 == '-':
        s_result = v3 - v4
        s_res = str(v3) + '-' + str(v4)
    elif a2 == '*':
        s_result = v3 * v4
        s_res = str(v3) + '*' + str(v4)
    elif a2 == '/':
        while v4 == 0:
            v4 = randint(0, 20)
        s_result = v3 / v4
        s_res = str(v3) + '/' + str(v4)

    if f_result > s_result:
        c = '>'
        answera = str(v1) + a1 + str(v2) + 'greather than' + str(v3) + a2 + str(v4)
    elif f_result < s_result:
        c = '<'
        answera = str(v1) + a1 + str(v2) + 'less than' + str(v3) + a2 + str(v4)
    else:
        c = '='
        answera = str(v1) + a1 + str(v2) + 'equals' + str(v3) + a2 + str(v4)

    font = ImageFont.truetype('mathgame/static/Ubuntu-Regular.ttf', 50)
    new = PIL.Image.new('RGB', (200, 200), (50, 50, 50))
    draw = PIL.ImageDraw.Draw(new, 'RGB')
    draw.text((20, 100), str(first) + 'or' + str(second) + '?', font=font)
    namelen = randint(4,20)
    nameinlist = sample(ascii_letters+digits, namelen)
    name = ''
    for i in nameinlist:
        name +=i
    fullname = name+'.jpeg'
    new.save('mathgame/static/' + fullname)

    return render(request, 'mathgame/compare.html', {'first': first, 'second': second, 'url': url, 'answern': answern, \
                                                     'f_res': f_res, 's_res': s_res, 'answera': answera, \
                                                     'fullname': fullname})