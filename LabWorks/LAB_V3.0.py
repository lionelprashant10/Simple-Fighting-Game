import time, random
for i in range(3):
    player_HP = random.randint(100,150)
    player_Att = random.randint(50,80)
    enemy_HP = random.randint(100,200)
    enemy_Att = random.randint(30,50)
    print('')
    print('')
    time.sleep(1)
    print(f'---------- ROUND {i+1} ----------')
    print(f'[Player]\n\nHealth Points: {player_HP}\nAttack Points: {player_Att}')
    print('---------------------------------')
    print('')
    time.sleep(1)
    print(f'[Enemy]\n\nHealth Points: {enemy_HP}\nAttack Points: {enemy_Att}')
    print('---------------------------------')
    print('')
    time.sleep(1)
    while True:

        player_HP = player_HP - enemy_Att
        enemy_HP = enemy_HP - player_Att

        print(f'You are attacking the enemy, [Enemy\'s] remain Health Point is: {enemy_HP}')
        time.sleep(1)
        print(f'Enemy is attacking you, [Player\'s] remain Health Point is: {player_HP}')
        print('')
        print('')
        time.sleep(1)


        if player_HP > 0 and enemy_HP <= 0:
            print('You Win!') 
            break
        elif player_HP <= 0 and enemy_HP > 0:
            print('Enemy Win!')
            break
        elif player_HP <= 0 and enemy_HP <= 0:
            print('You and Your enemy both died')
            break