import time

BRUTE_FORCE_MODE = 1 
CHECK_PASSWORD_MODE = 2

def get_mode_selection():
  while True:
    mode = int(input("Enter mode (1=brute force, 2=check password): "))
    if mode in [BRUTE_FORCE_MODE, CHECK_PASSWORD_MODE]:
      return mode
    else:
      print("Invalid selection.")

def read_word_list(file_path):
  with open(file_path) as f:
    for line in f:
      yield line.strip()  

def print_result(string, found):
  if found:
    print(f"{string} was found")
  else:
    print(f"{string} was not found")

def brute_force(file_path):
  for word in read_word_list(file_path):
    time.sleep(0.5)
    print(word)

def check_password(password, file_path):

  found = False

  for word in read_word_list(file_path):
    
    if password in word:
      found = True
      break

  print_result(password, found)

if __name__ == "__main__":

  mode = get_mode_selection()

  if mode == BRUTE_FORCE_MODE:
    file_path = input("Enter word list file path: ")
    brute_force(file_path)

  elif mode == CHECK_PASSWORD_MODE:
    password = input("Enter password to check: ")  
    file_path = input("Enter word list file path: ")
    check_password(password, file_path)