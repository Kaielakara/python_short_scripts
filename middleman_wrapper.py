def wrapper_func(func):


    def debug_logger(*args, **kwargs):
        a = []
        k = []

        for arg in args:
            a.append(arg)

        for key,value in kwargs.items():
            k.append(f"{key}='{value}'")

        new_args = ''.join(a)
        new_kwargs = ', '.join(k)



        print(f"Calling {func.__name__.title()} with args: ({new_args}',) and kwargs: ('{new_kwargs})")

        return func(*args, **kwargs)
    
    return debug_logger


@wrapper_func
def create_post(title, * , content):# the asteriks indicates that everything after the asteriks must be passed as a keyword
    return 


@wrapper_func
def editing(title, *, old_content, new_content):
    return


create_post("My First Post",  content="Hello World")

editing('First Post', old_content="Hello World", new_content="Hi World")