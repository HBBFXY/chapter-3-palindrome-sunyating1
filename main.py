n = input()
if len(n)!=5 or not num.isdigit():
  print("输出错误")
else:
  if n == n[::-1]:
    print("是回文数")
  else:
    print("不是回文数")
