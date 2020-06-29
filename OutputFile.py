"""
Creates an output file

For the insertsort and mergesort files
"""


def output_file(name, input_array):
    with open(name, 'w+') as out_file:
        # Write the input_Array to the file
        for array in input_array:
            str_array = ' '.join([str(x) for x in array])
            str_array += '\n'
            out_file.writelines(str_array)

        return True

