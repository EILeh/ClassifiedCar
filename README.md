ClassifiedCar

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
