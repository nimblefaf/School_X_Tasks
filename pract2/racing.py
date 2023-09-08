from import_this import generate_race_data
import random
from datetime import timedelta

winners_keys: list = []
RACE_DATA = generate_race_data(random.randint(1,10))

def search_for_winners(data: dict) -> list: #возвращает список ключей победителей, от первого места до третьего
    result = ['first', 'second', 'third']
    for key, value in data.items():
        if value['FinishedPlace'] < 4:
            result[int(value['FinishedPlace']) - 1] = key
    if type(result[2]) == str: #удалить плейсхолдер на случай если гонщиков только 2
        del result[2]
    return result

def display_winners(winners: list) -> None:
    first_line:str = f"Выиграл - {RACE_DATA[winners[0]]['RacerName']}!!! Поздравляем!!"
    print(
    "\n" + first_line + "\n" +   # если ставить перед словом \n то IDE начинает ругаться на ASCII
    "-" * len(first_line) +                                                                      # "\nВыиграл" - плохо, "\n" + "Выиграл" - хорошо
    "\n\n" + "Первые три места:\n"
    )
    for i in range(len(winners)):
        print(f"Гонщик на {i+1} месте:")
        print(f"    Имя - {RACE_DATA[winners[i]]['RacerName']}")
        print(f"    Команда - {RACE_DATA[winners[i]]['RacerTeam']}")
        print(f"    Время - {timedelta(seconds=RACE_DATA[winners[i]]['FinishedTimeSeconds'])} (H:M:S)\n")

def main():
    winners_keys = search_for_winners(RACE_DATA)
    display_winners(winners_keys)

if __name__ == "__main__":
    main()