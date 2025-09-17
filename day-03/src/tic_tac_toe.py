def tic_tac_toe():
    '''
    Игра в крестики-нолики для двух игроков.
    '''
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    def print_board():
        for row in board:
            print('|'.join(row))
            print('-' * 5)
    
    def check_win():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return True
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return True
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        return False
    
    moves_count = 0
    while moves_count < 9:
        print_board()
        row = int(input(f'Игрок {current_player}, выбери строку (0-2): '))
        col = int(input(f'Игрок {current_player}, выбери столбец (0-2): '))
        
        if board[row][col] == ' ':
            board[row][col] = current_player
            moves_count += 1
            if check_win():
                print_board()
                print(f'Игрок {current_player} победил!')
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Ячейка уже занята!')
    
    print_board()
    print('Ничья!')
    

if __name__ == '__main__':
    tic_tac_toe()