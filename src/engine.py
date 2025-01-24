from interface import make_board, show, cpu_turn, keep_playing, human_turn, clear, sleep, home, green

CPU_DELAY = 0.75


def open_cells(b):
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    cs = []
    for p in b:
        if type(p) is int:
            cs.append(p)
    return tuple(cs)


def first_open_cell(b):
    """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
    cs = open_cells(b)
    if cs != []:
        return cs[0]
    else:
        return None

def cpu_vs_cpu(strategy_x, strategy_o):
    """Game mode 0: run the game between two CPU opponents"""
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', strategy_x)
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', strategy_o)
        if not keep_playing(board):
            break
    show(board)


def cpu_vs_human(cpu_strategy):
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', cpu_strategy)
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_human():
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_cpu(cpu_strategy):
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', cpu_strategy)
        if not keep_playing(board):
            break
    show(board)


def game(strategy_x, strategy_o):
    global CPU_DELAY
    clear()
    print(green("GREETINGS PROFESSOR FALKEN\n"))
    sleep(CPU_DELAY)
    print(green("SHALL WE PLAY A GAME?\n"))
    sleep(CPU_DELAY * 2)
    orig_delay = CPU_DELAY
    clear()
    for _ in range(40):
        board = make_board()
        clear()
        while True:
            if CPU_DELAY > 0.025:
                CPU_DELAY *= 0.95
            home()
            show(board)
            board = cpu_turn(board, 'X', strategy_x, verbose=False)
            if not keep_playing(board):
                break
            home()
            show(board)
            board = cpu_turn(board, 'O', strategy_o, verbose=False)
            if not keep_playing(board):
                break
        clear()
        show(board)
        keep_playing(board)
        sleep(CPU_DELAY)
    CPU_DELAY = orig_delay
    sleep(CPU_DELAY)
    print(green("A STRANGE GAME.\n"))
    sleep(CPU_DELAY * 2)
    print(green("THE ONLY WINNING MOVE IS NOT TO PLAY.\n"))
    sleep(CPU_DELAY * 2)
    print(green("HOW ABOUT A NICE GAME OF CHESS?\n"))
    sleep(CPU_DELAY * 5)