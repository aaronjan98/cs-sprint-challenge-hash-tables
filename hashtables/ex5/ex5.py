import re

file_paths = {}

def finder(files, queries):
    # loop through every file path
    for file in files:
        # find index to the branch file
        name_aftr_this_i = file.rfind("/")
        # file_name is from the files directory
        file_name = file[name_aftr_this_i+1:]
        # create key value pairs of paths and file names
        file_paths.update({file_name: file})
        # print('path:', file_paths)
    found_queries = []
    # look through the queries
    for query in queries:
        # if query does exist in file_paths return in a new list
        try:
            found_queries.append(file_paths[query])
        except (RuntimeError, TypeError, NameError, KeyError):
            continue
    print('found:', found_queries)
    return found_queries


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
