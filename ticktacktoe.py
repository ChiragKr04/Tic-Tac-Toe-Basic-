import sys, os

r1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

filled_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def input_at(user):
    if user % 2 == 0:
        os.system('cls')
        print_updated_list(r1)
        print('Player O Chance')
        try:
            idx_fst = int(input('Input from 1-9 where to place your sign = '))
            if idx_fst in range(1, 10):
                if idx_fst - 1 not in filled_idx:
                    print('Location Filled')
                    input_at(user)
                else:
                    updated_list = put_idx_player1(idx_fst - 1)
                    print_updated_list(updated_list)
                    filled_idx.remove(idx_fst - 1)
            else:
                print('Wrong Index! Try Again')
                input_at(user)
        except:
            print('Wrong Index! Try Again')
            input_at(user)
    else:
        os.system('cls')
        print_updated_list(r1)
        print('Player X Chance')
        try:
            idx_fst = int(input('Input from 1-9 where to place your sign = '))
            if idx_fst in range(1, 10):
                if idx_fst - 1 not in filled_idx:
                    print('Location Filled')
                    input_at(user)
                else:
                    updated_list = put_idx_player2(idx_fst - 1)
                    print_updated_list(updated_list)
                    filled_idx.remove(idx_fst - 1)
            else:
                print('Wrong Index! Try Again')
                input_at(user)
        except:
            print('Wrong Index! Try Again')
            input_at(user)


def put_idx_player1(idx):
    if idx == 0:
        r1[0] = 'O'
    elif idx == 1:
        r1[1] = 'O'
    elif idx == 2:
        r1[2] = 'O'
    elif idx == 3:
        r1[3] = 'O'
    elif idx == 4:
        r1[4] = 'O'
    elif idx == 5:
        r1[5] = 'O'
    elif idx == 6:
        r1[6] = 'O'
    elif idx == 7:
        r1[7] = 'O'
    elif idx == 8:
        r1[8] = 'O'
    else:
        'Wrong Index'

    return r1


def put_idx_player2(idx):
    if idx == 0:
        r1[0] = 'X'
    elif idx == 1:
        r1[1] = 'X'
    elif idx == 2:
        r1[2] = 'X'
    elif idx == 3:
        r1[3] = 'X'
    elif idx == 4:
        r1[4] = 'X'
    elif idx == 5:
        r1[5] = 'X'
    elif idx == 6:
        r1[6] = 'X'
    elif idx == 7:
        r1[7] = 'X'
    elif idx == 8:
        r1[8] = 'X'
    else:
        'Wrong Index'

    return r1


def print_updated_list(u_list):
    print(f"{u_list[0]}  | {u_list[1]} | {u_list[2]}")
    print('--- --- ---')
    print(f"{u_list[3]}  | {u_list[4]} | {u_list[5]}")
    print('--- --- ---')
    print(f"{u_list[6]}  | {u_list[7]} | {u_list[8]}")


count = 0
while True:
    if r1[0] == 'O' and r1[1] == 'O' and r1[2] == 'O':
        print('Player 1 wins')
        break
    elif r1[0] == 'X' and r1[1] == 'X' and r1[2] == 'X':
        print('Player 2 wins')
        break
    elif r1[3] == 'O' and r1[4] == 'O' and r1[5] == 'O':
        print('Player 1 wins')
        break
    elif r1[3] == 'X' and r1[4] == 'X' and r1[5] == 'X':
        print('Player 2 wins')
        break
    elif r1[6] == 'O' and r1[7] == 'O' and r1[8] == 'O':
        print('Player 1 wins')
        break
    elif r1[6] == 'X' and r1[7] == 'X' and r1[8] == 'X':
        print('Player 2 wins')
        break
    elif r1[0] == 'O' and r1[3] == 'O' and r1[6] == 'O':
        print('Player 1 wins')
        break
    elif r1[0] == 'X' and r1[3] == 'X' and r1[6] == 'X':
        print('Player 2 wins')
        break
    elif r1[1] == 'O' and r1[4] == 'O' and r1[7] == 'O':
        print('Player 1 wins')
        break
    elif r1[1] == 'X' and r1[4] == 'X' and r1[7] == 'X':
        print('Player 2 wins')
        break
    elif r1[2] == 'O' and r1[5] == 'O' and r1[8] == 'O':
        print('Player 1 wins')
        break
    elif r1[2] == 'X' and r1[5] == 'X' and r1[8] == 'X':
        print('Player 2 wins')
        break
    elif r1[0] == 'O' and r1[4] == 'O' and r1[8] == 'O':
        print('Player 1 wins')
        break
    elif r1[0] == 'X' and r1[4] == 'X' and r1[8] == 'X':
        print('Player 2 wins')
        break
    elif r1[2] == 'O' and r1[4] == 'O' and r1[6] == 'O':
        print('Player 1 wins')
        break
    elif r1[2] == 'X' and r1[4] == 'X' and r1[6] == 'X':
        print('Player 2 wins')
        break
    else:
        if count <= 9:
            if len(filled_idx) != 0:
                input_at(count)
                count += 1
            else:
                print("!Game Draw!")
                break
        else:
            print("!!Game Draw!!")
            break
