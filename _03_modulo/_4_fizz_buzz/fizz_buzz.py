"""
 TODO: Fizz Buzz
   In this project, we're going to build FizzBuzz. It's a children's game where
   you count from 1 to 20. Easy, right? Here's the catch:
   -
   Instead of saying a number that is divisible by 3, say "Fizz".
   And instead of saying a number that is divisible by 5, say "Buzz".
   For numbers divisible by both 3 and 5, say "FizzBuzz".
   -
   Print your results to the console.
   -
   If your code is correct, the output will be:
   -
   1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz
"""
q = 1

for i in range(20):
    if q % 15 == 0:
        print("FizzBuzz")
        q = q + 1
    if q % 3 == 0:
        print("Fizz")
        q = q + 1
    if q % 5 == 0:
        print("Buzz")
    else:
        print(q)
    q = q + 1
    if q == 21:
        exit()


