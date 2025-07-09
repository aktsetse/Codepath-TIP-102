# def lineup(artists, set_times):
#     times = {}
#     for i in range(len(artists)):
#            times[artists[i]] = set_times[i] 
    
#     return times

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# Problem 3
# def total_sales(ticket_sales):
#     total = 0
#     for ticket in ticket_sales:
#         total += ticket_sales[ticket]
#     return total
         

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

# problem 4

# def identify_conflicts(venue1_schedule, venue2_schedule):
#     conflits = {}
#     for venue in venue1_schedule:
#         if venue1_schedule[venue] in venue2_schedule:
#             conflits[venue] = venue
#         return conflits


# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))


# def most_endangered(species_list):
#     for i in species_list:
#         if species_list[i] < species_list[i + 1]:
#             return species_list[i]


# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))

# Problem 2
# def count_endangered_species(endangered_species, observed_species):
#     count = 0
#     endangered_species.split()
#     observed_species.split()
#     for i in observed_species:
#         if i in endangered_species:
#             count += 1
    
#     return count

# def count_endangered_species(endangered_species, observed_species):
#     count = 0
#     for species in endangered_species:
#         count += observed_species.count(species)
#     return count


# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2)) 

# def navigate_research_station(station_layout, observations):
    
  

# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"

# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))

std_courses = []

def addcourses():
    while True:
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")  
        
        
        std_courses.append([course_name, course_code])

        print("Course added!")

        more_courses = input("Do you have additional courses to add? (Yes / No): ").strip().lower()
        if more_courses != 'yes':
            break  
    
    print("All courses added successfully!")

def studentreg():
    student = [] 
    
    name = input("Enter your name: ")
    GID_num = input("Enter your GID number: ") 
    semester = input("Which semester are you in? (Fall / Spring): ").strip().capitalize()

    if semester == 'Spring':
        addcourses()
        student.append(name)
        student.append(GID_num)
        student.append(semester)
        student.append(std_courses[:]) 

        print("Student Registration Complete!")
        print(student)
    
    else:
        print("Program stopped! This register is for the Spring semester.")

studentreg()