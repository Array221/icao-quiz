#!/usr/bin/env python3

import time as tm
import random as rnd

import colorama as col


icao = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrott', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}


def main():
    print('\nWelcome to ICAO phonetic alphabet quiz.\n')
    print('You will be asked about words corresponding letters in ICAO alphabet in random order.')
    print('When letter is displayed, just type correct word that is used in ICAO.')
    print('After filling out quiz, your results and average time of solving one question will be displayed.\n')
    input('If you\'re ready, press ENTER to continue...')
    print('\n')

    answers, averageTime = take_quiz()

    display_results(answers, averageTime)

    input('\nPress ENTER to continue...')
    print('\n')


def take_quiz():
    answers = {}

    timeElapsed = 0

    icaoCopy = icao.copy()
    for i in range(1, len(icao) + 1):
        letter = rnd.choice(list(icaoCopy.keys()))

        startTime = tm.time()
        answers[letter] = input(f'[{i:>2}/{len(icao)}] {letter}: ')
        endTime = tm.time()

        timeElapsed += endTime - startTime
        icaoCopy.pop(letter)

    return answers, (timeElapsed / len(icao))


def display_results(answers, averageTime):
    print(f'\n{" RESULTS ":=^25}')

    errors = 0

    for letter, correct in icao.items():
        answer = answers[letter].capitalize()

        if answer == correct:
            print(f'{col.Fore.GREEN}{letter}: {answer}{col.Style.RESET_ALL}')
        else:
            errors += 1
            if answer == '':
                answer = '[NO RESPONSE]'
            print(f'{col.Fore.RED}{letter}: {answer:<13} {col.Fore.LIGHTBLACK_EX}({correct}){col.Style.RESET_ALL}')

    print(f'\nYou\'ve got {col.Fore.CYAN}{len(icao) - errors}{col.Style.RESET_ALL} of {col.Fore.CYAN}{len(icao)}{col.Style.RESET_ALL} words right.')
    print(f'Your average time per word is {col.Fore.CYAN}{averageTime:.2f}s{col.Style.RESET_ALL}.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        quit(0)
