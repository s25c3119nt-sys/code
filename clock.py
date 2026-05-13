from citam_pydraw import *
import math

@animation(True)
def draw():
    h = date.hour
    m = date.minute
    s = date.second
    print("{}:{}:{}".format(h, m, s))
    
    Line(300, 150, 300, 150)
    Line(300, 300, 300, 300)

    # 水
    t = date.second + date.milli_second / 1000
    ratio = s / 60

    cx = 150
    cy = 150
    r = 140

    base_y = cy + r - (2 * r * ratio)

    for x in range(10, 290, 2):
        dx = x - cx

        if dx*dx > r*r:
            continue

        # 円の上下
        circle_top = cy - math.sqrt(r*r - dx*dx)
        circle_bottom = cy + math.sqrt(r*r - dx*dx)

        # 波
        wave = math.sin(t * 2 + x * 0.04) * 3
        y = base_y + wave

        # 上も下も円の中に制限
        if y < circle_top:
            y = circle_top
        if y > circle_bottom:
            y = circle_bottom

        water_line = Line(x, y, x, circle_bottom, 2)
        water_line.fill(color(120, 200, 255))

    #外枠
    dial = Ellipse(150, 150, 280, 280)
    dial.noFill()
    dial.outlineFill(color(0, 0, 0))

    #短針
    min = Line(150, 150, 150, 10, 4)
    min.fill(color(0, 0, 0))
    min.setRotationCenter(150, 150)
    min.rotate(m*360/60)

    #長針
    hou = Line(150, 150, 150, 50, 6)
    hou.fill(color(0, 0, 0))
    hou.setRotationCenter(150, 150)
    hou.rotate(h*360/12)

    #秒針
    byo = Line(150, 150, 150, 10, 2)
    byo.fill(color(0, 0, 0))
    byo.setRotationCenter(150, 150)
    byo.rotate(s*360/60)

    text12 = Text("12", 150, 20)
    text3 = Text("3", 280, 150)
    text6 = Text("6", 150, 280)
    text9 = Text("9", 20, 150)

    # 目盛り（1〜11）
    for i in range(1, 12):
        if i == 3 or i == 6 or i == 9:
            continue

        tick = Line(150, 20, 150, 40, 2)
        tick.setRotationCenter(150, 150)
        tick.rotate(i * 360 / 12)

    global pflag
    s = date.second
    #時報（1分毎に音を鳴らす）
    if (int(s)%60 == 0) and pflag:#秒の値が0になった時という条件と最初の再生という条件
        player.play()#音源ファイルを再生する
        pflag = False #毎0秒で1回だけ再生する
        #↑0秒だけど2回目以降はpflagがFalseになるので条件を満たさないから再生されない
    elif (int(s)%60 != 0) and not pflag: 
        pflag = True

if __name__ == "__main__":
    window = Window(300, 300).title("Clock").background(color(250,250,250))
    date = Date()
    player = loadMusic("water.mp3")
    pflag = True
    draw()
    window.show()

#python3.11 /Users/yokoyamatoshiki/code/clock.py