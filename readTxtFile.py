"""
A class for reading in the Contents of a file. Used to pass the information to the mergesort and insertsort python files.
"""


class ReadFile:

    def __init__(self, file):

        self.file = file

    def get_contents(self):
        """
        Returns the contents of whatever file is read in
        :return: The contents of whatever file is read in
        """

        contents = []

        with open(self.file, 'r') as file:
            # Loop through the lines and grab the context
            lines = file.readlines()
            for line in lines:

                line = list(line.strip().split(" "))

                # Convert the char values into ints.
                line = [int(x) for x in line]
                # Append the line to a list of lines
                contents.append(line)

            return contents
