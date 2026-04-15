from citam_pydraw import *

@animation(True)
def draw():
    h = date.hour
    m = date.minute
    s = date.second
    print("{}:{}:{}".format(h, m, s))
    
    Line(300, 150, 300, 150)
    Line(300, 300, 300, 300)

    dial = Ellipse(150, 150, 290, 290)
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

    text3 = Text("12", 150,15)
    text4 = Text("1", 225,35)
    text5 = Text("2", 265,80)
    text6 = Text("3", 290,150)
    text7 = Text("4", 265,210)
    text8 = Text("5", 220,260)
    text9 = Text("6", 150,280)
    text10 = Text("7", 80,260)
    text11 = Text("8", 40,210)
    text12 = Text("9", 15,150)
    text13 = Text("10", 30,80)
    text14 = Text("11", 70,35)

if __name__ == "__main__":
    window = Window(300, 300).title("Clock").background(color(250,250,250))
    date = Date()
    pflag = True
    draw()
    window.show()

#python3.11 /Users/yokoyamatoshiki/code/clock.py