def palindrome_check():
  user_phrase = input("Zadejte slovo, které chcete zkontrolovat: ").split(" ")
  join_phrase = "".join(user_phrase).lower()

  def validate():
    if join_phrase == join_phrase[::-1]:
      return True
    else:
      return False
  validate()

  if validate():
    join_phrase = " ".join(user_phrase).lower()
    print(f"Slovo či fráze '{join_phrase}' JE palindrom")
  else:
    join_phrase = " ".join(user_phrase).lower()
    print(f"Slovo či fráze '{join_phrase}' NENÍ palindrom")

palindrome_check()
