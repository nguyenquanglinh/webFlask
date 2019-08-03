
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if i%2==1:
#          print ('so le', i)
#     else:
#         print ('so chan', i)

# for t in range (10):
#     for u in range (10):
#         for v in range (10):
#             if 100*t+ 10*u+v == t**3 +u**3+v**3:
#                 print(t, u, v)

n = int (input ('nhap n'))

s = 1
for i in range (n):
    # t= int (input('i'))
    s=s+1/(i**2)
print('tong la', s)