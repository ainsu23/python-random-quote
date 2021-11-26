import random
last = 13
rmd = random.randint(0, last)
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rmd])

if __name__== "__main__":
  primary()
