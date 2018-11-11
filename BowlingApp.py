def bowlingScore(input):
    scores = list(''.join(input.split()))
    print(scores)

    #this converts input into numbers to more readable line

    for x in  range(len(scores)):
        if scores[x] == 'X':
            scores[x] = 10
        elif scores[x] == '-':
            scores[x] = 0
        elif scores[x] == '/':
            scores[x] = -1
        else:
            scores[x] = int(scores[x])
    print(scores)

    i = 0
    score = 0
    for f in range(10):
        if scores[i] >= 0 and scores[i] < 10:
            if scores[i + 1] == -1:
                score += 10 + scores[i + 2]
            else:
                score += scores[i] + scores[i + 1]
            i += 2
        else:
            if scores[i + 2] == -1:
                score += 10 + 10

            else:
                score += 10 + scores[i + 1] + scores[i + 2]

            i += 1
        print('= %d' % score)

    return score


#or input in ('XXXXXXXXXXXX', '9-9-9-9-9-9-9-9-9-9-', '5/5/5/5/5/5/5/5/5/5/5', 'X7/9-X-88/-6XXX81'):
bowlingScore('5/5/5/5/5/5/5/5/5/5/5')
