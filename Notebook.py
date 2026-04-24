notes = []

# Create
# Read
# Update
# Delete
while True:
    command = str(input("Enter a command : "))
    if command == "c1":
        # Create
        note = str(input("Enter a note: "))
        notes.append(note)
    elif command == "c2":
        # 2
        note = str(input("Enter a note: "))
        notes.insert(0,note)
        # Read
        # 1
    elif command == "r1":
        for note in notes:
            print(note)
        # 2
    elif command == "r2":
        for i in range(len(notes)):
            print(i, notes[i])

        # Update
        # 1
    elif command == "u1":
        index = int(input("Enter a index : "))
        new_note = str(input("Enter a new note : "))
        notes[index] = new_note

        # 2 По повному збігу старого напису kjkkkkkkkk
    elif command == "u2":
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                notes[i] = new_note

        # 3 По частковому збігу старого напису
    elif command == "u3":
        old_note = str(input("Enter a note : "))
        new_note = str(input("Enter a new note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                notes[i] = new_note

        # Delete
        # 1
    elif command == "d1":
        index = int(input("Enter a index : "))
        del notes[index]

        # 2 По повному збігу старого напису
    elif command == "d2":
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note == notes[i]:
                del notes[i]

            # 3 По частковому збігу старого напису
    elif command == "d3":
        old_note = str(input("Enter a note : "))
        for i in range(len(notes)):
            if old_note in notes[i]:
                del notes[i]