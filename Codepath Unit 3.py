# def is_valid_post_format(posts):
#   pairs = {
#     '(':')', 
#     '{':'}',
#     '[':']'
# }
  
#   stack = []

#   for post in posts:

#     if post in "({[":
      
#       stack.append(post)

#     elif post in ")}]":
#       if not stack or pairs[stack.pop()] != post:
#         return False
#   return not stack
      

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))


# def manage_stage_changes(changes):
#   scheduled = []
#   recent = None

  

#   for change in changes:
#     decision = change.split()
#     if decision[0] == "Schedule":
#       scheduled.append(decision[1])
#     elif decision[0] == "Cancel":
#       if scheduled:
#         recent = scheduled.pop()
#     elif decision[0] == "Rescheduled":
#       if recent is not None:
#         scheduled.append(recent)

#   return scheduled



# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


# def booth_navigation(clues):
#     stack = []
#     for path in clues:
#       if path == 'back': 
#           if stack:
#             stack.pop()
#       else:
#         stack.append(path)
#     return stack

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

import random
def patientlog():
  patient_list = {}

  while True:
    patientID = input("Please enter your hospiital ID: ")
    if patientID == '':
      break

    name = input("Please enter your full name: ")
    patient_list[patientID] = {"Name": name, "Vision Test Result": "Pending"}

    print("\nIntial Patient List (Before Eye Test): ")

    for patientID, details in patient_list.items():
      print(f"ID: {patientID} - Name: {details['Name']} - Vision Test Result: {details['Vision Test Result']}")

    for patientID in patient_list:

      patient_list[patientID]['Vision Test Result'] = "Need Glasses" if random.random() < 0.2 else "Clear Vision"

    print("\nUpadated Patient List (After Eye Test): ")
    
    for patientID, details in patient_list.items():
      print(f"ID: {patientID} - Name: {details['Name']} - Vision Test Result: {details['Vision Test Result']}")


patientlog()

import random

def eye_clinic_with_retest():
    patient_list = {}
    
    # Step 1: Input patients
    while True:
        patientID = input("Enter Patient ID (or press Enter to finish): ")
        if patientID == '':
            break
        
        name = input("Enter Patient Name: ")
        
        # Add patient to the list with initial status
        patient_list[patientID] = {"Name": name, "Vision Test Result": "Pending"}
    
    # Step 2: Print initial patient list (Pending)
    print("\nInitial Patient List (Before Eye Test):")
    for patientID, details in patient_list.items():
        print(f"ID: {patientID} - Name: {details['Name']} - Vision Test Result: {details['Vision Test Result']}")
    
    # Step 3: First round of testing
    print("\n--- First Vision Test ---")
    for patientID in patient_list:
        patient_list[patientID]["Vision Test Result"] = "Needs Glasses" if random.random() < 0.2 else "Clear Vision"
    
    # Step 4: Identify who needs a retest
    retest_patients = [pid for pid, details in patient_list.items() if details["Vision Test Result"] == "Needs Glasses"]
    
    print("\nPatients who need a retest:", retest_patients)
    
    # Step 5: Retest those who failed
    print("\n--- Retesting Patients ---")
    for patientID in retest_patients:
        print(f"Retesting Patient ID: {patientID} - Name: {patient_list[patientID]['Name']}")
        result = "Needs Glasses" if random.random() < 0.2 else "Clear Vision"
        patient_list[patientID]["Vision Test Result"] = result
        print(f"Final Result: {result}")
    
    # Step 6: Print final results
    print("\n--- Final Patient List After Retests ---")
    for patientID, details in patient_list.items():
        print(f"ID: {patientID} - Name: {details['Name']} - Final Vision Test Result: {details['Vision Test Result']}")
        
# Run the Eye Clinic simulation with retest
eye_clinic_with_retest()

