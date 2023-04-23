def main():
    singleProb = input("What is the probability of the desired event?\n")
    chances = input("How many chances do you have?\n")
    totalProb = (float(singleProb) ** float(chances)) * 100
    print("There is a " + str(totalProb) + "% chance that event will occur at least once.")

if __name__ == "__main__":
    main()