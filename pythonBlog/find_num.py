import os
import datetime


def reset_dir():
    if os.getcwd() != '/Users/noahcg/Desktop/ncaldwell17.github.io':
        os.chdir("..")
        reset_dir()
    else:
        return True


def get_if():
    the_list = []
    for the_file in os.listdir("."):
        if the_file.endswith(".html"):
            the_list.append(the_file)
    return the_list


def get_num(a_list, a_name):
    # the key
    the_key = a_name
    # the value
    the_num_in_dir = len(get_if())
    # the dictionary
    the_dict = {}
    the_dict[the_key] = the_num_in_dir
    a_list.append(the_dict)
    return a_list


def get_dirs():
    the_list = []
    for dirname in os.listdir('projects'):
        the_list.append(dirname)
    return the_list


def get_blog_num(a_path):
    the_dir_list = get_dirs()
    # needs to be defined outside function to account for all
    # list of dictionaries
    the_output_list = []
    for the_dir in the_dir_list:
        if the_dir == 'elections':
            os.chdir(a_path + "/elections/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        elif the_dir == 'ai':
            os.chdir(a_path + "/ai/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        elif the_dir == 'geo':
            os.chdir(a_path + "/geo/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        elif the_dir == 'econ':
            os.chdir(a_path + "/econ/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        elif the_dir == 'cyber':
            os.chdir(a_path + "/cyber/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        elif the_dir == 'local':
            os.chdir(a_path + "/local/posts")
            get_num(the_output_list, the_dir)
            reset_dir()
        else:
            print("All directories accounted for")
    return the_output_list


# variables
the_date = datetime.datetime.now().date()
ppath = "projects"

if __name__ == "__main__":
    if os.getcwd() != "/users/noahcg/Desktop/ncaldwell17.github.io":
        os.chdir("/users/noahcg/Desktop/ncaldwell17.github.io")
    print("Here's a list of project posts as of {0}:\n".format(the_date))
    my_outputs = get_blog_num(ppath)
    print(my_outputs)
