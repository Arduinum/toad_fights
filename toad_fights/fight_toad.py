from asyncio import run, create_task, gather
from random import randint

from сlass_toad import random_class, perform_attack


async def series_fights(count_fights: int):
    """Серия боёв"""

    toad_1_win = 0
    toad_2_win = 0

    for _ in range(count_fights):
        toad_1 = random_class()
        toad_2 = random_class()
        
        while True:
            # Определяем, кто начнет бой
            attacker_index = randint(1, 2)
            attacker = toad_1 if attacker_index == 1 else toad_2
            defender = toad_2 if attacker_index == 1 else toad_1
            
            # Жаба, которая атакует совершает атаку
            if perform_attack(attacker, defender):
                # добавление очка победителю
                if defender().get_health() == 0:
                    if attacker_index == 1:
                        toad_1_win += 1
                    else:
                        toad_2_win += 1
                    break

            # Жаба, которая защищается отвечает атакой
            if perform_attack(defender, attacker):
                # добавление очка победителю
                if attacker().get_health() == 0:
                    if attacker_index == 1:
                        toad_1_win += 1
                    else:
                        toad_2_win += 1
                    break
           
    # имена жаб из Наруто
    wins_board = f'Гамабунта - {toad_1_win} | Гамакен {toad_2_win}'
    winner = 'Ничья'

    if toad_1_win > toad_2_win:
        winner = 'Победил - Гамабунта'
    elif toad_1_win < toad_2_win:
        winner = 'Победил - Гамакен'

    print('---------------------------')
    print(f'{wins_board}\n{winner}')
    print('---------------------------\n')


async def arena():
    """Арена для сражения жаб"""
    
    try:
        battles = []

        # Запускаем несколько серий боев асинхронно
        for _ in range(2):
            battle = create_task(series_fights(count_fights=100))
            battles.append(battle)
        
        # Ожидаем завершения всех боев
        await gather(*battles)
    except Exception as err:
        print(f'Ошибка - жабы убежали во время битвы!\nВсему виной - {err}.')


if __name__ == '__main__':
    # запускаем бои на арене
    run(arena())
