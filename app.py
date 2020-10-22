print("encouragement bot :)")
print()

name = input("What is your name?")
print("Hello " + name)

while True:
  description = input("How was your day?")
  list_of_words = description.split()
  
  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("it's okay to feel sad sometimes. it will get better")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("glad that you are happy. continue smiling :)")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("it has been a long day, get some rest")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("take a break when u need it. u can do it !!")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("talk to a friend,I'm sure their more than willing to help you!")
      counter += 1
      
    if counter == 0:
          output = "Sorry I don't really understand. Please use different words?"
    elif counter == 1:
          output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  
   
  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

