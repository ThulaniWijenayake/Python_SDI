# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Student ID: w1953288
# Date: 13/12/2022


#Initializing variables
progress_n=0
trailer_n=0
retriever_n=0
exclude_n=0
total = 0

#List
progressionList = []

#dictionary
student_dictionary = {}

#studentversion
def student_version(pass_cs,defer_cs,fail_cs):
    #checking if the total is correct
    if sum([pass_cs,defer_cs,fail_cs])!=120:
        print("Total Incorrect.")
    else:
        #progression checking
        if (pass_cs ==120):
            print("Progress")
        
        elif (pass_cs ==100 and{ defer_cs==20 or fail_cs==20}):
            print("Progress (module trailer)")
        
        elif (fail_cs < 80):
            print("Do not Progress – module retriever")
        elif (fail_cs >= 80):
            print("Exclude")
        else:
            print("Invalid option")


#staffversion            
def staff_version(pass_cs,defer_cs,fail_cs):
    global progress_n,trailer_n,retriever_n,exclude_n,total
    progression_outcome = "Invalid Option"
    #checking if the total is correct
    
    if sum([pass_cs,defer_cs,fail_cs])!=120:
        progression_outcome="Total incorrect"
        print("Total Incorrect.")
    else:
        #progression checking
        if(pass_cs==120):
            progression_outcome="Progress"
            print("Progress")
            progress_n = progress_n+ 1
    
        elif (pass_cs ==100 and{ defer_cs==20 or fail_cs==20}):
            progression_outcome="Progress (module trailer)"
            print("Progress (module trailer)")
            trailer_n = trailer_n+ 1
                
        elif (fail_cs < 80):
            progression_outcome = "Do not Progress – module retriever"
            print("Do not Progress – module retriever")
            retriever_n = retriever_n+1
                        
        elif (fail_cs >=80):
            progression_outcome = "Exclude"
            print("Exclude")
            exclude_n = exclude_n+1
        total +=1 
    return progression_outcome
    
      
        
#printing Histogram
def printHistogram():
    global progress_n, trailer_n, retriver_n, exclude_n, total
    print("-"*100)
    print("Histogram")
    print("Progress ",progress_n,"\t: ",progress_n*"*")
    print("Trailer ",trailer_n,"\t: ",trailer_n*"*")
    print("Retriver ",retriever_n,"\t: ",retriever_n*"*")
    print("Excluded ",exclude_n,"\t: ",exclude_n*"*")
    print()
    print(total," outcomes in total.")
    print("-"*100)
   
def staff_validation():
    marksList = []
    pass_cs,defer_cs,fail_cs = 0,0,0
    #Asking for student ID
    student_id = input("Enter your Student ID : ")
    
    #validation
    
    while True:
        pass_cs = int(input("Enter your total PASS credits : " ))
        if pass_cs in range(0,140,20):
            print()
            break
        else:
            print("Out of range")
            continue
        
    while True:
        defer_cs = int(input("Enter your total DEFER credits : " ))
        if defer_cs in range(0,140,20):
            print()
            break
        else:
            print("Out of range")
            continue
        
    while True:
        fail_cs =int(input("Enter your total FAIL credits : " ))
        if fail_cs in range(0,140,20):
            print()
            break
        else:
            print("Out of range") 
            continue

    progression_outcome=staff_version(pass_cs,defer_cs,fail_cs)
    # appending credit scores to the list
    if progression_outcome != 'Total incorrect':
        marksList=[pass_cs]
        marksList.append(defer_cs)
        marksList.append(fail_cs)
	
        marksList.append(progression_outcome)
           
   

    #adding items to the student_dictionary
        try:
            student_dictionary[student_id] = marksList
        except KeyError:
            print("Duplicate Entry!")

        progressionList.append(marksList)
            

#Rerunning
def rerun():
    global progress_n, trailer_n, retriver_n, exclude_n, total
    print()

    while True:
        staff_validation()
        print("Would you like to enter another set of data ?")
        CHOICE = str(input("Enter 'y' for yes and 'q' to quit and view results: "))
        CHOICE = CHOICE.lower()
        #Yes
        if CHOICE == 'y':
            continue
        #Quit
        elif CHOICE=='q':
            printHistogram()
            printList()
            writeToFile()
            printDictionary()
            
        else:
            print("Invalid Option")
        
        break
#printing Dictionary
def printDictionary():
    print("-"*100)
    print("Part 4: ")
    dictionary_line = ""
    for student_id, student_marks in student_dictionary.items():
        dictionary_line += f'{student_id} : {student_marks[3]} - {student_marks[0]}, {student_marks[1]}, {student_marks[2]} '
    
    print(dictionary_line)

#Writing to file
def writeToFile():
    f = open("file.txt", "w")

    for strings_list in progressionList:
        pass_str = str(strings_list[0])
        defer_str = str(strings_list[1])
        fail_str = str(strings_list[2])

        file_str = strings_list[3] + " - " + pass_str + ", " + defer_str + ", " + fail_str + "\n"
        f.write(file_str)
    
    f.close()

        
#printing the list
def printList():
    print("Part 2: ")
    for x in progressionList:
        print(x[3]," - ",x[0],", ",x[1],", ",x[2])


def main():
    pass_cs,defer_cs,fail_cs = 0,0,0
    try:
        # Choosing whether the student version or staff member version
        choice= str(input("Student or Staff member(s/sm) : "))
        # For Students
        if choice== 's':
            print()
            print("#Student version")
            while True:
                pass_cs = int(input("Please enter your credit at pass : " ))
                if pass_cs in range(0,140,20):
                    print()
                    break
                else:
                    print("Out of range")
                    continue
            while True:
                defer_cs = int(input("Please enter your credit at defer : " )) 
                if defer_cs in range(0,140,20):
                    print()
                    break
                else:
                    print("Out of range")
                    continue

            while True:
                fail_cs =int(input("Please enter your credit at fail : " ))
                if fail_cs in range(0,140,20):
                    print()
                    break
                else:
                    print("Out of range")
                    continue
                
            student_version(pass_cs,defer_cs,fail_cs)
 
        # For Staff members    
        elif choice=='sm':
            print()
            print("#Staff version with Histogram")

            #Rerunning
            rerun() 
        else:
            print("Invalid Option ") 
         
            
    except ValueError:
        print("Integer required! ")   


main()       



            
