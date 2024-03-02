import colorama as col

My_list = ["ali", "tahere", "ali", "kosar", "ali"]
lenList = len(My_list)
a = 0
del_Counter = 0
print(My_list)
while a < len(My_list):
    My_list.remove("ali")
    a = a+1
    del_Counter= del_Counter+1

print(My_list,col.Fore.MAGENTA,f'--This list has {len(My_list)} items')
print(col.Fore.RED,col.Style.BRIGHT,f'** {del_Counter} items deleted from the list')