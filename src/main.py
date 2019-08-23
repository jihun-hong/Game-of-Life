def main():
    print("Welcome to the Game of Life!\n@Created by Jihun Hong\n")

    while True:
        # Receive input from user.
        mode = input("Please choose (custom, random, quit): ")
        mode = mode.lower()

        if mode == "quit":
            print("See you next time, my friend!")
            break

        # If input not valid, send error.
        if mode not in ['custom', 'random']:
            print("Wrong Input! Error ...")
            continue

        if mode == "custom":
            file = input("Please enter file name: ")
            while True:


        if mode == "random":
            print("Welcome to random mode! ...")





if __name__ == "__main__":
    main()
