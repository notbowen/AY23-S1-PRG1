# Written by: Hu Bowen (S10255800)
# Date: 25 June 2023
# Class: CSF02

# Pet simulator 2023

# Pet class
class Pet:
    def __init__(self) -> None:
        self.menu = ['Feed', 'Play', 'Rest', 'Status']
        self.status = [3, 3, 3]
        self.title = ['hungry', 'happiness', 'energy']
        self.msg = ['Nom nom nom', 'XD', 'Zzzzz']

    def show_and_select_options(self) -> int:
        """ List the options to the user and returns the choice the user selected """
        for i, action in enumerate(self.menu):
            print("({}) {}".format(i+1, action))

        return int(input("Please select an option: "))

    def perform_action(self, action: int) -> None:
        """ Performs an action based on the index """
        action -= 1

        if action == 3:
            self.show_status()
            return

        self.status = [star - 1 for star in self.status]
        self.status[action] += 2

        print(self.msg[action])

    def show_status(self) -> None:
        """ Shows the status of the pet """
        for title, status in zip(self.title, self.status):
            print("{:12}".format(title), end="")
            print("*" * status, end="." * (5 - status))
            print()


# Init pet and let user interact with it
pet = Pet()
print("Digipet")

while True:
    action = pet.show_and_select_options()
    pet.perform_action(action)
