my_string = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

my_list = list(my_string)

for i in range(len(my_list)//2):
    my_list[i], my_list[-i-1] = my_list[-i-1], my_list[i]

reversed_string = ''.join(my_list)

print(reversed_string)