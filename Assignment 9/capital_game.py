import random


def main():
    capitals = {
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Wisconsin': 'Madison',
        'Michigan': 'Lansing',
        'Ohio': 'Columbus',
        'Iowa': 'Des Moines',
        'Hawaii': 'Honolulu',
        'Wyoming': 'Cheyenne',
        'New Hampshire': 'Concord',
        'Texas': 'Austin',
        'California': 'Sacramento',
        'Florida': 'Tallahassee'
    }

    states = list(capitals.keys())
    correct = 0
    incorrect = 0

    state = random.choice(states)
    answer = input(f'What is the capital of {state}? (or enter 0 to quit): ').strip()

    while answer != '0':
        if answer.lower() == capitals[state].lower():
            print('That is correct.')
            correct += 1
        else:
            print('That is incorrect.')
            incorrect += 1

        state = random.choice(states)
        answer = input(f'What is the capital of {state}? (or enter 0 to quit): ').strip()

    print(f'You had {correct} correct responses and {incorrect} incorrect responses.')


if __name__ == '__main__':
    main()