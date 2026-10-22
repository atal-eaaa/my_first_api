import random 

def roll_a_die():
    """
    Roll a die once
    """
    return(random.randint(1,6))


def roll_the_dice(n):
    """
    Returns list of n dice rolls
    """
    dice=[]
    for i in range(n):
        dice.append(roll_a_die())
    return(dice)

def counter(dice):
    """
    Counts how many of each numbers is in dice roll
    """
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in dice:
        if die == 1:
            count[1] += 1
        elif die == 2:
            count[2] += 1
        elif die == 3:
            count[3] += 1
        elif die == 4:
            count[4] += 1
        elif die == 5:
            count[5] += 1
        else:
            count[6] += 1

    return(count)


def score_yatzy(dice):
    """
    Evaluates a list of 5 dice (e.g., [2, 3, 3, 3, 5]) 
    and returns a dictionary of possible Yatzy categories and scores.
    """
    counts = counter(dice)
    scores = {}
    
    # Upper section (1 to 6)
    for i in range(1, 7):
        scores[f"ones_to_sixes_{i}"] = counts[i] * i

    # Three of a kind: 3 dice of the same value
    for val, count in counts.items():
        if count >= 3:
            scores["three_of_a_kind"] = 3*val
            break
    else:
        scores["three_of_a_kind"] = 0

    # Four of a kind: 4 dice of the same value
    for val, count in counts.items():
        if count >= 4:
            scores["four_of_a_kind"] = 4*val
            break
    else:
        scores["four_of_a_kind"] = 0

    # Full house: Three of a kind + a Pair
    vals = list(counts.values())
    if 3 in vals and 2 in vals:
        scores["full_house"] = sum(dice)
    else:
        scores["full_house"] = 0

    # Small straight: 1, 2, 3, 4, 5 (15 points)
    if sorted(dice) == [1, 2, 3, 4, 5]:
        scores["small_straight"] = 15
    else:
        scores["small_straight"] = 0

    # Large straight: 2, 3, 4, 5, 6 (20 points)
    if sorted(dice) == [2, 3, 4, 5, 6]:
        scores["large_straight"] = 20
    else:
        scores["large_straight"] = 0

    # Yatzy: 5 dice of the same value (50 points)
    if 5 in counts.values():
        scores["yatzy"] = 50
    else:
        scores["yatzy"] = 0

    # Chance: sum of all dice
    scores["chance"] = sum(dice)

    return scores


if __name__ == '__main__':
    # try it out
    my_dice = [2, 3, 6, 3, 5]
    
    print(counter(my_dice))
    print(score_yatzy(my_dice))