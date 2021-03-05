import turtle as t

t.shape("turtle")


# 삼각형 그리기
# d = 200
# t.color("red")
# for x in range(3):
#     t.forward(d)
#     t.left(120)


# 사각형 그리기
# t.pensize(3)
# for x in range(4):
#     t.forward(d)
#     t.left(90)

# 원 그리기
# t.color("blue")
# t.pensize(5)
# t.circle(100)

# n각형 그리기
# n = 8
# t.color("purple")
# t.speed(1)
# t.begin_fill()
# for x in range(n):
#     t.forward(50)
#     t.left(360/n)
# t.end_fill()

# 원50개 그리기
# n = 50
# t.bgcolor("black")
# t.color("green")
# t.speed(0)
# for x in range(n):
#     t.circle(80)
#     t.left(360/n)

# 네모200개 그리기
angle = 89
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)