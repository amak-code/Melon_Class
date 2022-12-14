############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code

        self.first_harvest = first_harvest

        self.color = color

        self.is_seedles = is_seedless

        self.is_bestseller = is_bestseller

        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)
        #mint
        #strawberries
        #prosciutto
        #ice_cream

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon= MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "muskmelon"
    )
    muskmelon.add_pairing("mint")

    all_melon_types.append(muskmelon)

    crenshaw=MelonType(
        "cren",
        1996,
        "green",
        False,
        False,
        "crenshaw"
    )
    crenshaw.add_pairing("prosciutto")

    all_melon_types.append(crenshaw)

    yellow_watermelon=MelonType(
        "yw",
        2013,
        "yellow",
        False,
        True,
        "yellow watermelon"
    )
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(yellow_watermelon)

    casaba = MelonType(
        "cas",
        2003,
        "orange",
        False,
        False,
        "casaba"

    )
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    all_melon_types.append(casaba)
    
    

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

    #print out each melon types pairings
    for melon in melon_types:

        print(f"{melon.name}  pairs with \n" )
        print(f"-{melon.pairings[0]}")
        if len(melon.pairings)>1:
            # print(f"-{melon.pairings[0]}")
            print(f"-{melon.pairings[1]}")
        print("\n")
            



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon

    return melons_by_id

casaba = MelonType(
        "cas",
        2003,
        "orange",
        False,
        False,
        "casaba"

    )




############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon instance."""
        self.melon_type = melon_type

        self.shape_rating = shape_rating

        self.color_rating = color_rating

        self.field = field

        self.harvester = harvester



    def is_sellable(self):
        """Determine whether this melon can be sold."""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True

        return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD )")
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE )")


list_melons = make_melon_types()
#print(print_pairing_info(list_melons))
#melons_by_id = make_melon_type_lookup(list_melons)
#print(melons_by_id)
melons = make_melons(list_melons)
get_sellability_report(melons)
