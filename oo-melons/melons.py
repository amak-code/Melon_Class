"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

  

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    shipped = False
    order_type = "domestic"
    tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == 'Christmas':
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    shipped = False
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas':
            base_price = base_price * 1.5
        if self.qty < 10:
             total = (1 + self.tax) * self.qty * base_price + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
