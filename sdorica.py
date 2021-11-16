from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import base64
from io import BytesIO

from random import choice
import random


# 加入抽卡背景
def background():
    img_bg = Image.new(mode="RGB", size=(1858, 886), color="green")
    bg = Image.open('sdorica/bg.jpg')
    img_bg.paste(bg)
    return img_bg


# 随机抽卡
def choose_img(num):
    path = "E:/QQbot/sdorica/{}".format(num)
    out_list = os.listdir(path)
    o = choice(out_list)
    name = str(o)[:-4]
    img = Image.open("sdorica/{}/{}".format(num, o))
    img = img.resize((157, 233))
    return [img, name]


# 计算文本位置
def name(x, y, name):
    tfont = ImageFont.truetype('E:/QQbot/sdorica/sdorica.otf', 23)
    width = tfont.getsize(name)[0]  # 获取文本宽度
    xx = x + (155 - width) / 2
    yy = y + 5
    return [xx, yy]


# 选择边框
def choose_frame(num):
    path = "E:/QQbot/sdorica/kuang"
    out_list = os.listdir(path)
    if num == 0:
        img = Image.open("sdorica/kuang/0k.png")
    elif num == 1:
        img = Image.open("sdorica/kuang/1k.png")
    elif num == 2:
        img = Image.open("sdorica/kuang/2k.png")
    elif num == 3:
        img = Image.open("sdorica/kuang/3k.png")
    return img


# 选择光效
def choose_Light(num):
    path = "E:/QQbot/sdorica/kuang"
    out_list = os.listdir(path)
    if num == 1:
        img = Image.open("sdorica/kuang/1g.png")
    elif num == 2:
        img = Image.open("sdorica/kuang/2g.png")
    elif num == 3:
        img = Image.open("sdorica/kuang/3g.png")
    return img


# 抽卡
def Draw_card():
    out_list = []
    bd = 0  # 十连保底蓝色
    for i in range(10):
        pro = random.randint(0, 1000)
        if bd != 9:
            if pro <= 20:
                out_list.append(3)
                bd += 1
            elif pro <= 50:
                out_list.append(2)
                bd += 1
            elif pro <= 240:
                out_list.append(1)
                bd = 0
            else:
                out_list.append(0)
                bd += 1
        else:
            if pro <= 20:
                out_list.append(3)
            elif pro <= 50:
                out_list.append(2)
            else:
                out_list.append(1)
            bd = 0
    return out_list


def shi_lian(ls):
    img_bg = background()
    xstar = 427;ystar = 144;
    x_ = 214;y_ = 283
    w = 0

    x0k_ = 26;y0k_ = 27
    x1k_ = 7;y1k_ = 3
    x2k_ = 9;y2k_ = 2
    x3k_ = 9;y3k_ = 5

    x1g_ = 46;y1g_ = 57
    x2g_ = 49;y2g_ = 80
    x3g_ = 50;y3g_ = 82

    x3t_ = 65;y3t_ = 101

    for i in ls:
        xp = 0
        wow = 0
        if i == 0:
            im, na = choose_img(0)
            k = choose_frame(0)
            xk = x0k_;yk = y0k_
        elif i == 1:
            im, na = choose_img(1)
            k = choose_frame(1)
            xk = x1k_;yk = y1k_
            g = choose_Light(1);xp = 1
            xg = x1g_;yg = y1g_
        elif i == 2:
            im, na = choose_img(2)
            k = choose_frame(2)
            xk = x2k_;yk = y2k_
            g = choose_Light(2);xp = 1
            xg = x2g_;yg = y2g_
        else:
            im, na = choose_img(3)
            k = choose_frame(3)
            xk = x3k_;yk = y3k_
            g = choose_Light(3);xp = 1;wow = 1
            xg = x3g_;yg = y3g_
            xt = x3t_;yt = y3t_
        if w == 5: xstar = 427;ystar += y_
        img_bg.paste(im, (xstar, ystar), mask=im)
        if xp == 1:
            img_bg.paste(g, (xstar - xg, ystar - yg), mask=g)
        if wow == 1:
            t = Image.open("sdorica/kuang/3t.png")
            img_bg.paste(t, (xstar - xt, ystar - yt), mask=t)
        img_bg.paste(k, (xstar - xk, ystar - yk), mask=k)
        tx, ty = name(xstar, ystar, na)
        draw = ImageDraw.Draw(img_bg)
        tfont = ImageFont.truetype('E:/QQbot/sdorica/sdorica.otf', 23)
        draw.text((tx, ty), na, fill='white', font=tfont)
        xstar += x_
        w += 1
    return img_bg


def pic2b64():
    # im是Image对象，把Image图片转成base64
    shi_lian(Draw_card())
    bio = BytesIO()
    shi_lian(Draw_card()).save(bio, format='PNG')
    base64_str = base64.b64encode(bio.getvalue()).decode()
    return 'base64://' + base64_str

# shi_lian(Draw_card()).show()
