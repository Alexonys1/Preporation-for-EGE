def win(s: int) -> bool:
    """Возвращает True, если позиция абсолютно выигрышная."""
    if (51 <= s + 1 <= 60) or (51 <= s + 2 <= 60) or (51 <= 2*s <= 60):
        return True
    else:
        return False


def loss(s: int) -> bool:
    """Возвращает True, если эта позиция абсолютно проигрышная и
       все следующие позиции абсолютно выигрышные."""
    if not win(s) and win(s + 1) and win(s + 2) and win(2 * s):
        return True
    else:
        return False


def petya_will_win_on_second_move(s: int) -> bool:
    """Возвращает True, если Петя выиграет на своём втором ходе."""
    if loss(s + 1) or loss(s + 2) or loss(2 * s):
        return True
    else:
        return False


def vania_will_win_on_second_move(s: int) -> bool:
    if petya_will_win_on_second_move(s + 1) or \
            petya_will_win_on_second_move(s + 2) or \
            petya_will_win_on_second_move(2*s):
        return True
    else:
        return False


def new(s):
    if vania_will_win_on_second_move(s + 1) or \
            vania_will_win_on_second_move(s + 2) or \
            vania_will_win_on_second_move(2*s):
        return True
    else:
        return False


for s in range(1, 51):
    if new(s):
        print(s)
