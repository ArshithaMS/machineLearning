chars='abcdefghijklmnopqrstuvwxyz'
str1='It was a bright cold day in April and the clocks were striking thirteen'

for c in chars:
      count=str1.count(c)

      if count >1:
              print(c,count)
