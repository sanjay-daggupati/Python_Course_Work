import allprograms

programs = {
    1: allprograms.automorphic_number,
    2: allprograms.roman_to_integer,
    3: allprograms.symmetric_matrix,
    4: allprograms.caesar_cipher,
    5: allprograms.harshad_number,
    6: allprograms.char_frequency,
    7: allprograms.extract_domain,
    8: allprograms.rectangle_overlap,
    9: allprograms.flatten_list,
    10: allprograms.count_pos_neg_zero
}

def display_menu():
    print("------ FUNCTION MENU ------")
    print("1. Check Automorphic Number")
    print("2. Convert Roman Numeral to Integer")
    print("3. Check Symmetric Matrix")
    print("4. Caesar Cipher Encryption")
    print("5. Check Harshad Number")
    print("6. Count Character Frequency")
    print("7. Extract Domain from Email")
    print("8. Check Rectangle Overlap")
    print("9. Flatten Nested List")
    print("10. Count Positive, Negative, Zero in List")
    print("0. Exit")
    print("----------------------------")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
