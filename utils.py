import numpy as np
import io

# Function to read input from a file
def read_input(filename):
    with open(filename, 'r') as file:
        return file.readlines()

# Function to add zeros and convert lines to array
def add_zeros_and_convert_to_array(lines):
    modified_lines = []

    # Loop through lines and modify as needed
    for index, line in enumerate(lines):
        if index == 0:
            modified_lines.append(line.strip() + ' 0 0 0 0 0 0 0')
        elif index == 1:
            modified_lines.append(line.strip() + ' 0 0 0 0 0')
        elif index == 2:
            modified_lines.append(line.strip() + ' 0 0 0')
        else:
            modified_lines.append(line.strip())

    # Convert modified content to array
    modified_content = '\n'.join(modified_lines)
    modified_content_io = io.StringIO(modified_content)
    return np.genfromtxt(modified_content_io, dtype=str)

# Function to remove columns from an array
def remove_columns(array, columns_to_remove):
    return np.delete(array, columns_to_remove, axis=1)

# Function to replace first column with indexes
def replace_first_column_with_indexes(array):
    indexes = np.arange(1, array.shape[0] + 1)
    return np.column_stack((indexes, array[:, 1:]))

# Function to calculate bond length between two atom coordinates
def calculate_bond_length(atom1_coords, atom2_coords):
    return np.sqrt(np.sum((atom1_coords - atom2_coords)**2))

# Function to calculate angle between three atom coordinates
def calculate_angle(atom1_coords, atom2_coords, atom3_coords):
    vec1 = atom1_coords - atom2_coords
    vec2 = atom3_coords - atom2_coords
    cosine_theta = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    angle_radians = np.arccos(np.clip(cosine_theta, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

# Function to calculate dihedral angle between four atom coordinates
def calculate_dihedral(atom1_coords, atom2_coords, atom3_coords, atom4_coords):
    vec1 = atom1_coords - atom2_coords
    vec2 = atom3_coords - atom2_coords
    vec3 = atom4_coords - atom3_coords

    n1 = np.cross(vec1, vec2)
    n2 = np.cross(vec2, vec3)
    m1 = np.cross(n1, vec2)
    x = np.dot(n1, n2)
    y = np.dot(m1, n2)

    dihedral_radians = np.arctan2(y, x)
    dihedral_degrees = np.degrees(dihedral_radians)
    return dihedral_degrees

# Function to read XYZ file and return atom coordinates dictionary
def read_xyz_file(filename):
    with open(filename, 'r') as file:
        num_rows = int(file.readline().strip())  # Read the number of rows
        lines = file.readlines()

        if len(lines) != num_rows:
            raise ValueError("Number of rows in the file does not match the expected value.")

        atom_coordinates = {}

        for index, line in enumerate(lines):
            parts = line.strip().split()
            col2 = float(parts[1])
            col3 = float(parts[2])
            col4 = float(parts[3])

            atom_coordinates[index + 1] = (col2, col3, col4)

        return atom_coordinates
