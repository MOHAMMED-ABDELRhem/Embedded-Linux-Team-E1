#!/usr/bin/python3

usr_dict = { "Ahmed" : 1394 , "Ali" : 6078 , "Amr" : 9345 }

usr_name = input('Enter User name:')
if usr_name in usr_dict.keys():
    usr_pass = int(input("Enter Your Password"))
    if usr_pass == usr_dict[usr_name]:
        print(" Welcome " + usr_name)
        exit()
print(":: incorrect entry ::")
  
   