import re

string2work = "India Is An Awesome Country"


def reversed_str(istr):
    rstring = istr[::-1]+" "
    final =''
    count = 0
    for n in range(len(rstring) - 1):
        if rstring[n] == " ":
            #print("found", n)
            final += rstring[count:n][::-1]
            print(rstring[count:n])
            count = n
        #print(count)

    print(final)

reversed_str(string2work)

