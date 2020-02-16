from time import time as counter_of_time


def time_of_the_execution(file_name=None):
    print(f'Saving to the {file_name}')

    def decorator(function):

        def inner():
            starting_point = counter_of_time()
            function()
            working_time = counter_of_time() - starting_point
            print(f'function {function.__name__} took {working_time} seconds to execute')
            if file_name is None:
                with open('text.txt', 'w+') as recording_file:
                    recording_file.write(f'function {function.__name__} took {working_time} seconds to execute')
            else:
                with open(file_name, 'w+') as recording_file:
                    recording_file.write(f'function {function.__name__} took {working_time} seconds to execute')

        return inner

    return decorator
