import time
import os
import random


def guess_the_num():
    os.system('cls')
    def game():
        print('\ni am thinking of a number in between 0 and 15,\n\nLets see if you can guess that in three chances or not\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
        number=random.randint(0,15)
        for i in range(0,3):
            num=int(input('\nGuess a number: '))
            if num==number:
                print('\tyayyy!!! Correct guess pal...')
                break
            elif (num>number):
                print('\tthe number you entered is too high')
            elif (num<number):
                print('\tthe number you entered is too low')
            else:
                for w in range(0,2):
                    print('\tYOU GOTTA DO THAT AGAIN   :)')
        print('the correct answer is '+str(number)+'\n\n')
    game()
    print('1.wanna play again\n2.exit')
    choice=int(input('\nEnter your CHOICE...'))
    if choice==1:
        game()
    else:
        menu()

def palindrome():
         os.system('cls')
         print('For those who donno about PALINDROME...\nIts nothing but a word,phrase or a sequence that reads the same backwards as forward\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
         n=int(input("Enter any number:"))
         temp=n
         rev=0
         while(n>0):
             dig=n%10
             rev=rev*10+dig
             n=n//10
         if(temp==rev):
             print("\n\n\t\tThe number is a palindrome!\n\n")
         elif (temp!=rev):
             print("\n\n\t\tThe number isn't a palindrome!\n\n")
         input('Press enter to continue...\n\n')
         menu()


def reverse2():
         os.system('cls')
         print('i am gonna reverse the given integer for you...\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
         n=int(input("Enter any number:"))
         temp=n
         rev=0
         while(n>0):
             dig=n%10
             rev=rev*10+dig
             n=n//10
         print('\n\n\t\tthe reverse of the given number is ',rev,'\n\n')
         input('Press enter to continue...\n\n')
         menu()

def armstrong():
         os.system('cls')
         print('ARMSTRONG is nothing but sum of cubes of each digit of a specified integer eg: 371=3**3+7**3=1**3...\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
         n=int(input("Enter any number:"))
         temp=n
         sum=0
         while(n!=0):
                  r=n%10
                  sum=sum+r**3
                  n=n//10
         if temp==sum:
                  print('\n\n\t\tthe given number is ARM STRONG\n\n')
         else:
                  print('\n\n\t\tthe given number is NOT armstrong\n\n')
         input('Press enter to continue...\n\n')
         menu()

def factorial():
         os.system('cls')
         print('eg: factorial of 5 == 5*4*3*2*1...\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
         n=int(input('Enter any number: '))
         fact=1
         for i in range(1,n+1):
                  fact=fact*i
         print('\n\n\t\tthe factorial of the given number is ',fact,'\n\n')
         input('Press enter to continue...\n\n')
         menu()

def fabinocci():
         os.system('cls')
         print('next number in interger series is added serially until specified interger is reached...\n\n\tMAKE SURE YOU ENTERED AN INTEGER, IF NOT IT WILL BE EXITED\n\n')
         a=0
         cnt=0
         b=1
         n=int(input('Enter the sequence limit : '))
         print('the sequence of the fabinocci series is : \n',a,'\n',b,'\n')
         while cnt!=n-2:
                  c=a+b
                  print(' ',c,'\n')
                  temp=b
                  b=c
                  a=temp
                  cnt=cnt+1
         input('Press enter to continue...\n\n')
         menu()



def menu():
         os.system('cls')
         #time.sleep(1)
         print("\n1.Palindrome Number\n2.Reverse Number \n3.Armstrong Number \n4.Factorial \n5.Fibonacci Series \n6.Guess the number game \n7.Exit ")
         choice=str(input('Enter Your Choice : '))

         if choice=='1':
                  palindrome()
         elif choice=='2':
                  reverse2()
         elif choice=='3':
                  armstrong()
         elif choice=='4':
                  factorial()
         elif choice=='5':
                  fabinocci()
         elif choice=='6':
                  guess_the_num()
         elif choice=='7':
                  print('\n\n\t\tTHANK YOU!!\n\n')
                  time.sleep(3)
                  exit()
         else:
                print("Invalid entry!!!!")
                time.sleep(2)
                menu()






def main():
        def forgot_password():
         os.system('cls')
         answer1="mahatma gandhi"
         answer2="raj vadeghar"
         '''def change_password():
                  new_password=str(input('new password : '))
                  def confirm():      
                                    
                                    confirm_password=str(input('confirm password : '))
                                    if new_password==confirm_password:
                                                        password=confirm_password
                                                        main()
                                    else:
                                                        print('the password is not matched\n')
                                                        confirm()
                  confirm()'''
         print('Hint : MAKE SURE ALL LETTERS ARE SMALL and NO SPACES please\n')
         def question_2():
              os.system('cls')
              question2=str(input('Question-2 : Who wrote this program ??\n'))
              
              if question2==answer2:
                    #change_password()
                    time.sleep(2)
                    print('\n\n\t\tThe password is \'Raj@vadeghar\' <----')
                    time.sleep(2)
                    main()
                    
              else:
                    question_2()
         def question_1():
             os.system('cls')
             question1=str(input('Question-1 : Who is the father of our nation ??\n'))
             
             if question1==answer1:
                       question_2()
             else:
                       question_1()
        
         question1=str(input('Question-1 : Who is the father of our nation ??\n'))
         if question1==answer1:
                  question_2()
         else:
                  question_1()
        def wrong_password():
          os.system('cls')
          print('1.Retry \n2.Forgot Password\n\n')
          enter=str(input('Enter Your Choice : '))
          if enter=='1':
             os.system('cls')
             main()
          elif enter=='2':
             os.system('cls')
             forgot_password()
          else:
             os.system('cls')
             print('Invaild number!!!\n')
             wrong_password()
        password='12345678'
        input_pass=str(input('Enter the password : '))
        if input_pass == password:
           print('\n\t\tCorrect Password!!!')
           time.sleep(1)
           print('\n\n\t\tAccess Granted!')
           time.sleep(1)
           menu()
        else:
           print('\n\n\t\tWrong Password!!')
           time.sleep(1)
           print('\n\n\t\tAccess Denied!!')
           time.sleep(1)
           print('\n\n\t\tPlease Enter the Correct Password!!')
           time.sleep(1)
           wrong_password()

main()
    
