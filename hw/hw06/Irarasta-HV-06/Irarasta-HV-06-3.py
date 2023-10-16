
  ## Define the dictionary of credentials, t
  ## which already exist in the base:

def credentials(login,password):
    input_credentials = {
        'nick': 'bestnick',
        'mike': 'supermike',
        'annette': 'babydoll',
        'mario': 'princess'
    }
  ## Check if the User enters correct LOGIN
  ## which is the firts (key) element
  ## in the pair login / password

    while True:
        if login in input_credentials:
            print(f'Welcome, {login}!')
            break
        else:
            print('Invalid LOGIN. Enter a valid LOGIN.')
            login = input("Enter your LOGIN: ")
  ## If User enters wrong LOGIN, ask to enter correct LOGIN
user_login = input("Enter your LOGIN: ")

credentials(user_login, None)