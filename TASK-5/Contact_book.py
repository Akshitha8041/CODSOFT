print('1. Add a contact\n2.Search for contact\n3.Delete a contact\n4.Exit')
n=1
d=dict()
while(n!=4):
    n=int(input('Enter an option:'))
    if n==1:
        name=input('Enter New Name:')
        Num=input('Enter New Number:')
        if name not in d:
            d[name]=Num
            print('contact saved successfully')
        else:
            print('contact is already existing')
    elif n==2:
        s=input('Enter name to search:')
        if s in d:
            print(s,'->',d[s])
        else:
            print('contact not found')
    elif n==3:
        x=input('Enter name to delete: ')
        if x in d:
            d.pop(x)
            print('contact deleted successfully')
        else:
            print('contact not found')
    elif n==4:
        print('Thankyou')
    else:
        print('invalid option')
