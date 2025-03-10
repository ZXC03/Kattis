num_rooms = int(input())
num_idiots = int(input())

leftover_students = num_idiots%num_rooms
students_p_room = num_idiots//num_rooms+1

if students_p_room == 0:
    print(num_idiots*'*')
elif leftover_students == 0:
    for i in range(num_rooms):
        print((students_p_room-1)*'*')
else:
    if leftover_students + 1 == students_p_room:
        for i in range(num_rooms-1):
            print(students_p_room*'*')
        print(leftover_students*'*')
    else:
        students_to_move = students_p_room - leftover_students
        for i in range(students_p_room-students_to_move):
            print(students_p_room*'*')
        for i in range(num_rooms-(students_p_room-students_to_move)):
            print((students_p_room-1)*'*')
