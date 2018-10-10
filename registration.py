''' The module defines user details and methods related to it '''
import re, uuid

class UserDetails(object):
    def __init__(self):
        #A list to store users
        self.user_list = []

    #A method to register the users
    def validate_data(self, username, email, password, confirm_password):
        if not re.match("^[a-zA-Z0-9_]*$", username)\
        or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 6:
            return "Your username should be atleast six characters long"
        elif len(password) < 6:
            return "Your password should be atleast six characters long" 
        elif password != confirm_password:
            return "Your passwords must match"
        else:
            return True  

    #A method to register the user
    def register(self, username, email, password, confirm_password):
        #A dictionary to store user details
        user_details = {}

        #check if there are users in the list
        if len(self.user_list) > 0:
            #validate user details
            validate = self.validate_data(username, email, password, confirm_password) 
            if validate == True:
                #A the validation of user details if True (user details are correct)
                #loop through self.user_list to check if there is a user with similar username or email
                for user in self.user_list:
                    if username == user['username'] or email == user['email']:
                        return "Username or email already exists"
                        
                #No user with the given email or username exist
                else:
                    # So, register the user with correct user details
                    user_details['username'] = username
                    user_details['email'] = email
                    user_details['password'] = password
                    user_details['confirm_password'] = confirm_password
                    user_details['id'] = uuid.uuid1()
                    self.user_list.append(user_details) 
                    return "user registered successfully"
            else:
                #return the error stored in the validate
                return validate              
        else:
            #there are no users in the list
            #validate data
            validate = self.validate_data(username, email, password, confirm_password)
            if validate == True:
                #A the validation of user details if True (user details are correct)
                #Register the user
                user_details['username'] = username
                user_details['email'] = email
                user_details['password'] = password
                user_details['confirm_password'] = confirm_password
                user_details['id'] = uuid.uuid1()
                self.user_list.append(user_details)
                return "user registered successfully"
            else:
                #An error was found in the user details during validation 
                #So the error was stored in the varible validate
                #So you should return the error stored in the validate
                return validate 
                   

    #A login method
    def login(self, username, password):
        #loop through the self.user_list to check for user with the given username and password
        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                return True
        else:
            return "Usename or password or both do not exist" 

    #A method to reset user password
    def reset_password(self, username, password, new_password):
        #loop through self.user_list to check if the provided username and password exists
        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                if len(new_password) < 6:
                    return "Your password must be atleast six characters"
                elif new_password == user['password']:
                    return "Your initial password and new password are same"
                else:
                    user['password'] = new_password 
                    return "You have successfully updated your password"               
        else:
            return "You cannot reset password because username and password or both are not details of any user in the program"    

    
def run():
    Rafael = UserDetails() 

    response = Rafael.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
    print(response)

    response1 = Rafael.register("kelvin", "kelwambugu@gmail.com", "kelraf11747", "kelraf11747")  
    print(response1)

    response3 = Rafael.register("kelvinr", "kelrwambugu@gmail.com", "kelraf11747", "kelraf11747")
    print(response3)

    response2 = Rafael.login("kelvinr", "kelraf11747")
    print(response2)

    response4 = Rafael.reset_password("kelvin", "kelraf11747", "kelraf11749")
    print(response4) 

if __name__ == "__main__":
    run()                    