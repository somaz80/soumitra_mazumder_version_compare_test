class InvalidVersionFormatError(Exception):

    def __init__(self, message):
        self.message = message


class VersionCompare:

    def __init__(self):
        self.version_string_a = None
        self.version_string_b = None

    def __get_int_value_of_last_indices_values__(self, list_value):
        str_out = ''
        for i in list_value:
            str_out += i
        return int(str_out)

    def __get_bigger_list_after_looping__(self, version_a_list, version_b_list, loop_counter):

        # if the supplied loop_counter value is less than length of version a list
        if (len(version_a_list) > loop_counter) and (
                self.__get_int_value_of_last_indices_values__(version_a_list[loop_counter:]) > 0):

            return self.version_string_a
        # if the supplied loop_counter value is less than length of version b list
        elif (len(version_b_list) > loop_counter) and (
                self.__get_int_value_of_last_indices_values__(version_b_list[loop_counter:]) > 0):

            return self.version_string_b
        else:
            # otherwise return 'EQ' for equal
            return 'EQ'

    def compare_versions_input(self, version_a_list, version_b_list):
        position = 0

        # a if a < b else b
        try:
            # set the loop counter to the smallest of versions
            loop_counter = len(version_a_list) if len(version_a_list) < len(version_b_list) else len(version_b_list)
            # infinite loop to check on the list
            while True:
                # get the integer value from the positions
                int_at_pos_a = int(version_a_list[position])
                int_at_pos_b = int(version_b_list[position])
                # if position value of integer is same at both the lists then increase the counter and  continue
                if int_at_pos_a == int_at_pos_b:
                    position += 1
                    if position < loop_counter:
                        continue
                    else:
                        # just in case we have exhausted the small list,
                        # we have to check what is left from the bigger list
                        return self.__get_bigger_list_after_looping__(version_a_list, version_b_list, loop_counter)
                # if we find that integer value at position a is bigger than position b,
                # then return the value of version string a
                elif int_at_pos_a > int_at_pos_b:
                    return self.version_string_a
                # if we find that integer value at position b is bigger than position a,
                # then return the value of version string b
                else:
                    return self.version_string_b
        except ValueError:
            # Raise custom error for invalid version format string
            print('Invalid version string format supplied')
            raise InvalidVersionFormatError('Invalid version string format supplied')

    # this method takes two version strings as input and returns two lists of them by splitting based on '.'.
    def get_version_string_as_list(self, version_string_a, version_string_b):
        version_a_list = version_string_a.split('.')
        version_b_list = version_string_b.split('.')
        self.version_string_a = version_string_a
        self.version_string_b = version_string_b
        return version_a_list, version_b_list


# main method for standalone run
def main():
    print("python main function")
    version_string_a = '1.3.2.1'
    version_string_b = '1.3.2.1.3'
    version_compare = VersionCompare()
    version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)
    return_version_string = version_compare.compare_versions_input(version_a_list, version_b_list)
    print(return_version_string)


if __name__ == '__main__':
    main()
