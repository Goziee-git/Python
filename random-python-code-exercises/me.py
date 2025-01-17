#def datatype(data):
#   match data:
#      case int():
#         print("you entered an integer", data)
#      case _:
#        print("Invalid data type")

#datatype(4.5)

def weekday(day):
   match day:
      case "Monday" | "Tuesday":
         print("start of the week")
      case "wednesday" | "thursday" | "friday":
         print("midweek days")
      case _:
         print("must be a weekend")

weekday("Monday")
weekday("sunday")


      