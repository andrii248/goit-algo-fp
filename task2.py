import turtle
import math


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    # Малюємо основний стовбур
    t.forward(length)

    # Повертаємося ліворуч і малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.right(45)

    # Повертаємося праворуч і малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.left(45)

    # Повертаємося назад до початкової точки
    t.backward(length)


def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 0, 1, 2, ...): "))

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Дерево Піфагора")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -300)  # Початкова позиція
    t.pendown()
    t.left(90)  # Орієнтація вгору

    draw_pythagoras_tree(t, 100, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
