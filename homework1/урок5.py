# condition = True
# while condition :
#     user_choice = input("please chooce:\n1:print message\n0:Exit\n--")
#     if user_choice == "1":
#         print("hello world")
#     elif user_choice == "0":
#         condition = False


# condition = True
# while condition:
#
#     try:
#         user_input = input("please enter id code: ")
#         user_input = int(user_input)
#     except
#         print("your code is invalid")


# condition = True
while True:
    try:
        user_input = input('Please enter ID code: ')
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print('Your code is not numeric.')
        continue
    except UserWarning:
        if len(user_input) > 11:
            print('ID code is too long')
        elif len(user_input) < 11:
            print('ID code is too short')
        continue
    else:
        # print(user_input)
        break

 condition = True
 while condition:
     user_choice = input("please shoice :\n1.Get data from id\n2. validate\n0.exit")
     if user_choice == "1"
         gender_num == user_input[0]





         if int(gender_num) % 2 == 0:
             gender_id = "female"
             elise:
             gender_id = "male"
     elif user_choice == "2"
         id_code = input('Please enter your ID: ')

         chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
         chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

         cnt = 0
         result = 0
         for num in chk1:
             result += num * int(id_code[cnt])
             cnt += 1
         check_num = result % 11

         if int(id_code[-1]) == check_num:
             print(f'Your ID is {id_code}')
             print('ID is valid')
         elif check_num == 10:
             cnt = 0
             result = 0
             for num in chk2:
                 result += num * int(id_code[cnt])
                 cnt += 1
             check_num = result % 11
             if check_num == int(id_code[-1]):
                 print(f'Your ID is {id_code}')
                 print('ID is valid')
             else:
                 print('Your ID is invalid.')
         else:
             print('Your ID is invalid.')

         pass
     elif user_choice == "0"
         break
    elis:
        print("choice is out of range")
