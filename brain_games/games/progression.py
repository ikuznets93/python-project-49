import random


def progression_game():
    element_of_progression = random.randint(1, 100)
    step_of_progression = random.randint(1, 10)
    length_of_progression = 10
    position_of_unknown = random.randint(0, length_of_progression - 1)

    progression = []
    for position in range(length_of_progression):
        if position == position_of_unknown:
            progression.append('..')
            answer = str(element_of_progression)
        else:
            progression.append(element_of_progression) 
        element_of_progression += step_of_progression
    question = ' '.join(map(str, progression))
    return (question, answer)