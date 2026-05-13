from citam_pydraw import *
import math

def draw_hand(angle, length_scale):
    cx = 150
    cy = 150

    top_y = cy - int(110 * length_scale)
    mid_y = cy - int(20 * length_scale)
    bottom_y = cy + int(30 * length_scale)

    max_width = int(8 * length_scale)

    for y in range(top_y, bottom_y):
        if y < mid_y:
            # 上
            t = (y - top_y) / (mid_y - top_y)
            half_width = int(max_width * t)
        else:
            # 下
            t = (y - mid_y) / (bottom_y - mid_y)
            half_width = int(max_width * (1 - t))

        x1 = cx - half_width
        x2 = cx + half_width

        line = Line(x1, y, x2, y, 2)
        line.fill(color(47, 73, 110))
        line.setRotationCenter(cx, cy)
        line.rotate(angle)

    #外枠
    points = [
        (cx, top_y),
        (cx - max_width, mid_y),
        (cx, bottom_y),
        (cx + max_width, mid_y)
    ]

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]

        outline = Line(x1, y1, x2, y2, 3)
        outline.fill(color(47, 73, 110))
        outline.setRotationCenter(cx, cy)
        outline.rotate(angle)




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
    ratio = m / 60

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

    #3,6,9,12
    text12 = Text("12", 150, 20)
    text3 = Text("3", 280, 150)
    text6 = Text("6", 150, 280)
    text9 = Text("9", 20, 150)
    # 目盛り（上記以外）
    for i in range(1, 12):
        if i == 3 or i == 6 or i == 9:
            continue

        tick = Line(150, 20, 150, 40, 2)
        tick.setRotationCenter(150, 150)
        tick.rotate(i * 360 / 12)

    draw_hand(h * 30, 0.6)   # 短針
    draw_hand(m * 6, 1.0)    # 長針

    #秒針
    byo = Line(150, 150, 150, 20, 2)
    byo.fill(color(237, 140, 114))
    byo.setRotationCenter(150, 150)
    byo.rotate(s*360/60)

    

    

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
    window = Window(300, 300).title("Clock").background(color(244,234,222))
    date = Date()
    player = loadMusic("water.mp3")
    pflag = True
    draw()
    window.show()

#python3.11 /Users/yokoyamatoshiki/code/clock.py