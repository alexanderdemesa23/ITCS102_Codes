
anime_type = ["isekai", "adventure", "romance", "scifi"]
anime_title = []

while True:
  ans = input("do you know any anime? ---> (yes/no)")
  if ans.lower() == 'yes':
    print("what type of anime? pick in the list")
    for x in anime_type:
      print(x)

    a_type =input ("type --> ")

    title = input("what is title? --> ")
    anime_title.append(title)
    continue
  else:
    print("thank you!")
    break



















