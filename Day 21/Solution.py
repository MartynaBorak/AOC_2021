def roll_die_determ(dice):
    move = 0
    for _ in range(3):
        dice += 1
        move += dice
        if dice == 100:
            dice = 0
    return move, dice

def main():
    #input
    player1 = [10, 0] #[position, score]
    player2 = [9, 0]

    #part 1
    dice = 0
    rolls = 0
    while True:
        #p1 turn:
        move, dice = roll_die_determ(dice)
        rolls += 3
        player1[0] += move
        player1[0] = (player1[0]-1)%10 +1
        player1[1] += player1[0]
        if player1[1] > 999:
            break
        #p2 turn:
        move, dice = roll_die_determ(dice)
        rolls += 3
        player2[0] += move
        player2[0] = (player2[0]-1)%10 +1
        player2[1] += player2[0]
        if player2[1] > 999:
            break
    a = min(player1[1], player2[1])
    print("Part 1: " + str(a*rolls))

    #part 2
    print("Part 2: " + str())
    

if __name__ == '__main__':
    main()