import random


# Create the class Tamagotchi
class Tamagotchi:

    def __init__(self, name):

        self.name = name

        # life & care parameters
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2
        self.sleep = False
        self.alive = True

    # Define the method eat, when the creature eats
    def eat(self):

        # Check if there is food available
        if self.food > 1:

            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print(f"{self.name} has eaten.")

        elif self.food == 0:
            print("No food available")

        # make sure hunger won't take any negative value
        self.hunger = 0 if self.hunger < 0 else self.hunger

    # when the creature wants to play, this method governs the action
    def play(self):

        # declare the game's possible answers
        answers = ("scissors", "paper", "rock")

        # random number which will be the creature guess
        num = random.randint(0, 2)

        # player's move, it's supposed to input a number between 0 and 2
        move = int(
            input(f"{self.name} wants to play scissors-paper-rock. Make a guess!")
        )

        # Print the moves
        print(f"{self.name} guess: {answers[num]}")
        print(f"Your guess: {answers[move]}")

        # The boredom decreases when playing in different degrees depending on the result
        if num == move:
            print("Tie!")
            self.boredom -= 2

        elif answers[num] == answers[move - 1]:
            print(f"{self.name} WINS!")
            self.boredom -= 3

        else:
            print("You WIN!")
            self.boredom = 1

        # Ensure boredom is never negative
        self.boredom = 0 if self.boredom < 0 else self.boredom

    # Creature sleeping
    def sleeping(self):

        # sleeping mode
        self.sleep = True
        self.tiredness -= 3
        self.boredom -= 2

        print("The creature is sleeping...")

        # return values to 0 when negative
        self.tiredness = 0 if self.tiredness < 0 else self.tiredness
        self.boredom = 0 if self.boredom < 0 else self.boredom

    # waking up
    def wake_up(self):

        num = random.randint(0, 2)

        # The creature wakes up if the generated random number is zero
        if num == 0:

            print(f"{self.name} is awake.")
            self.sleep = False
            self.boredom = 0

        else:

            print(f"{self.name} is fast asleep.")
            self.sleeping()

    # Bath function for cleaning the creature
    def bath(self):

        self.dirtiness = 0
        print(f"{self.name} has taken a bath.")

    def search_food(self):

        found_food = random.randint(0, 4)

        self.food += found_food
        self.dirtiness += 2

        # print the meals found
        meals = "meals" if found_food != 1 else "meal"
        print(f"{self.name} has found {found_food} {meals}")

    # show values
    def show_values(self):

        print(f"Name: {self.name}")
        print(50 * "*")
        print("")

        print(f"Hunger: {self.hunger}")
        print(f"Boredom: {self.boredom}")
        print(f"Tiredness: {self.tiredness}")
        print(f"Dirtiness: {self.dirtiness}")

        print("")
        print(50 * "*")
        print(f"Meals: {self.food}")
        print(50 * "*")
        print("")

        if self.sleep == True:
            print(f"{self.name} is now sleeping.")
        else:
            print(f"{self.name} is awake.")

    # Difficulty will vary the parameters depending on the difficulty level
    def difficulty(self, level):

        if not 1 <= level <= 5:
            raise ValueError("Difficulty level must be between 1 and 5!")

        else:

            # increase hunger and dirtiness
            self.hunger += random.randint(0, level)
            self.dirtiness += random.randint(0, level)

            # increase boredom and tiredness when awake
            if self.sleep != True:

                self.boredom += random.randint(0, level)
                self.tiredness += random.randint(0, level)

    # Death
    def death(self):

        if self.hunger == 10:
            print(f"{self.name} starved to death.")

        elif self.dirtiness == 10:
            print(f"{self.name} collapsed from exhaustion and never woke up.")

        elif self.boredom == 10:
            print(f"{self.name} was so bored that it gave up on life.")

        elif self.tiredness == 10:
            print(f"{self.name} collapsed from exhaustion and never woke up.")
