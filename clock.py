from citam_pydraw import *
import math

alarm_time = input("アラーム時刻(HH:MM): ")

ALARM_HOUR = int(alarm_time.split(":")[0])
ALARM_MINUTE = int(alarm_time.split(":")[1])

alarm_triggered = False
alarm_start_second = 0

date = Date()

START_TIME = (
    date.hour * 3600
    + date.minute * 60
    + date.second
)

CLOCK_X = 200
CLOCK_Y = 200
CLOCK_R = 180

def draw_hand(angle, length_scale):
    cx = CLOCK_X
    cy = CLOCK_Y

    bottom_y = cy
    mid_y = cy - int(35 * length_scale)
    top_y = cy - int(180 * length_scale)

    max_width = int(8 * length_scale)

    for y in range(top_y, bottom_y):
        if y < mid_y:
            t = (y - top_y) / (mid_y - top_y)
            half_width = int(max_width * t)
        else:
            t = (y - mid_y) / (bottom_y - mid_y)
            half_width = int(max_width * (1 - t))

        x1 = cx - half_width
        x2 = cx + half_width

        line = Line(x1, y, x2, y, 2)
        line.fill(color(47, 73, 110))
        line.setRotationCenter(cx, cy)
        line.rotate(angle)

    points = [
        (cx, top_y),
        (cx - max_width, mid_y),
        (cx, bottom_y),
        (cx + max_width, mid_y)
    ]

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        outline = Line(x1, y1, x2, y2, 3)
        outline.fill(color(47, 73, 110))
        outline.setRotationCenter(cx, cy)
        outline.rotate(angle)


@animation(True)
def draw():
    global alarm_triggered
    global alarm_start_second

    h = date.hour
    m = date.minute
    s = date.second

    print("{}:{}:{}".format(h, m, s))

    Line(400, 200, 400, 200)
    Line(400, 400, 400, 400)

    now = h * 60 + m
    alarm = ALARM_HOUR * 60 + ALARM_MINUTE

    if now == alarm - 1:
        if int(date.milli_second / 200) % 2 == 0:
            water_color = color(250, 128, 114)
        else:
            water_color = color(255, 220, 100)
    elif alarm - 3 <= now < alarm - 1:
        water_color = color(250, 128, 114)
    elif alarm - 10 <= now < alarm - 3:
        water_color = color(255, 220, 100)
    else:
        water_color = color(120, 200, 255)

    # 水

    water_top = 0
    water_bottom = 400
    water_height = water_bottom - water_top

    now_seconds = h * 3600 + m * 60 + s
    alarm_seconds = ALARM_HOUR * 3600 + ALARM_MINUTE * 60

    total_time = alarm_seconds - START_TIME

    if total_time <= 0:
        total_time += 24 * 3600

    elapsed_time = now_seconds - START_TIME

    if elapsed_time < 0:
        elapsed_time += 24 * 3600

    # アラーム到達
    if now_seconds >= alarm_seconds and not alarm_triggered:
        alarm_triggered = True
        alarm_start_second = now_seconds

    # アラーム前
    if not alarm_triggered:

        ratio = elapsed_time / total_time

        if ratio > 1:
            ratio = 1

    # アラーム後
    else:

        if now_seconds - alarm_start_second < 6:
            ratio = 1.0
        else:
            ratio = 0.0

    base_y = water_bottom - water_height * ratio

    for x in range(0, 400, 2):

        water_line = Line(
            x,
            base_y,
            x,
            water_bottom,
            2
        )

        water_line.fill(water_color)
    # 時計外枠
    dial = Ellipse(CLOCK_X, CLOCK_Y, CLOCK_R * 2, CLOCK_R * 2)
    dial.noFill()
    dial.outlineFill(color(0, 0, 0))


    # 数字
    Text("12", CLOCK_X, 30)
    Text("3", CLOCK_X + 170, CLOCK_Y)
    Text("6", CLOCK_X, 370)
    Text("9", CLOCK_X - 170, CLOCK_Y)

    # アラーム表示
    alarm_text = Text(
        "ALARM {:02d}:{:02d}".format(
            ALARM_HOUR,
            ALARM_MINUTE
        ),
        320,
        390
    )


    # 5分ごとの目盛り
    for i in range(1, 12):
        if i == 3 or i == 6 or i == 9:
            continue

        tick = Line(CLOCK_X, 20, CLOCK_X, 50, 2)
        tick.setRotationCenter(CLOCK_X, CLOCK_Y)
        tick.rotate(i * 360 / 12)

    # 1分ごとの目盛り
    for i in range(60):

        if i % 5 == 0:
            continue

        small_tick = Line(CLOCK_X, 30, CLOCK_X, 42, 1)

        small_tick.fill(color(120, 120, 120))

        small_tick.setRotationCenter(CLOCK_X, CLOCK_Y)
        small_tick.rotate(i * 6)

    # 短針
    draw_hand((h + m / 60 + s / 3600) * 30, 0.6)

    # 長針
    draw_hand((m + s / 60) * 6, 1.0)

    # 秒針
    byo = Line(CLOCK_X, CLOCK_Y, CLOCK_X, 30, 2)
    byo.fill(color(237, 140, 114))
    byo.setRotationCenter(CLOCK_X, CLOCK_Y)
    byo.rotate(s * 6)


if __name__ == "__main__":
    window = Window(400, 400).title("Clock").background(color(244, 234, 222))
    draw()
    window.show()

#python3.11 /Users/yokoyamatoshiki/code/clock.py