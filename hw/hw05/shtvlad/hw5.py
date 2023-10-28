# TASK_1
# l = [1, 2, 5, 7, 4, 3, 8]
# for i in range(len(l)):
#     l[i]=float(l[i])
# print(l)
#
# TASK_2_v1
# n = int(input("Input number: "))
# fib_l=[]
# cnt=0
# while cnt<=n:
#     if cnt<2:
#         fib_l.append(cnt)
#     else:
#         s=fib_l[cnt-2]+fib_l[cnt-1]
#         fib_l.append(s)
#     cnt += 1
# print(fib_l)
#
# TASK_2_v2
# n = int(input("Input number: "))
# f1=0
# f2=1
# print(f1, f2, end=" ")
# cnt=0
# while cnt<n-2:
#     f_sum=f1+f2
#     f1=f2
#     f2=f_sum
#     cnt += 1
#     print(f_sum,end=" ")
#
# TASK_3
n=int(input("Factorial number: "))
f=0
sum_f=1
for f in range(1,n+1):
    sum_f=sum_f*f
    f+=1
print(f"{n}!=",sum_f)