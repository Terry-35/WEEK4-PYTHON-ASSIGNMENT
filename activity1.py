# Base Class: DesignPackage
class DesignPackage:
    def __init__(self, name, price, description):
       
        # Constructor to initialize the DesignPackage object, Name of the package (e.g., Logo, Branding)Price of the package, and a Short description of the package
      
        self.name = name
        self.price = price
        self.description = description

    def display_info(self):
        # Display package details.
        print(f"Package: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price}")

# Subclass 1: LogoDesign
class LogoDesign(DesignPackage):
    def __init__(self, name, price, includes_revision):
        super().__init__(name, price, "Logo Design with custom graphics and concepts.")
        self.includes_revision = includes_revision

    def display_info(self):
        """Override the display_info to include revision info."""
        super().display_info()
        print(f"Includes Revision: {'Yes' if self.includes_revision else 'No'}")

# Subclass 2: Branding
class Branding(DesignPackage):
    def __init__(self, name, price, includes_social_media_kit):
        super().__init__(name, price, "Complete Branding Package including logos, business cards, and social media kit.")
        self.includes_social_media_kit = includes_social_media_kit

    def display_info(self):
        """Override the display_info to include social media kit info."""
        super().display_info()
        print(f"Includes Social Media Kit: {'Yes' if self.includes_social_media_kit else 'No'}")

# Subclass 3: BusinessCardDesign
class BusinessCardDesign(DesignPackage):
    def __init__(self, name, price, double_sided):
        super().__init__(name, price, "Business card design with a minimalist approach.")
        self.double_sided = double_sided

    def display_info(self):
        """Override the display_info to include double-sided info."""
        super().display_info()
        print(f"Double-Sided: {'Yes' if self.double_sided else 'No'}")

# Class to represent an Order
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.packages = []
        self.status = "Pending"

    def add_package(self, package):
        """Add a design package to the order."""
        self.packages.append(package)

    def calculate_total(self):
        """Calculate the total price of the order."""
        total = sum(package.price for package in self.packages)
        return total

    def display_order(self):
        """Display order details."""
        print(f"Order for: {self.customer_name}")
        for package in self.packages:
            package.display_info()
            print("-" * 30)
        print(f"Total Price: ${self.calculate_total()}")
        print(f"Status: {self.status}")

    def update_status(self, new_status):
        """Update the status of the order."""
        self.status = new_status
        print(f"Order status updated to: {self.status}")


# Example Usage
if __name__ == "__main__":
    # Creating design packages
    logo_package = LogoDesign("Minimal Logo", 150, True)
    branding_package = Branding("Branding Kit", 350, True)
    business_card_package = BusinessCardDesign("Elegant Business Card", 50, True)

    # Creating an order
    order1 = Order("Tee Codes Client")
    order1.add_package(logo_package)
    order1.add_package(branding_package)
    order1.add_package(business_card_package)

    # Displaying the order
    order1.display_order()

    # Updating the order status
    order1.update_status("In Progress")
    order1.display_order()

    # Calculating the total price
    total_price = order1.calculate_total()
    print(f"Total Price for the order: ${total_price}")
