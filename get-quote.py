import random
def primary():

   # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
#here we know last number of array is 13
    last = 13
#If you want to add or remove quotes from your text file, you could change the last variable to update automatically:last = len(quotes) - 1

    rnd = random.randint(0, last)
    print(quotes[rnd])

if __name__== "__main__":
  primary()
