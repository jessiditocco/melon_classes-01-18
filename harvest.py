############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    # def __repr__(self):
    #     """Provide helpful output when printing"""

    #     repr_str = "<MelonType code={code} name={name}>"
    #     return repr_str.format(code=self.code, name=self.name)

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType("musk", 1998, "green", False, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    crenshaw = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")

    muskmelon.add_pairing(['mint'])
    casaba.add_pairing(['strawberry', 'mint'])
    crenshaw.add_pairing(['proscuitto'])
    yellow_watermelon.add_pairing(['icecream'])

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    # print all_melon_types
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print melon.name + " pairs with"

        for pairing in melon.pairings:
            print "- {}".format(pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon
        # melon_codes[melon.code] = melon.code

    return melon_codes

# print_pairing_info(make_melon_types())
# print make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from,
                 harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and
                self.harvested_from != 3)


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')

    harvested_melon_collection = [melon1, melon2, melon3, melon4, melon5,
                                  melon6, melon7, melon8, melon9]

    return harvested_melon_collection


# melon_types_dictionary = make_melon_type_lookup(make_melon_types()) # dictionary, keys are code and values are obj
# print make_melons(melon_types_dictionary)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for i, harvested_melon in enumerate(melons, 1):
        print "Melon ", i
        print " -Melon type: {}".format(harvested_melon.melon_type.name)
        print " -Shape rating: {}".format(harvested_melon.shape_rating)
        print " -Color rating: {}".format(harvested_melon.color_rating)
        print " -Harvested from Field: {}".format(harvested_melon.harvested_from)
        print " -Harvested by: {}".format(harvested_melon.harvested_by)
        print " -Sellable or Not: {}".format(harvested_melon.is_sellable())

melon_types_dictionary = make_melon_type_lookup(make_melon_types())
melon_collection = make_melons(melon_types_dictionary)

get_sellability_report(melon_collection)
