from re import search
import nlpcloud
class NLPApp:

  def __init__(self):
    self.__database = {}
    self.__first_menu()

  def __first_menu(self):
    first_input = input("""

    Hi! How would you like to proceed?
    1. Not a member? Register
    2. Already a member? Login
    3. Quit

    """)

    if first_input == "1":
      self.__register()
    elif first_input == "2":
      self.__login()
    else:
      self.__quit()
    
  def __second_menu(self):
    first_input = input("""

    1. NER
    2. Language Detection
    3. Sentiment Analysis
    4. Logout
    
    """)

    if first_input == "1":
      self.__NER()
    elif first_input == "2":
      self.__language_detection()
    elif first_input == "3":
      self.__sentiment_analysis()
    else:
      self.Logout()

  def __register(self):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if email in self.__database:
      print("email already exists")
    else:
      self.__database[email] = [name, password]
      print("registration successful")
      print(self.__database)
      self.__first_menu()

  def __login(self):
    email = input("Enter your email: ")
    if email in self.__database:
      password = input("Enter your password: ")
      if self.__database[email][1] == password:
        print("Login Successful, Welcome to the application")
        self.__second_menu()
      else:
        print("Incorrect Password")
        self.__login()
    else:
      print("Incorrect email")
      self.__login()


  def __NER(self):
    para = input("Enter the paragraph: ")
    search_term = input("what would you lilke to search")

    client = nlpcloud.Client("finetuned-gpt-neox-20b", "523ad8e8b84573d26d033e11620af7012add3b9c", gpu=True, lang="en")
    response = client.entities(para, searched_entity = search_term)
    
    print(response)

  def __language_detection(self):
    pass
  
  def __sentiment_analysis(self):
    para = input("Enter the paragraph")

    client = nlpcloud.Client("distilbert-base-uncased-emotion", "523ad8e8b84573d26d033e11620af7012add3b9c", gpu=False, lang="en")
    response = client.sentiment(para)

    L = []
    for i in response['scored_labels']:
        L.append(i['score'])
    index = sorted(list(enumerate(L)),key = lambda x:x[1],reverse = True)[0][0]

    print(response['scored_labels'][index]['label'])
    self.__second_menu()

  def __Logout(self):
    pass
    
  def __quit(self):
    print("exit")

obj = NLPApp()

    