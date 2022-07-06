#
# competition_v1.py - outputting score for each dance competitor
#
import numpy as np

def main():
    numJudges = 7
    numCompetitors = int(input('Enter number of competitors (between 3 and 16 inc): '))

    for comp in range(numCompetitors +1):
        totalC = 0
        print('Enter score between 0 and 10: ')
        for j in range(numJudges):
            scoreJ = int(input('Score for judge: '))
            totalC = totalC + scoreJ
            
            scoreC = totalC/numJudges
        print('Score for competitor ', comp, ' is', scoreC)

if __name__== '__main__':
    main()
