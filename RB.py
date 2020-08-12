import math
import random
import itertools
from pycsp3 import *
from pycsp3.solvers.abscon import AbsConProcess, AbsconPy4J
from pycsp3.solvers.chocosolver import ChocoProcess


k1 = 2
k2 = 3
n = 20
alpha = 0.6
p = 0.4
r = 0.95
l1 = 0.3
l2 = 0.7
l = [l1, l2]
k = [k1, k2]
alpha = float(alpha)
p = float(p)
l1 = float(l1)
l2 = float(l2)
r = float(r)
m = r * n * math.log(n)  
d = round(n ** alpha)  
m_list = [math.ceil(i * m) for i in l]
q_list = [round(p * d ** ki) for ki in k]  

x_sub = range(n)  
var_support = [list(itertools.product(range(1, d + 1), repeat=ki)) for ki in k]  # 约束变量可取值组合全排列
constraint_var_sub_group = list()  
constraint_var_no_support_group = list()  

for i, mi in enumerate(m_list):
    for constraint_n in range(mi):
            tmp_con_x = random.sample(x_sub, k[i])  
            constraint_var_sub_group.append(tmp_con_x)
            tmp_con_x_no_support = random.sample(var_support[i], q_list[i])
            constraint_var_no_support_group.append(tmp_con_x_no_support)

x = VarArray(size=n, dom=range(1, d + 1))

for i, con_var in enumerate(constraint_var_sub_group):
    satisfy(
            [x[con_var_i] for con_var_i in con_var] not in constraint_var_no_support_group[i]
          )


print("Compile:\n")
instance = compile()


print("\nStatic solving:\n")
solution = AbsConProcess().solve(instance)
print("solution:", solution)
    
print("\nPy4j solving:\n")
solver = AbsconPy4J()
solver.loadXCSP3(instance)

print("in progress")
