# class Dog:
#     def _init_(self, name, breed, language):
#         self.name = name
#         self.breed = breed
#         self.language = language

#     def bark(self):
#         if self.language == "English":
#             return "Woof!"
        
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

# # Instantiate your villager here

# apollo = Villager("Apollo", "Eagle", "pah")
# def greet_player(self, player_name):
#     return f"{ self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 



# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah

# # Add code here to link the above nodes


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_item(head, item):
    
#     cursor = head
#     prev = Node(None)
    
#     while cursor.value != item:
#         cursor = cursor.next
#         if cursor == None:
#             return head
#         if prev.value == None:
#             prev = head
#         else:
#             prev = prev.next
#     if prev.value == None:
#         return head.next
    
#     prev.next = cursor.next

#     return head



    


# slingshot = Node("Slingshot")
# peaches = Node("Peaches")
# beetle = Node("Scarab Beetle")
# slingshot.next = peaches
# peaches.next = beetle

# # Linked List: slingshot -> peaches -> beetle
# print_linked_list(delete_item(slingshot, "Peaches"))

# # Linked List: slingshot -> beetle
# print_linked_list(delete_item(slingshot, "Triceratops Torso"))


from tkinter import *

root = Tk()
root.title("Ghost Image")

# Constant values
canvas_width = 400
canvas_height = 300

head_radius = canvas_width/4
body_width = head_radius * 2
body_height = canvas_height/3
num_feet = 3
foot_radius = body_width / (num_feet * 2)
body_color = "red"

eye_radius = head_radius/4
eye_offset = eye_radius * 1.5
eye_color = "white"
pupil_radius = eye_radius/2.5
pupil_left_offset = eye_radius
pupil_right_offset = pupil_radius * 5
pupil_color = "blue"

# Create canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw ghost head
canvas.create_oval(canvas_width/2 - head_radius, 50, canvas_width/2 + head_radius, 50 + head_radius * 2, fill=body_color, outline=body_color)

# Draw ghost body
canvas.create_rectangle(canvas_width/2 - head_radius, 50 + head_radius, canvas_width/2 + head_radius, 50 + head_radius + body_height, fill=body_color, outline=body_color)

# Draw ghost feet
for i in range(num_feet):
    x = (canvas_width/2 - head_radius) + i * (2 * foot_radius)
    canvas.create_oval(x, 50 + head_radius + body_height - foot_radius, x + 2 * foot_radius, 50 + head_radius + body_height + foot_radius, fill=body_color, outline=body_color)

# Draw eyes
left_eye_x = canvas_width/2 - eye_offset
right_eye_x = canvas_width/2 + eye_offset
canvas.create_oval(left_eye_x - eye_radius, 80, left_eye_x + eye_radius, 80 + 2 * eye_radius, fill=eye_color, outline=eye_color)
canvas.create_oval(right_eye_x - eye_radius, 80, right_eye_x + eye_radius, 80 + 2 * eye_radius, fill=eye_color, outline=eye_color)

# Draw pupils
canvas.create_oval(left_eye_x - pupil_radius + pupil_left_offset, 100, left_eye_x + pupil_radius + pupil_left_offset, 100 + 2 * pupil_radius, fill=pupil_color, outline=pupil_color)
canvas.create_oval(right_eye_x - pupil_radius + pupil_right_offset, 100, right_eye_x + pupil_radius + pupil_right_offset, 100 + 2 * pupil_radius, fill=pupil_color, outline=pupil_color)

root.mainloop()

