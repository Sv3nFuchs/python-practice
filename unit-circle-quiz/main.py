# This code was created through collaboration with a partner.
import random
angles = ["pi/6", "pi/4", "pi/3", "pi/2", "2pi/3", "3pi/4", "5pi/6", "pi", "7pi/6", "5pi/4", "4pi/3", "3pi/2", "5pi/3", "7pi/4", "11pi/6", "2pi"]
coordinates = ["(√3/2, 1/2)", "(√2/2, √2/2)", "(1/2, √3/2)", "(0, 1)", "(-1/2, √3/2)", "(-√2/2, √2/2)", "(-√3/2, 1/2)", "(-1, 0)", "(-√3/2, -1/2)", "(-√2/2, -√2/2)", "(-1/2, √3/2)", "(0, -1)", "(1/2, -√3/2)", "(√2/2, -√2/2)", "(√3/2, -1/2)", "(1, 0)"]

def unit_circle(score, out_of):
    random_element = random.choice(angles)
    index = angles.index(random_element)
    user_answer = input("What are the coordinates of " + random_element + "? Enter as (x, y): ")
    answer = coordinates[index]
    for i in range(len(user_answer)):
        if "sqrt" in user_answer:
            user_answer = user_answer.replace("sqrt", "√")
    if user_answer == answer:
        score += 1
        out_of += 1
        print("That was correct! Your score so far is: " + str(score) + "/" + str(out_of) + ".")
        print()
    elif user_answer == "Exit":
        final_percent = (score / out_of) * 100
        print("Your final score was: " + str(score) + "/" + str(out_of) + ".")
        print("That score is equivalent to a: " + str(final_percent) + "%.")
        print("Thank you for playing! Good luck in the future with studying the Unit Circle.")
        return score, out_of
    else:
        out_of += 1
        print("That response was incorrect. The correct coordinates are: " + str(answer) + ".")
        print("Your score is: " + str(score) + "/" + str(out_of) + ".")
        print()
    return unit_circle(score, out_of)
unit_circle(0, 0)
