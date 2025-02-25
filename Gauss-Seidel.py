A = [[2, 3, -4, 9],[-4, -27, 11, -6],[36, 11, -20, 10],[-2, -7, 22, -6]]
b = [[-10],[7],[7],[4]]


Itera = 319025070

n = 0

Man = 10**(-6)

x1 = 0
x2 = 0
x3 = 0
x4 = 0

Cx1 = (3+4+9)/36
Cx2 = (4*Cx1+11+6)/27
Cx3 = (36*Cx1+11*Cx2+10)/20
Cx4 = (2*Cx1+7*Cx2+22*Cx3)/6

if (Cx1 and Cx2 and Cx3 and Cx4) < 1:
 print("A matriz converge")

else:
    print("A matriz diverge")

def Gauss(x2, x3, x4, n, Man):
    X1 = (-10 - 3*x2 + 4*x3 - 9*x4)/2
    X2 = (-(7 + 4*X1 - 11*x3 + 6*x4))/27
    X3 = (-(7 - 36*X1 - 11*X2 - 10*x4))/20
    X4 = (-(4 + 2*X1 + 7*X2 - 22*X3))/6
    if n <= Itera and abs(X1) >= Man and abs(X2) >= Man and abs(X3) >= Man and abs(X4) >= Man:
        n = n + 1
        print(X4)
        return Gauss(X2,X3,X4,n,Man)

    else:
        print(f"Valor de X1 = {X1}, X2 = {X2}, X3 = {X3}, X4 = {X4} e iteração atual {n}") and print("that's All people")
        return None
Gauss(x2, x3, x4, n, Man)