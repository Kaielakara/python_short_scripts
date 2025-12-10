# create a pyhton script which is sort of a django helper file which generate the html id or class
def element_generator(tag, content, **attribute):

    attr = []


    for key,value in attribute.items():
        attr.append(f'{key}: {value}')
        

    print(attr)
    a = " ".join(attr)

    return f"<{tag} {a} > {content} </{tag}>"


print(element_generator("h1", "Hello World", id='hello_header', style='red'))