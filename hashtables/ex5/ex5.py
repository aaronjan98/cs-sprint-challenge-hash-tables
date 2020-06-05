import re

file_paths = {}

def finder(files, queries):
    # loop through every file path
    for root_file_path in files:
        # find index to the root_file_path
        name_aftr_this_i = root_file_path.rfind("/")
        # file_name is from the files directory
        file_name = root_file_path[name_aftr_this_i+1:]

        if file_paths != {}:
            if file_name not in file_paths.keys():
                # create key value pairs of paths and file names
                file_paths.update({file_name: [root_file_path]})
            else:
                file_paths[file_name].append(root_file_path)
        else:
            file_paths.update({file_name: [root_file_path]})
        
    found_queries = []
    # look through the queries
    for query in queries:
        # if query does exist in file_paths return it in a new list
        try:
            # loop through file_paths to check for multiple files with the same name
            # if len(file_paths.values(query))
            # print(len(file_paths[query]))
            item = file_paths[query]
            if len(file_paths[query]) < 2:
                found_queries.append(item[0])
            else:
                for key, value in file_paths.items():
                    # if the query matches the key, append file_paths' value
                    if key == query:
                        # need to loop through the values of file_path
                        for i in value:
                            found_queries.append(i)
        except (RuntimeError, TypeError, NameError, KeyError):
            continue
    return found_queries


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/bin/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
