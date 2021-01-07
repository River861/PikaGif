import turtle


class Pikachu(object):

    def __init__(self):
        self.__t = turtle.Turtle()
        self.__t.speed(9)

    def __goto(self, x, y, toward_angle):
        """无痕迹移动光标
        """
        self.__t.penup()
        self.__t.goto(x - 200, 200 - y)  # 映射到中点坐标系
        self.__t.pendown()
        self.__t.seth(toward_angle)

    def __drawto(self, x, y, toward_angle):
        """有痕迹移动光标
        """
        self.__t.goto(x - 200, 200 - y)  # 映射到中点坐标系
        self.__t.seth(toward_angle)

    def __wall(self, pen_size):
        self.__t.pensize(pen_size)
        self.__goto(275, 0, -90)
        self.__t.forward(241)
        self.__goto(275, 275, -90)
        self.__t.forward(125)

    def __head(self, pen_size):
        self.__t.fillcolor('#ffee91')
        self.__t.begin_fill()
        self.__t.pensize(pen_size)
        self.__goto(274, 54, 180)  # 额头
        self.__t.circle(80, 52)
        self.__goto(216, 76, 150)  # 耳朵
        self.__t.circle(200, 40)
        self.__goto(80, 55, -60)
        self.__t.circle(130, 60)
        self.__goto(200, 114, -120)  # 脸颊
        self.__t.circle(60, 6)
        self.__goto(196, 121, -93)
        self.__t.circle(200, 13)
        self.__goto(198, 162, -93)
        self.__t.circle(60, 15)
        self.__goto(199, 180, -100)
        self.__t.circle(35, 85)
        self.__goto(224, 219, -20)
        self.__t.circle(120, 11)
        self.__goto(248, 224, 0)  # 下巴
        self.__t.forward(25)
        self.__goto(274, 223, 90)  # 墙沿
        self.__t.forward(170)
        self.__t.end_fill()

    def __hand(self, arm_size, hand_size):
        self.__t.fillcolor('#ffee91')
        self.__t.begin_fill()
        self.__t.pensize(arm_size)
        self.__goto(237, 223, -89)  # 肩膀
        self.__t.circle(100, 20)
        self.__goto(241, 251, -70)  # 手肘
        self.__t.circle(35, 80)
        self.__goto(275, 275, 5)  # 手腕
        self.__t.circle(105, 10)
        self.__t.pensize(hand_size)  # 手指
        self.__goto(297, 272, 100)
        self.__drawto(291, 267, 10)
        self.__drawto(297, 260, 120)
        self.__t.pensize(arm_size)  # 手背
        self.__drawto(274, 244, 90)
        self.__t.forward(20)  # 墙沿
        self.__drawto(251, 224, 180)
        self.__drawto(237, 223, 180)
        self.__t.end_fill()

    def __body(self, pen_size):
        self.__t.fillcolor('#ffee91')
        self.__t.begin_fill()
        self.__t.pensize(pen_size)
        self.__goto(240, 250, -95)  # 背
        self.__t.circle(-200, 20)
        self.__goto(222, 316, -100)  # 屁股
        self.__t.circle(130, 6)
        self.__goto(220, 330, -90)
        self.__t.forward(10)
        self.__t.circle(25, 65)  # 膝盖
        self.__goto(238, 365, -5)
        self.__t.circle(160, 12)
        self.__goto(274, 366, 90)  # 墙沿
        self.__t.forward(88)
        self.__goto(274, 274, 180)  # 手肘
        self.__t.circle(-35, 85)
        self.__t.end_fill()

    def __feet(self, foot_size, toe_size):
        self.__t.fillcolor('#ffee91')
        self.__t.begin_fill()
        self.__t.pensize(foot_size)
        self.__goto(231, 365, -160)  # 脚背
        self.__t.circle(85, 25)
        self.__t.pensize(toe_size)  # 脚趾
        self.__goto(197, 387, 10)
        self.__drawto(217, 384, -95)
        self.__drawto(217, 390, 5)
        self.__t.pensize(foot_size)  # 脚掌
        self.__t.circle(80, 40)
        self.__goto(263, 367, 180)  # 膝盖
        self.__t.circle(-160, 10)
        self.__t.circle(-25, 10)
        self.__t.end_fill()

    def __tail(self, pen_size):
        self.__t.fillcolor('#ffee91')
        self.__t.begin_fill()
        self.__t.pensize(pen_size)
        self.__goto(225, 310, 100)
        self.__drawto(194, 254, -150)
        self.__drawto(170, 277, 110)
        self.__drawto(132, 201, -130)
        self.__drawto(66, 255, -75)
        self.__drawto(88, 331, 60)
        self.__drawto(128, 276, -60)
        self.__drawto(158, 318, 60)
        self.__drawto(189, 290, -60)
        self.__drawto(220, 315, 80)
        self.__drawto(225, 310, 80)
        self.__t.end_fill()

    def __ear(self, pen_size):
        self.__t.pensize(pen_size)
        self.__t.fillcolor('black')
        self.__goto(131, 53, -60)
        self.__t.begin_fill()
        self.__t.circle(-75, 45)
        self.__goto(140, 108, 160)
        self.__t.circle(-120, 38)
        self.__goto(81, 60, 95)  # 耳尖
        self.__t.circle(-8, 60)
        self.__goto(82, 54, 10)
        self.__t.circle(-200, 15)
        self.__t.end_fill()

    def __eye(self, pen_size):
        self.__t.pensize(pen_size)
        self.__t.fillcolor('black')  # 眼黑
        self.__goto(218, 133, 60)
        self.__t.begin_fill()
        self.__t.circle(-8, 110)
        self.__goto(231, 133, -76)
        self.__t.circle(-45, 27)
        self.__goto(230, 154, -105)
        self.__t.circle(-8, 152)
        self.__goto(213, 153, 92)
        self.__t.circle(-45, 29)
        self.__t.end_fill()
        self.__t.fillcolor('white')  # 眼白
        self.__t.pencolor('white')
        self.__goto(224, 138, 60)
        self.__t.begin_fill()
        self.__t.circle(-4, 90)
        self.__goto(229, 138, -76)
        self.__t.circle(-22, 27)
        self.__goto(229, 148, -105)
        self.__t.circle(-4, 130)
        self.__goto(222, 148, 92)
        self.__t.circle(-22, 29)
        self.__t.end_fill()
        self.__t.pencolor('black')

    def __nose(self, pen_size):
        self.__t.pensize(pen_size)
        self.__goto(264, 152, 10)
        self.__t.forward(6)

    def __mouth(self, pen_size):
        self.__t.pensize(pen_size)
        self.__goto(272, 167, 180)
        self.__drawto(266, 169, -150)
        self.__t.circle(-40, 12)
        self.__goto(257, 172, -160)
        self.__t.circle(-9, 45)

    def __cheek(self, pen_size):
        self.__t.pensize(pen_size)
        self.__goto(199, 179, 40)
        self.__t.fillcolor('#ff8861')
        self.__t.begin_fill()
        self.__t.circle(-19, 60)
        self.__goto(218, 177, -30)
        self.__t.circle(-30, 90)
        self.__goto(221, 216, 158)  # 闭合
        self.__t.circle(-34, 85)
        self.__t.end_fill()

    def __face(self):
        self.__ear(3.5)
        self.__nose(2.5)
        self.__mouth(2.5)
        self.__cheek(3)
        self.__eye(2)

    def __decorate(self, pen_size):
        self.__t.pencolor('#ff8860')
        self.__t.pensize(pen_size)
        self.__goto(345, 140, 60)
        self.__t.fillcolor('#ff8860')
        self.__t.begin_fill()
        self.__t.circle(-7, 200)
        self.__goto(358, 146, -110)
        self.__t.circle(-50, 10)
        self.__drawto(346, 164, 110)
        self.__drawto(332, 153, 110)
        self.__t.circle(-50, 10)
        self.__t.circle(-8, 180)
        self.__t.end_fill()

    def start(self):
        self.__wall(10)
        self.__head(6)
        self.__hand(5, 3)
        self.__body(4.5)
        self.__feet(4.5, 4)
        self.__tail(6)
        self.__face()
        self.__decorate(2)
        self.__goto(0, 0, 0)


if __name__ == "__main__":
    turtle.setup(400, 400)
    turtle.screensize(350, 350, '#d3e9ff')
    turtle.title('Pikachu')
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()
