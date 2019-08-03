# # a= input('nhap nam sinh')
# # a=int(a)
# # b = 2019-a


# # if b>=18:
# #     print ('la nguoi lon')
# # elif b>=13:
# #     print('teen')
# # else:
# #     print('tre em')



# # #  else: 
# # #      if b<13:
# # #         print ('la tre con')
# # #     else:
# # #         print('teen')

# # age = 10
# # is_baby = age < 10
# # print (is_baby)
  


# # num = 101
# # is_odd = num % 2 == 1
# # print (is_odd)

# # text = 'xin chao'
# # text_is_not_empty = len(text)> 0
# # print (text_is_not_empty)
# if True:
#     print ('true')
# if False:
#     print ('false')
a = int (input ('nhap a'))
b = int (input ('nhap b'))
c= int (input('nhap c'))
if a+b<= c:
    print ('khong phai tam giac')
elif a+c <= b:
    print ('khong phai tam giac')
elif b+c<=a:
    print ('khong phai tam giac')
else:
    print ('la tam giac')