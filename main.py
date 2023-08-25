from calculations import calculate_values
from data_processing import process_input, create_dicts

def main():
    input_filename = 'connect.txt'
    xyz_filename = 'cart_coord.xyz'

    # Process input data
    modified_array_final = process_input(input_filename)

    # Create dictionaries for B, A, and D arrays
    B_dict, A_dict, D_dict = create_dicts(modified_array_final)

    # Calculate bond lengths, angles, and dihedrals
    bond_lengths_B, angles_A, dihedrals_D = calculate_values(B_dict, A_dict, D_dict, xyz_filename)

    #Print the calculated values
    print("\nCalculated bond lengths for B:")
    print(bond_lengths_B)
    print("\nCalculated angles for A:")
    print(angles_A)
    print("\nCalculated dihedrals for D:")
    print(dihedrals_D)

    # Save the calculated values to a text file
    with open('calculated_values.txt', 'w') as output_file:
        output_file.write("Calculated bond lengths for B:\n")
        output_file.write(str(bond_lengths_B) + '\n')
        output_file.write("Calculated angles for A:\n")
        output_file.write(str(angles_A) + '\n')
        output_file.write("Calculated dihedrals for D:\n")
        output_file.write(str(dihedrals_D) + '\n')

if __name__ == "__main__":
    main()
