#cull excel sheet by first removing duplicate subscriber ids and
#renewal codes from their respective columns


#do your text file with the subscriber IDs here
with open('testpad.txt', 'r') as file:
    lines = file.readlines()

#renewal codes here
with open('testpad_renewalcode.txt', 'r') as file:
    codes = file.readlines()


with open('keys.txt', 'r') as file:
    keys = file.readlines()

    api_url = keys[0].rstrip()
    api_key_id = keys[1].rstrip()
    api_password = keys[2].rstrip()