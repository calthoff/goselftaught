authors = []

def collect_authors():
  answer = None
  while answer != "q":
      answer = input("Who is your favorite author?")
      authors.append(answer)
    
print(authors)
