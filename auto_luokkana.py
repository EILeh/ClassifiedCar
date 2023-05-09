"""
Classified car

The program contains the class Car. The main function also includes an object of
the Car class and a call of the method print_information. The attributes
__gas and __odometer are used for saving the internal state of the car object,
i.e. the amount of gas in the car's tank and the number of kilometers in the
car's odometer. The constructor initiates values that ensure that the tank is
empty and the odometer shows a zero. The method print_information prints how
much gas the car's tank contains and what does the car's odometer show. The
information is printed to the specificity of one decimal. A car refuelling
method called fill and the method uses the amount of refuelled gas as a
parameter. The Car class ensures that you can't surpass the size of the tank.
If you try to do so, the exceeding amount of gas is wasted. The car also
prints the error message "You cannot remove gas from the tank" if you attempt to
refuel the car with a negative amount. A method called drive uses
information on how many kilometers to drive as a parameter. If you try to
drive further than where the gas can take you, the travelling ends when the tank
is emptied. The method increments the value of the attribute __odometer for the
length of the trip that you drove. The Car class prints the error message
"You cannot travel a negative distance" if you attempt to enter a negative
input here.

Writer of the program: EILeh

"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption, gas=0.0, odometer=0.0):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        :param gas: float, the amount of gas in the tank
        :param odometer: float, the amount of kilometer you can drive
        with the amount of gas left
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas_left = gas
        self.__odometer_atm = odometer


    def gas(self, gas):
        """
        Deducts the gas in the tank.
        :param gas: amount of gas
        :return: how much gas is left
        """
        self.__gas_left = gas

        return self.__gas_left


    def odometer(self, odometer):
        """
        Deducts the kilometers you can drive with the amount of gas in the tank.
        :param odometer: kilometers you can drive
        :return: kilometer
        """
        self.__odometer_atm = odometer

        return self.__odometer_atm


    def print_information(self):
        """
        Prints the amount of gas in the tank and the car's consumption.
        """
        print(f"The tank contains {self.__gas_left} liters of gas and"
              f" the odometer shows {self.__odometer_atm} kilometers.")


    def fill(self, fill):
        """
        How much gas does the driver want to fill in the tank and adds the
        amount to it. If driver fills more than the car can be filled, the
        rest goes waste.
        :param fill: float, the amount of gas to be filled
        :return: float, returns the amount of gas after tank has been filled
        """
        self.__fill = fill

        if fill < 0:
            print("You cannot remove gas from the tank")

            return self.__gas_left


        if fill > self.__tank_volume:
            self.__gas_left = self.__tank_volume

            return self.__tank_volume


        if (fill + self.__gas_left) > self.__tank_volume:
            self.__gas_left = self.__tank_volume

        else:
            self.__gas_left = self.__gas_left + self.__fill

            return self.__gas_left


    def drive(self, distance):
        """
        The distance that driver wants to drive.
        :param distance: float, the distance the driver wants to drive
        :return: float, updated distance
        """
        self.__drive = distance

        if distance < 0:
            print("You cannot travel a negative distance")

            return self.__odometer_atm


        elif self.__drive > (self.__gas_left * self.__consumption):
            self.__odometer_atm = self.__odometer_atm + (self.__gas_left *
                                                         self.__consumption)
            self.__gas_left = 0.0

            return self.__odometer_atm


        elif distance < (self.__gas_left + self.__drive):
            self.__odometer_atm = self.__odometer_atm + distance
            self.__gas_left = self.__gas_left - (self.__drive / 10)

            return self.__gas_left



        else:
            self.__odometer_atm = self.__odometer_atm + self.__drive

            return self.__odometer_atm


def main():

    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    # Here we define the variable car which is an object initiated
    # from the class Car (its type is Car). This is the point where the
    # constructor of the class Car (i.e. the method that is named __init__)
    # is called automatically behind the scenes to give an initial
    # value for the Car object we are creating!

    car = Car(tank_size, gas_consumption)

    # In this program we only need one car object but it is possible
    # to create multiple objects from one class. For example we could
    # create more objects if we needed them:
    #
    #     lightning_mcqueen = Car(20, 30)
    #     canyonero = Car(200, 400)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()