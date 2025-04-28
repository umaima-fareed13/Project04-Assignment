def main():
    anton : int = 21 # Anton' age is given as 21 years old
    beth : int = 6 + anton # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = 20 + beth # chen is 20 years older than Beth, so add 20 to Beth's age to get chen's
    drew : int = chen + anton # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan : int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to chen's


    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

if __name__ == "__main__":
    main()