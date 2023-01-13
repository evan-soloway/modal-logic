# variables "a, b, c" represent various premises of argument.
# Arguments are represented mathematically; premise is false if
# less than zero.

class logic:
     def valid(premise_a, premise_b, premise_c, conclusion):
          if premise_a + premise_b + premise_c != conclusion:
               return False
          else:
               return True

     def sound(premise_a, premise_b, premise_c, conclusion):
          if premise_a < 0 or premise_b < 0 or premise_c < 0:
               return False
          else:
               return True
     

def main():

     print("\nYou're constructing an argument. Enter 3 premises for your argument.")

     print("NOTE: Argument is false if less than 0.")

     a, b, c, conclusion = receive_premises_and_argument()

     if logic.valid(a,b,c,conclusion):
          print("\nArgument is valid.")
     else:
          print("\nArgument is not valid.")

     if logic.sound(a,b,c,conclusion):
          print("Argument is sound.")
     else:
          print("Argument is not sound.")

     
           
def receive_premises_and_argument():

     try:

          conclusion = int(input("\nWhat number are you arguing for? "))

          print('\nNOTE: Premise is false if less than 0.')
          
          a = int(input("\n1st Premise: "))
          b = int(input("2nd Premise: "))
          c = int(input("3rd Premise: "))

     except ValueError:
          print("Please enter a number...")
          receive_premises_and_argument()

     except:
          print("ERROR")
          receive_premises_and_argument()
          
     return a, b, c, conclusion

main()
          
          
