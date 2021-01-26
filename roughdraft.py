import sys


def findseats(number, ident, seats, rowtoletter):


    rows = len(seats)
    columns = len(seats[0])
    res = []
    for i in range(rows):

        recentchair = None
        for j in range(columns):

            if (number == 0):
                if (recentchair != None):
                    index = recentchair + 1
                    while(index < columns and index < (j + 3)):
                        seats[i][index] = ident
                        if (i > 0):
                            seats[i - 1][index] = ident
                        if (i < rows - 1):
                            seats[i + 1][index] = ident
                        index += 1
                return res 

            if (seats[i][j] == '' or seats[i][j] == ident):
                seats[i][j] = ident
                if (i < rows - 1):
                    seats[i + 1][j] = ident
                if (i > 0):
                    seats[i - 1][j] = ident
                res.append(rowtoletter[i] + str(j + 1))
                number -= 1
                recentchair = j 

    return res








def main():
    if (len(sys.argv) != 3):
        print('Usage: movietheater.py INPUT_FILE OUTPUT_FILE')
        return 


    f = open(sys.argv[1],"r")
    input = f.readlines()

    f.close()

    requests = {}


    for x in input:
        txt = x.split()

        if (len(txt) != 2 or (not (txt[1].isnumeric()))):
            raise Exception("Input Line: ID   # in Party")
        
        requests[txt[0]] = int(txt[1])
    

    srequests = {}
    sortedkeys = sorted(requests, key=requests.get, reverse=True)

    for w in sortedkeys:
        srequests[w] = requests[w]


    # initialize seats
    seats = [ [ '' for i in range(20) ] for j in range(10) ] 


    rowtoletter = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
    }

    results = {}


    for r in srequests:
        results[r] = findseats(srequests[r], r, seats, rowtoletter)


    
    f = open(sys.argv[2], "w")

    for key in sorted(results):
        result = ','.join(results[key])
        f.write(key + ' ' + result)
        f.write('\n')

    f.close()






if __name__ == '__main__':
    main()