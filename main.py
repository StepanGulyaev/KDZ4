from scipy.optimize import linprog

f1 = [-1, -1]
f2 = [3, -1]
f3 = [-1, 3]

lhs_ineq = [[1, 2], [-2, -1]]
rhs_ineq = [32, -8]
bnd = [(0, 16), (0, 12)]

opt1 = linprog(c=f1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,method='highs')

print("1)(", opt1.x[0], ", ", opt1.x[1], ")", sep='')

f1_new = 2 - (opt1.x[0] + opt1.x[1])
lhs_ineq.append(f1)
rhs_ineq.append(f1_new)

opt2 = linprog(c=f2, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method='highs')

print("2)(", opt2.x[0], ", ", opt2.x[1], ")", sep='')

f2_new = 1 - (-3 * opt2.x[0] + opt2.x[1])
lhs_ineq.append(f2)
rhs_ineq.append(f2_new)

opt3 = linprog(c=f3, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method='highs')
print("3)(", opt3.x[0], ", ", opt3.x[1], ")", sep='')
