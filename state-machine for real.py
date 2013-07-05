# State machine program for real numbers
# state = final,trasition(a,b,c)
# final is to find it is the final state
#a is if the i is alphabetic
#b is if the i is numeric
#c is if the i is .
STATE_MACHINE={
    's'     :   {'final': False, 'transition':(None,'int',None)},
    'int'   :   {'final': True, 'transition':(None,'int','s1')},
    's1'    :   {'final': False, 'transition':(None,'s2',None)},
    's2'    :   {'final': True, 'transition':(None,'s2',None)},
    #'None'  :   {'final': False}
        }

#print STATE_MACHINE[current_state]['transition'][0]

def matches():
    current_state='s'
    data=raw_input("Enter the data : ")
    for i in data:
        #print i
        #print current_state
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
    if current_state == None:
        print "Invalid value"
    else:        
        if STATE_MACHINE[current_state]['final']:
            print "Valid value"
        else:
            print "Invalid value"

if __name__ == '__main__':
    matches()
