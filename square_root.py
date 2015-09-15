from random import randint

def approx_sqrt(num):
    if num == '':
        return "I'm sorry Dave, I'm afraid I can't do that."
    for char in num:
        if ((ord(char) < 48 or ord(char) > 57) and ord(char)!=45) or int(num) == 0:
            return "I'm sorry Dave, I'm afraid I can't do that."

    guess = float(randint(1,abs(int(num))))
    previous_guess = 0.0
    iteration = 0
    iteration_guess = []
    target = int(num)
    if target > 0:
        while float("{0:.3}".format(previous_guess)) != float("{0:.3}".format(guess)):
            previous_guess, guess = guess, (1/2)*(guess+(target/guess))
            iteration +=1
            iteration_guess.append([iteration, guess])
    else:
        target = abs(target)
        while float("{0:.3}".format(previous_guess)) != float("{0:.3}".format(guess)):
            previous_guess, guess = guess, (1/2)*(guess+(target/guess))
            iteration +=1
            iteration_guess.append([iteration, complex(guess,1)])
    return iteration_guess

print(approx_sqrt(input('What number do you want to square root? ')))
