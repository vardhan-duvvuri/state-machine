STATE_MACHINE={
    's'     :   {'final': False, 'transition':('c',None,None,None)},
    'c'     :   {'final': False, 'transition':('c',None,'d','at')},
    'd'     :   {'final': False, 'transition':('c1',None,None,None)},
    'c1'    :   {'final': False, 'transition':('c1',None,None,'at')},
    'at'    :   {'final': False, 'transition':('c2',None,None,None)},
    'c2'    :   {'final': False, 'transition':('c2',None,'d1',None)},
    'd1'    :   {'final': False, 'transition':('c3',None,None,None)},
    'c3'    :   {'final': True, 'transition':('c3',None,None,None)},
        }

#print STATE_MACHINE[current_state]['transition'][0]

def matches():
    current_state='s'
    data=raw_input("Enter the data : ")
    for i in data:
        #print current_state
        #print i
        if current_state == None:
            print "Invalid value"
            return
        else:
            if i.isalpha():
                current_state=STATE_MACHINE[current_state]['transition'][0]
            elif i.isdigit():
                current_state=STATE_MACHINE[current_state]['transition'][1]
            elif i == '.':
                current_state=STATE_MACHINE[current_state]['transition'][2]
            elif i == '@':
                current_state=STATE_MACHINE[current_state]['transition'][3]
    if current_state == None:
        print "Invalid email"
    else:        
        if STATE_MACHINE[current_state]['final']:
            print "Valid email"
        else:
            print "Invalid email"

if __name__ == '__main__':
    matches()
