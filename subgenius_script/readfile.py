#cull excel sheet by first removing duplicate subscriber ids and
#renewal codes from their respective columns


#do your text file with the subscriber IDs here
with open('testpad.rtf', 'r') as file:
    lines = file.readlines()

#renewal codes here
with open('testpad_renewalcode.rtf', 'r') as file:
    codes = file.readlines()
