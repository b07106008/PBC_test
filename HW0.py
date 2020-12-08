x1 = int(input())
x2 = int(input())
p1 = int(input())
p2 = int(input())
t = int(input())

pay = x1*p1 + x2*p2
change = t-pay
ans = "%s,%s,%s"

print(ans % (t, pay, change))
