patientData = {
    "P001": {
        "Name": "UMAR ARRASYID",
        "Gender": "Male",
        "Age": 35,
        "Address": "Jakarta",
        "Blood Type": "O"
    },
    "P002": {
        "Name": "MUHAMMAD JUNDULLAH",
        "Gender": "Male",
        "Age": 25,
        "Address": "Bandung",
        "Blood Type": "A"
    },
    "P003": {
        "Name": "GAVIN CHANDRA",
        "Gender": "Male",
        "Age": 20,
        "Address": "Yogyakarta",
        "Blood Type": "B"
    },
    "P004": {
        "Name": "Angel",
        "Gender": "Female",
        "Age": 5,
        "Address": "Surabaya",
        "Blood Type": "A"
    },
     "P005": {
        "Name": "NAJWA SUBHAN",
        "Gender": "Female",
        "Age": 19,
        "Address": "Bekasi",
        "Blood Type": "AB"
    },
    
}



# ---------------Function to read all patient data---------------
def read(sortedByName = False):
    print("\n Patient Data")
    if not patientData:
        print("No data available")
        return
    if sortedByName:
        sortedPatients = sorted(patientData.items(), key = lambda data : data[1]['Name']) # items() return berupa list berisi key (index 0) dan value (index1)  return berupa list, sorted
    else:
        sortedPatients = patientData.items()
    
    for patient_ID, data in sortedPatients:
        print(f"\nPatient ID\t: {patient_ID}")
        print(f"Name\t\t: {data['Name']}")
        print(f"Gender\t\t: {data['Gender']}")
        print(f"Age\t\t: {data['Age']}")
        print(f"Address\t\t: {data['Address']}")
        print(f"Blood Type\t: {data['Blood Type']}")
        



# -----------FUnction to find patient data by ID-----------
def find():
    if not patientData:
        print("No data availab")
        return
    patient_ID = input("Enter Patient ID to find: ").upper()
    if patient_ID not in patientData:
        print("Patient ID not found.")
    else:
        print(f"\nPatient ID\t: {patient_ID}")
        print(f"Name\t\t: {patientData[patient_ID]['Name']}")
        print(f"Gender\t\t: {patientData[patient_ID]['Gender']}")
        print(f"Age\t\t: {patientData[patient_ID]['Age']}")
        print(f"Address\t\t: {patientData[patient_ID]['Address']}")
        print(f"Blood Type\t: {patientData[patient_ID]['Blood Type']}")




# -----------Function to add new patient data -----------
def add():
    print("\nInput Patient Data")
    # patient ID
    while True:
        patient_ID = input("Enter Patient ID: ").upper()
        if patient_ID in patientData:
            print("Patient ID already exists.")
        elif not patient_ID:
            print("Patient ID cannot be empty")
        else:
            break
        
    # name
    while True:
        name = input("Name\t\t: ").upper()
        if not name:
            print("Name cannot be empty")
        else:
            break

    # gender
    while True:
        gender = input("Gender\t\t: ").capitalize()
        if gender in ['Male', 'Female']:
            break
        else:
            print("Invalid, please enter Male or Female.")
    # age
    while True:
        age = input("Age\t\t: ")
        if age.isdigit() and 0 <= int(age) <=120:
            age = int(age)
            break
        else:
            print("Invalid input. Please enter a valid age")
    # address
    while True:
        address = input("Address\t\t: ")
        if not address:
            print("Address cannot be empty")
        else:
            break
    
    #Blood type
    while True:
        bloodType = input("Blood Type\t: ").upper()
        if bloodType in ['A', 'B', 'AB', 'O']:
            break
        else:
            print("Invalid blood type. Please enter A, B, AB, or O.")

    # Konfirmasi untuk memastikan pengguna ingin menambah data
    confirm = input("Are you sure you want to save the data? (yes/no): ").lower()
    if confirm != 'yes':
        print("Returning to Add submenu.")
        return
    
    patientData[patient_ID] = {
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Address": address,
        "Blood Type": bloodType
    }

    print("Patient data added successfully.")


# -----------Function to update patient data with confirmation after input----------------
def update():
    print("\nUpdate Patient Data")
    # patient ID
    patient_ID = input("Enter Patient ID to update: ").upper()
    if patient_ID not in patientData:
        print("Patient ID not found.")
        return
    print("Enter new data (leave blank to keep current)")
    
    # name
    name = input(f"Name: ({patientData[patient_ID]['Name']}): ").upper()
    
    # gender
    while True:
        gender = input(f"Gender: ({patientData[patient_ID]['Gender']}): ").capitalize()
        if not gender:
            gender = patientData[patient_ID]['Gender']
            break
        elif gender in ['Male', 'Female']:
            break
        else:
            print("Invalid, please enter Male or Female.")

    # age
    while True:
        age = input(f"Age: ({patientData[patient_ID]['Age']}): ")
        if not age:
            age = patientData[patient_ID]['Age']  # Jika kosong, gunakan umur lama
            break
        elif age.isdigit() and 0 <= int(age) <= 120:  # Validasi input umur
            age = int(age)
            break  # Keluar dari loop jika input valid
        else:
            print("Invalid input. Please enter a valid age between 0 and 120.")
    
    # address
    address = input(f"Address: ({patientData[patient_ID]['Address']}): ")
    
    # blood type
    while True:
        bloodType = input(f"Blood Type: ({patientData[patient_ID]['Blood Type']}): ").upper()
        if not bloodType:  # Jika kosong, gunakan data lama
            bloodType = patientData[patient_ID]['Blood Type']
            break
        elif bloodType in ['A', 'B', 'AB', 'O']:
            break
        else:
            print("Invalid blood type. Please enter A, B, AB, or O.")

    confirm = input("Are you sure you want to save the updated data? (yes/no): ").lower()
    if confirm != 'yes':
        print("Returning to Update submenu.")
        return

    if name:
        patientData[patient_ID]['Name'] = name
    if gender:
        patientData[patient_ID]['Gender'] = gender
    if age:
        patientData[patient_ID]['Age'] = age
    if address:
        patientData[patient_ID]['Address'] = address
    if bloodType:
        patientData[patient_ID]['Blood Type'] = bloodType
    print("Patient data updated successfully.")



# ---------------Function for delete patient data---------------
def delete():
    print("\nDeleting Patient Data")
    patient_ID = input("Enter Patient ID to delete: ").upper()
    if patient_ID not in patientData:
        print("Patient ID not found.")
        return
    confirm = input(f"Delete patient data for Patient ID {patient_ID}? (yes/no)")
    if confirm == 'yes':
        del patientData[patient_ID]
        print(f"Patient data with ID {patient_ID} deleted successfully.")
    else:
        print("Deletion cancelled. No data was deleted.")
    
    print("Patient data deleted successfully.")

# ---------------Submenu read patient data---------------
def subMenuRead():
    while True:
        print("\n===============================")
        print("  Submenu Read Patient Data")
        print("=================================")
        print("1. Read All Patient Data")
        print("2. Find Patient Data by ID")
        print("3. Read All Patient Data sort by Name (Ascending)")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4)")
        if choice == '1':
            read()
        elif choice == '2':
            find()
        elif choice == '3':
            read(sortedByName=True)
        elif choice == '4':
            print("Exiting the submenu")
            break
        else:
            print("Invalid choice, please try again.")

# -----------Submenu for deleting patient data---------------
def subMenuDelete():
    while True:
        print("\n===============================")
        print("  Submenu Delete Patient Data")
        print("=================================")
        print("1. Delete Patient Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            delete()
        elif choice == '2':
            print("Exiting the submenu.")
            break
        else:
            print("Invalid choice, please try again.")

# -----------Submenu for updating patient data---------------
def subMenuUpdate():
    while True:
        print("\n===============================")
        print("  Submenu Update Patient Data")
        print("=================================")
        print("1. Update Patient Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            update()
        elif choice == '2':
            print("Exiting the submenu.")
            break
        else:
            print("Invalid choice, please try again.")

# -----------Submenu for adding patient data---------------
def subMenuAdd():
    while True:
        print("\n===============================")
        print("  Submenu Add Patient Data")
        print("=================================")
        print("1. Add Patient Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            add()
        elif choice == '2':
            print("Exiting the submenu.")
            break
        else:
            print("Invalid choice, please try again.")

# --------------- Main Menu---------------
def menu():
    while True:
        print("\n==========================================")
        print("  Hospital Patient Data Application Menu")
        print("============================================")
        print("1. Read Patient Data")
        print("2. Add Patient Data")
        print("3. Update Patient Data")
        print("4. Delete Patient Data")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            subMenuRead()
        elif choice == '2':
            subMenuAdd()
        elif choice == '3':
            subMenuUpdate()
        elif choice == '4':
            subMenuDelete()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

menu()
