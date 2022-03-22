import time
player_HP = 100
player_Att = 35
enemy_HP = 100
enemy_Att = 23

print(f'[Player]\n\nHealth Points: {player_HP}\nAttack Points: {player_Att}')
print('---------------------------------')
time.sleep(0.5)
print(f'[Enemy]\n\nHealth Points: {enemy_HP}\nAttack Points: {enemy_Att}')
print('---------------------------------')
time.sleep(0.5)

while True:

    player_HP = player_HP - enemy_Att
    enemy_HP = enemy_HP - player_Att

    print(f'You are attacking the enemy, [Enemy\'s] remain Health Point is: {enemy_HP}')
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