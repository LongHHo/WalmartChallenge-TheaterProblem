import sys




# algorithm: start with biggest parties and end with smallest parties. for
# each party, determine if the seats available in a row can fit the number of people in the party, such that the 
# seats are available because they aren\'t near any other parties (indicated by '') or seats such that the only nearby people are the people
# in their party (indicated by string of party id). Else, move onto next row. For each seat occupied,
# reassign the value of the seat above and below them so that it has the value of their group id. If in a given row, 
# we are finished assigning seats and there are seats left in that row, block off the 
# next three seats(as well as the ones above and below those seats).





def findseats(number, ident, seats, rowtoletter):


    rows = len(seats)
    columns = len(seats[0])
    # the seats that the party can sit in
    res = []


    for i in range(rows):

        j = 0
        # recentchair keeps track of whether we put people in this row
        recentchair = None
        while (j < columns):
            
            # if we filled all the people in this party, block off next three seats
            # and seats above/below those
            if (number == 0):
                # if we put seats in this row
                if (recentchair != None):
                    index = j
                    while(index < columns and index < (j + 3)):
                        seats[i][index] = ident
                        if (i > 0):
                            seats[i - 1][index] = ident
                        if (i < (rows - 1)):
                            seats[i + 1][index] = ident
                        index += 1
                return res 


            # if a seat has the same id of the party we're trying to fill in,
            # they can sit here. block off top and bottom seats and add to res
            if (seats[i][j] == ident):  
                if (i < rows - 1):
                    seats[i + 1][j] = ident
                if (i > 0):
                    seats[i - 1][j] = ident
                res.append(rowtoletter[i] + str(j + 1))
                number -= 1
                recentchair = j 


            if (seats[i][j] == ''):
                
                # find number of open seats in that row
                openSeats = 0
                indexn = j
                while(indexn < columns and seats[i][indexn] == ''):
                    openSeats += 1
                    indexn += 1


                # if number in party > 20, we need to break party up
                if (number > columns):
                    tNum = columns 
                else:
                    tNum = number
                
                # if number of open seats > number of people in party, try next available row
                if (openSeats < tNum):
                    break
                else:
                    # else, occupy the row with number of people in the party, add to res, and block off top and bottom seats
                    # to only those in their party. 
                    seats[i][j:j + tNum] = [ident for aa in seats[i][j:j+tNum]]
                    if (i < rows - 1):
                        seats[i + 1][j:j + tNum] = [ident for aa in seats[i][j:j + tNum]]
                    if (i > 0):
                        seats[i - 1][j:j + tNum] = [ident for aa in seats[i][j:j + tNum]]
                    for k in range(j, j + tNum):        
                        res.append(rowtoletter[i] + str(k + 1))
                    if (j + tNum > 0):
                        recentchair = j + tNum - 1
                    j = j + tNum
                    number = number - tNum
                    continue 

            j += 1






    return res








def main():
    if (len(sys.argv) != 3):
        print('Usage: movietheater.py INPUT_FILE OUTPUT_FILE')
        return 


    f = open(sys.argv[1],"r")
    input = f.readlines()

    f.close()

    requests = {}

    # read input and create key(id)-value(no. in party) pair
    for x in input:
        txt = x.split()

        if (len(txt) != 2 or (not (txt[1].isnumeric()))):
            raise Exception("Input Line: ID   # in Party")
        
        requests[txt[0]] = int(txt[1])
    

    srequests = {}
    sortedkeys = sorted(requests, key=requests.get, reverse=True)

    # sort the dictionary by value, so that biggest parties appear first
    for w in sortedkeys:
        srequests[w] = requests[w]


    # represent seating with 10 x 20 array of strings, where each string represents
    # the id of a party and the seat is either occupied or unable to be used because it is too 
    # close to a party

    # '' indicates seat is available for use
    seats = [ [ '' for i in range(20) ] for j in range(10) ] 


    # row number in array mapped to letter
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


    # determine seating for each party request
    for r in srequests:
        resp = findseats(srequests[r], r, seats, rowtoletter)
        if (resp):
            results[r] = resp


    
    f = open(sys.argv[2], "w")

    for key in sorted(results):
        result = ','.join(results[key])
        f.write(key + ' ' + result)
        f.write('\n')

    f.close()








if __name__ == '__main__':
    main()