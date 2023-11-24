# Nested For Loop for printing  similar  pattern as below  based  on  the  number  input  given  by  the user

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num  =  int(input("Enter  a  number  to  generate  its  pattern  :  "))
for  i  in  range(1,num  +  1):
        for  j  in  range(1,i  +  1):
                  print(j,  end  =  "  ")
        print()
