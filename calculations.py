import numpy as np
from utils import calculate_bond_length, calculate_angle, calculate_dihedral, read_xyz_file

def calculate_values(B_dict, A_dict, D_dict, xyz_filename):
    try:
        # Read the XYZ file containing cartesian coordinates
        atom_coordinates = read_xyz_file(xyz_filename)

        # Calculate bond lengths for B
        bond_lengths_B = {}
        for key, value in B_dict.items():
            atom1_index, atom2_index = value
            atom1_coords = np.array(atom_coordinates[atom1_index])
            atom2_coords = np.array(atom_coordinates[atom2_index])
            bond_length = calculate_bond_length(atom1_coords, atom2_coords)
            bond_lengths_B[key] = bond_length

        # Calculate angles for A
        angles_A = {}
        for key, value in A_dict.items():
            atom1_index, atom2_index, atom3_index = value
            atom1_coords = np.array(atom_coordinates[atom1_index])
            atom2_coords = np.array(atom_coordinates[atom2_index])
            atom3_coords = np.array(atom_coordinates[atom3_index])
            angle = calculate_angle(atom1_coords, atom2_coords, atom3_coords)
            angles_A[key] = angle

        # Calculate dihedrals for D
        dihedrals_D = {}
        for key, value in D_dict.items():
            atom1_index, atom2_index, atom3_index, atom4_index = value
            atom1_coords = np.array(atom_coordinates[atom1_index])
            atom2_coords = np.array(atom_coordinates[atom2_index])
            atom3_coords = np.array(atom_coordinates[atom3_index])
            atom4_coords = np.array(atom_coordinates[atom4_index])
            dihedral = calculate_dihedral(atom1_coords, atom2_coords, atom3_coords, atom4_coords)
            dihedrals_D[key] = dihedral

        #Print the calculated values
        #print("\nCalculated bond lengths for B:")
        #print(bond_lengths_B)
        #print("\nCalculated angles for A:")
        #print(angles_A)
        #print("\nCalculated dihedrals for D:")
        #print(dihedrals_D)

    

        return bond_lengths_B, angles_A, dihedrals_D # Return the calculated values

    except ValueError as e:
        print(f"Error: {e}")
