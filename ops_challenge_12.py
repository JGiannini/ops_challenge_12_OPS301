#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Create a Python script that performs the following:

# [X] Prompt the user to type a string input as the variable for your destination URL
# [X] Prompt the user to select a HTTP Method of the following options: 
#       [X] GET
#       [X] POST
#       [X] PUT
#       [X] DELETE
#       [X] HEAD
#       [X] PATCH
#       [X] OPTIONS
# [X] Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# [X] Using the requests library, perform a GET request against your lab web server.
# [X] For the given header, translate the codes into plain terms that print to the screen; for example, a ‘404’ error should print ‘Site not found’ to the terminal instead of ‘404’.
# [X] For the given URL, print response header information to the screen

import requests #imports necessary library

def run_request():
    destination_flag = 0
    r = True
    user_destination = input("\nPlease enter a destination URL:\n")
    user_method = input("\nChoose a HTTP Method: [G] GET | [P] POST | [PU] PUT | [D] Delete | [H] HEAD | [PA] PATCH | [O] OPTIONS | [Q] Quit:\n")
    
    while r:
        if destination_flag == 0:
            print("\nPlease confirm the following details: ")
            
            print("Your destination: " + user_destination)
            # Translates entry into full name for better UX
            if user_method == "G" or user_method == "g":
                user_method_easy = "GET"
            elif user_method == "P" or user_method == "p":
                user_method_easy = "POST"
                print("(Note: Since you selected Post, for testing purposes we will use https://httpbin.org/post)")
            elif user_method == "PU" or user_method == "pu":
                user_method_easy = "PUT"
            elif user_method == "D" or user_method == "d":
                user_method_easy = "DELETE"
            elif user_method == "H" or user_method == "h":
                user_method_easy = "HEAD"
            elif user_method == "PA" or user_method == "pa":
                user_method_easy = "PATCH"
            elif user_method == "O" or user_method == "o":
                user_method_easy = "OPTIONS" 
            elif user_method == "Q" or user_method == "q":
                break
            
            print("Your choosen HTTP Method: " + user_method_easy)

            user_choice = input("\nSelect: [1] edit destination | [2] edit HTTP Method | [3] Continue:\n")
        
            if user_choice == "1":
                destination_flag = 1
                continue
            elif user_choice == "2":
                destination_flag = 2
                continue
            elif user_choice == "3":
                destination_flag = 3
                continue
        
        elif destination_flag == 1:
            user_destination = input("\nPlease enter a destination URL:\n")
            destination_flag-=1
            continue

        elif destination_flag == 2:
            user_method = input("\nChoose a HTTP Method: [G] GET | [P] POST | [PU] PUT | [D] Delete | [H] HEAD | [PA] PATCH | [O] Options | [Q] Quit:\n")
            destination_flag-=2
            continue
        
        #Perform request
        elif destination_flag == 3:
            if user_method == "G" or user_method == "g":
                reply = requests.get("http://"+user_destination)
                print("\nResults:")
                if reply.status_code == 200:
                    print("Success!")
                    print("\nHeader data: \n"+str(reply.headers)) # Also print request header data
                elif reply.status_code == 301:
                    print("Moved Permanently.")
                elif reply.status_code == 302:
                    print("Moved Temporarily.")
                elif reply.status_code == 403:
                    print('Forbidden.')
                elif reply.status_code == 404:
                    print('Site Not Found.')
                elif reply.status_code == 500:
                    print('Internal Server Error.')
                elif reply.status_code == 503:
                    print('Server Unavailable.')
                else:
                    print("Error")
                break
            #Playing with POST
            elif user_method == "P" or user_method == "p":
                get_key = input("\nProvide a key:\n")
                get_value = input("\nProvide a value:\n")
                # Using HTTPbin for testing
                reply = requests.post('https://httpbin.org/post', data={get_key:get_value})
                print("\nHeaders: "+str(reply.request.headers))
                print("\nURL: "+str(reply.request.url))
                print("\nBody: "+str(reply.request.body))
                break
            #Catch all for anything not GET or POST for now
            elif user_method != "G" and user_method != "g" and user_method != "P" and user_method != "p":
                print("Other HTTP Methods Still In Development. Coming soon!")
                break
#main
run_request()


#Resource: https://realpython.com/python-requests/#the-get-request


        
        
        
        
        
       


