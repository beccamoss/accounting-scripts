"""Print out all the melons in our inventory."""


#from melons import melon_names, melon_seedlessness, melon_prices
from melons import melon_names

def print_melon(melon):
    """Print each melon."""

    print melon
    print "   seedless: " + str(melon_names[melon]["seedless"])
    print "   price: " + str(melon_names[melon]["price"])
    print "   flesh_color: " + melon_names[melon]["flesh"]
    print "   weight: " + str(melon_names[melon]["weight"])
    print "   rind_color: " + melon_names[melon]["rind"]

for melon in melon_names:
    print_melon(melon)
