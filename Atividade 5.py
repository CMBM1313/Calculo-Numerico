print("yi = f(xi)")

x = 10
f=(3*(x**8)+(x**7)+9*(x**6)+2*(x**4)+5*(x**3)+7*x)
T2 = f

x = -10
f=(3*(x**8)+(x**7)+9*(x**6)+2*(x**4)+5*(x**3)+7*x)
T1 = f
print(f"y1 = {T1}")

T=0
for i in range(998):
    x = x + 0.02
    f=(3*(x**8)+(x**7)+9*(x**6)+2*(x**4)+5*(x**3)+7*x)
    print(f"y{i+2} = {f}")
    T = T + f

print(f"y1000 = 319025070\n")
R=((0.02)/2)*(T1+T2+(2*T))
print(f"Valor da integral é {R}\n")

V_Med=692460867
Abs = abs(R - V_Med)

print(f"Erro Absoluto é igual a {Abs}")
print(f"Erro Relativo é igual a {((Abs/(V_Med))*100)}")