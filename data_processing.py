from utils import read_input, add_zeros_and_convert_to_array, remove_columns, replace_first_column_with_indexes

def process_input(input_filename):
    input_lines = read_input(input_filename)
    modified_array = add_zeros_and_convert_to_array(input_lines)

    columns_to_remove = [2, 4, 6, 7]

    modified_array_removed = remove_columns(modified_array, columns_to_remove)
    modified_array_final = replace_first_column_with_indexes(modified_array_removed)

    return modified_array_final

def create_dicts(modified_array_final):
    B_array = modified_array_final[1:, :2]
    A_array = modified_array_final[2:, :3]
    D_array = modified_array_final[3:, :4]

    B_dict = {f'B{i+1}': list(map(int, B_array[i])) for i in range(B_array.shape[0])}
    A_dict = {f'A{i+1}': list(map(int, A_array[i])) for i in range(A_array.shape[0])}
    D_dict = {f'D{i+1}': list(map(int, D_array[i])) for i in range(D_array.shape[0])}

    return B_dict, A_dict, D_dict
