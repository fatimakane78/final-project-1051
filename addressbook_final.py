#file name will be addressbook.vcf since it is saved already



import os

cname = input('What is the file you want to use?: ')
c = open(cname)


#asking the user which tasks they would like to complete. It is more ideal to add a contact first before anything else
def user_input():
    search_add = input('a. Would you like to add a location?: ' + '\n' + 'b. Do you wanna search an address?: ' + '\n'   + 'c. Would you like to print all contacts?: ')
    return search_add



#asking user to add a contact and creating a vcard file in the name 'addressbook.vcf'
def add(list):
    with open(cname, 'a+') as vcf_file:
        print('Please enter contact details:')
        first_name   = input(' - First name       : ')
        last_name    = input(' - Last name        : ')
        email        = input(' - E-mail address   : ')
        phone_number = input(' - Phone number     : ')
        address      = input(' - Address          : ')
        okay()
        print('Name: {}, Address: {}, Phone Number: {}, Email Address: {}'.format(first_name, last_name, email, phone_number, address))
        dict = { 'First Name': first_name , 'Last Name': last_name , 'Email': email , 'Phone Number': phone_number , 'Address': address } 
        list = []
        list.append(dict)
        print(f'Will be writing vcard to: {vcf_file}')
        okay()
        vcard = make_vcard(first_name, last_name, phone_number, address, email ) 
        write_vcard(vcf_file, vcard)
    return

    
#creating a vcard format
def make_vcard(first_name,last_name,phone_number,address,email):
     
    return [
        'BEGIN:VCARD',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK:{phone_number}',
        f'ADR;WORK;PREF:;;{address}',
        f'VERSION:2.1',
        'END:VCARD'   
    ] 

#user input filling in the lines of the vcard file
def write_vcard(f, vcard):
    with open(cname, 'a') as f:
        f.writelines([l + '\n' for l in vcard])
    return 

#searching in a vcard file
def search(): #list): 
   if user_input() == 'b':
       with open(cname, 'r') as f:
            search = input('Search: Make sure to type it in caps if the contacts is saved in caps: ')
            for i in f:
                if search in i:
                    print(f.read())
                    return True 




#printing everything in the vcard file
def print_all():
    with open(cname , 'r') as f:
        print(f.read())
    #user is allowed to print all contacts

#asking if it is okay to do the task in the giving file 'addressbook.vcf'
def okay():
    okay = input('Is that all? [yes/no]? ')
    if okay in ['Yes', 'yes', 'YES', 'y', 'Y', 'ok']:
        return
    else:
        print('Cancelled.')
        exit(1)

#printing the functions and appending the dictionary
def main(list):
    list = []
    
    for i in list:
        with open(cname, 'r') as f:
            read = f.readlines()
            dict = {}
            for i in range(len(read)):
                if read[i] == 'BEGIN:VCARD':
                    dict = {}
                elif read[i].startswith('N:'):
                    dict['N;'] = read[i][2:]
                elif read[i].startswith('FN:'):
                    dict['FN:'] = read[i][3:]
                elif read[i].startswith('EMAIL;'):
                    dict['EMAIL;'] = read[i][6]
                elif read[i].startswith('TEL;WORK:'):
                    dict['TEL;WORK:'] = read[i][9]
                elif read[i].startswith('ADR;WORK;PREF:;;'):
                    dict['ADR;WORK;PREF:;;'] = read[i][16]
                elif read[i].startswith('VERSION:'):
                    dict['VERSION:'] = read[i][8]
                elif read[i] == 'END:':
                    list.append(dict)

    x = user_input()
    print(search())
    
    if x == 'a':
        print(add(list))                                                                                        
    if x == 'b':
        print(search())
    if x == 'c':
       print(print_all())


if __name__ == '__main__':
    main(list)