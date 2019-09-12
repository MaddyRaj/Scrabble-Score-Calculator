# The purpose of the class was to be able to place a word on a 15 by 15 grid, which also contains 
# Special blocks that increase the score of the letter or the total of the whole word. This class
# has methods that assign the appropriate scores to the letters and if they are on a special block,
# then to multiply by the appropriate number to give final score.  
def Scrabble():    
    # made score a global variable since it will be used inside the methods in the class below
    # so making it global is easier to work with. 
    global score
    # score stores the score for all the letters from a-z.
    score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}
    
    # This method took the x,y values to check if they are in a special spot and the let was taken
    # to multiply by the score of the letter with the type of special block, if it was applicable.
    def specialSpots(x,y,let):
        # The 4 sets below each saved the coordinates of the special blocks on the scrabble grid. 

        # DL - Double Letter
        DL = {(3,14),(11,14),(6,12),(8,12),(0,11),(7,11),
            (14,11),(2,8),(6,8),(8,8),(12,8),(3,7),(11,7),
            (2,6),(6,6),(8,6),(12,6),(0,3),(7,3),(7,3),
            (14,3),(6,2),(8,2),(3,0),(11,0)}
 
        # DW - Double Word
        DW = {(1,13),(13,13),(2,12),(12,12),(3,11),(11,11),
            (4,10),(10,10),(7,7),(4,4),(10,4),(3,3),(11,3),
            (2,2),(12,2),(1,1),(13,1)}

        # TL - Triple Letter
        TL = {(5,13),(9,13),(1,9),(5,9),(9,9),(13,9),
            (1,5),(5,5),(9,5),(13,5),(5,1),(9,1)}

        # TW - Triple Word
        TW = {(0,14),(7,14),(14,14),(0,7),
            (14,7),(0,0),(7,0),(14,0)}

        # The big if/elif/else loop below checked each special blocks set above and if the x,y
        # given to us matched any co-ordinates in any of the special blocks, then returns 2 or 3 
        # times the score of the letter. For the double/triple word, we need to multiply by the
        # final score, so that is done by just returning a string here, and then a check will be made
        # in the placeOnBoard method, to multiply the total instead of just the letter.
        if((x,y) in DL):
            return (2*score[let])
        elif((x,y) in DW):
            return "Double Word"
        elif((x,y) in TL):
            return (3*score[let])
        elif((x,y) in TW):
            return "Triple Word"
        else:
            return (score[let])

    # This method took the x,y values, the direction, and the word to plot on the scrabble grid.
    def placeOnBoard(x,y,direc,word):
        # variable to keep track of the total score of the word
        total = 0
        # variable to keep track of how many double,triple word blocks we have, to multiply the
        # total score by how many of these we have, at the end of the method. 
        tripleW = 0
        doubleW = 0

        # If the direction is right, then inside there is a for loop which will go through each
        # letter in the word given, and inside there is another for loop to go through the global
        # variable score above to check if the letter is valid.  
        if(direc == 'R'):
            for let in word:
                for alph in score:
                    # If the letter matches, then we give the x,y,let values to the special spots
                    # method to check if there are any special spots.
                    if(let == alph):
                        # If the type of special spots is a string, then that means we found a 
                        # double/triple word.
                        if(type(specialSpots(x,y,let)) == str):
                            # so we first add to the total the score of the letter
                            total += score[let]
                            # Then, we check if the string returned was double word, then we
                            # increment the variable for how many double word there are or if
                            # triple word then the same is done, else pass.
                            if(specialSpots(x,y,let) == 'Double Word'):
                                doubleW += 1
                            elif(specialSpots(x,y,let) == 'Triple Word'):
                                tripleW += 1
                            else:
                                pass
                        else:
                            # If the type is not string, then  we just add to the total the
                            # score we received from the special spots method. 
                            total += specialSpots(x,y,let)
                # We also increment is x by 1, because since we are going to the right,
                # just the x values changes, y stays the same.
                x += 1
        elif(direc == 'D'):
            # if the direction is Down, then we do the same for loop as above, the only 
            # difference is that we decrement the y by 1 at the end of checking and adding the 
            # score of each letter, since we are plotting the letters in the order Down, instead
            # of to the right.
            for let in word:
                for alph in score:
                    if(let == alph):
                        if(type(specialSpots(x,y,let)) == str):
                            total += score[let]
                            if(specialSpots(x,y,let) == 'Double Word'):
                                doubleW += 1
                            elif(specialSpots(x,y,let) == 'Triple Word'):
                                tripleW += 1
                            else:
                                pass
                        else:
                            total += specialSpots(x,y,let)
                # We also decrement is y by 1, because since we are going to the Down,
                # just the y values changes, x stays the same.
                y -= 1
        else:
            print("Please give valid direction!")
        
        # The if/elif/else below is checking that first if the double word variable is not 0, 
        # then it means we had to double the score of the word the desired number of times, so we
        # square 2 by the number of double word we found times the total score. We do the same 
        # thing for the triple word, if the same situation was found. We also check if we found 
        # that there were both double word and triple word blocks, then we take into account both
        # and multiply them with the total score. If all the blocks were non-special, just return
        # the total score.
        if(doubleW != 0):
            return ((2 ** doubleW) * total)
        elif(tripleW != 0):
            return ((3 ** tripleW) * total)
        elif(doubleW != 0 and tripleW != 0):
            return ((2 ** doubleW) * (3 ** tripleW) * total)
        else:
            return total

    def main():
        # counter is made just so that the first line of the file is not counted, when taking 
        # input for the score, since the first line is the number of test cases.
        counter = 0
        # there is a boolean for if the direction and word were found, because if both were not
        # found, then there would be an issue if we took input the wrong line and give wrong 
        # output.
        gotDirec = False
        gotWord = False
        # then file that i stored in my folder was called input and I read from it, so use
        # the open function and the variable is assigned to reading from that file.
        fileInput = open("input.txt","r")

        # Test case 1
        #0 0 R
        #indix

        # Test case 2
        #7 8 D
        #bootcamp

        # Test case 3
        #0 0 R
        #unconsciousness

        # Test case 4
        #14 14 D
        #cryptozoologies

        # saved all the lines from the input file into the variable, which will 
        # be an array saving all the lines in it. 
        allLines = fileInput.readlines()
        
        fileInput.close()

        # iterate over each line in the input file, but discard the first line, so the counter
        # is 0 initially, and gets incremented at the end of the loop, since the first line does
        # not have x,y or direc, but just the number of test cases.
        for line in allLines:
            if(counter == 0):
                line.strip()
            else:
                # checks that if the number is odd, then that line will represent the x,y,direc
                # line and that line is split into an array, codi, representing co-ordinate and 
                # direction. 
                if(counter % 2 != 0):
                    answer = line.strip()
                    codi = answer.split()
                    # there are x,y values created which will be the first and second value
                    # in the string or the array, and the last one will be the direction.
                    x,y = int(codi[0]),int(codi[1])
                    direc = codi[2]
                    # we have found the direction and co-ordinates and will wait to get the word
                    gotDirec = True
                else:
                    # if the counter was even, then we found the second line of each test case, 
                    # so the line is saved as the word and we change got word to true, since we 
                    # found the word and now we can place the word on the board.
                    word = line.strip()
                    gotWord = True
            # if we have found the co-ord, direction and the word, then we have found 1 full case,
            # so we print the score found from the placeOnBoard method, which will be given the 
            # respective values. 
            if(gotDirec == True and gotWord == True):
                print(placeOnBoard(x,y,direc,word))
                # we make the direction and the word false again, since we will going through the 
                # next set of test cases, so we want to make sure we get both direction and word
                # accurately for each test case.
                gotDirec = False
                gotWord = False
            # counter is incremented by 1 at the end of each line
            counter += 1
    
    main()
    # call the main, which will call the output function, that calls the other methods which do
    # the main job of the crux of the calculations and main logic of the code.
Scrabble()
