def f(t, y):
    return t - y**2

def Euler_Method():
    a = 0.0
    b = 2.0
    n = 10
    t = 0.0
    y = 1.0  # initial value of y

    h = (b - a) / n
    
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h

    print(y)

def Runge_Kutta_Method():
    a = 0.0
    b = 2.0
    n = 10
    t = 0.0
    y = 1.0  # initial value of y

    h = (b - a) / n

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h

    print(y)

# Run both methods
Euler_Method()
Runge_Kutta_Method()
