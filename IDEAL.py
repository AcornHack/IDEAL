# Has the user input data to develop a schedule [GenZ Hackathon 26/1/19]

userSchedule = open("userSchedule.txt","r") # Opens the user schedule data base 

def initialise(): # Checks if it is the user's first time using the app
  with open("userData.txt","r") as user:
    file = user.readlines()
    global first
    first = True # Defaults to True
    if len(file) == 0:
      first = True
    else:
      first = False
    if first == True:
      startup()
    else:
      home()

def startup(): # A signup page that requests data from the user to use for the timetable  
  
  name = input("What is your name?\n")
  hours = int(input("How many hours would you like to spend revising a day?\n"))
  days = input("What days would you like to revise on? E.g Monday - Friday -> 1 1 1 1 1 0 0\n")
  activities = int(input("How many subjects would you like to focus on?\n"))
  toDo = ""

  for i in range(0,activities): # Makes a list of the activies done by the user
    subject = input ("What subject are you doing?\n")
    toDo =  toDo + subject + " "
  with open("userData.txt","w") as user:
    user.write(name+"\n"+str(hours)+"\n"+days+"\n"+str(activities)+"\n"+toDo)
  home()
def calculateTimetable(hours, activities, days, toDo): # AI Powered Function
  "A Function That Generates A Timetable Using Artificial Intelligence"
  schedule = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  days = days.split(" ")
  return [day for day,flag in zip(schedule,days) if flag == "1"] 
def home():
  with open("userData.txt","r") as user:
    file = user.readlines()
    if first == False:
      global name, hours, days, activities
      name = file[0].strip("\n")
      hours = file[1].strip("\n")
      days = file[2].strip("\n")
      activities = file[3].strip("\n")
      toDo = file[4].strip("\n")
      print ("Welcome back "+name+"!")
      with open("userSchedule.txt","r") as userSchedule:
        schedule = userSchedule.readlines()
        print (calculateTimetable(hours, activities, days, toDo))
        print (toDo)
        print ("Revise each subject for",int(hours)/int(activities),"hours!")
    else:
      name = file[0].strip("\n")
      hours = file[1].strip("\n")
      days = file[2].strip("\n")
      activities = file[3].strip("\n")
      toDo = file[4].strip("\n")                     
      print ("Welcome "+name+"!")
      schedule = calculateTimetable(hours, activities, days, toDo)
      with open("userSchedule.txt","w") as userSchedule:
        userSchedule.write("\n".join(schedule))
      print (schedule)
      print ("ToDo: "+toDo)
      print ("Revise each subject for "+str(int(hours)/int(activities))+" hours!")

initialise()
