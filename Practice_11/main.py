import sympy
# f(x) = 18x^3+5x^2 + 10x - 30
x = sympy.Symbol('x')
f=18*x**3 + 5*x**2 + 10*x - 30
# 1.Определить корни
des = sympy.solve(f,x)
print(des)
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
print(sympy.solve(f>0,x))
print(sympy.solve(f<0,x))
# 4. Построить график
sympy.plotting.plot(f)
# 5. Вычислить вершину
diff = sympy.diff(f,x)
print(diff)
top = sympy.solve(diff,x)
print(top)
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
print(sympy.solve(diff>0,x))
print(sympy.solve(diff<0,x))