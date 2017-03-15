import sys

def query_yes_no(question, default="yes", assumed=False):
    # Ref: http://code.activestate.com/recipes/577058/
    valid = {
            "yes": True,
            "y": True,
            "ye": True,
            "no": False,
            "n": False 
            }
    if default == None:
        prompt = " [y/n]:"
    elif default == "yes":
        prompt = " [Y/n]:"
    elif default == "no":
        prompt = " [y/N]:"
    else:
        raise ValueError("invalid default answer: '{0}'".format(default))

    while True:
        if(assumed):
            choice = valid[default]
            return choice
        else:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid.keys():
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

def query_integer(question, default, assumed=False):
    prompt = ' [default: {0}]:'.format(default)
    if(not isinstance(default, int)):
        raise ValueError("invalid default answer: '{0}'".format(default))
    while True:
        if(assumed):
            return default
        else:
            sys.stdout.write(question + prompt)
            value = int(input())
            if(not isinstance(value, int)):
                sys.stdout.write("Please respond with integer value.\n")
            elif value == '':
                return default
            else:
                return value
