#
# competition_v1.py - outputting score for each dance competitor
#
import numpy as np

def inputValue(lower, upper, prompt):
    value = int(input(prompt))
    while value < lower or value > upper:
        print('Error -- re-enter number (lower-upper): (', lower, '-', upper, ')')
        value = int(input(prompt))
    return value

def main():
    numJudges = 7
    numCompetitors = inputValue(3, 16, 'Enter number of competitors (between 3 and 16 inc): ')

    while numCompetitors < 3 or numCompetitors > 16:
        numCompetitors = int(input('Error -- Re-enter number of competitors (between 3 and 16 inc): '))

    for comp in range(numCompetitors):
        totalC = 0
        print(0, 10, 'Enter score between 0 and 10: ')
        for j in range(numJudges):
            scoreJ = int(input('Score for judge: '))
            while scoreJ < 0 or scoreJ > 10:
                scoreJ = int(input('Error -- Re-enter score (0-10): '))
            totalC = totalC + scoreJ
            
        scoreC = totalC/numJudges
        print('Score for competitor ', comp + 1, ' is', scoreC)
    print()

if __name__== '__main__':
    main()
