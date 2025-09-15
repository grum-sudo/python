# def display_names(*args):
#   for arg in args:
#       print(arg, end=" ")
#
#
# display_names("dr.", "totaly", "real", "person", "for", "sure")

# def print_address(**kwargs):
#   for key, value in kwargs.items():
#       print(f"{key}: {value}")

#print_address(street="123 real place", city="nowhere", state="hi", zip="12345")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("dr.", "totaly", "real", "person", 
               street="123 real place", city="nowhere", zip="12345")