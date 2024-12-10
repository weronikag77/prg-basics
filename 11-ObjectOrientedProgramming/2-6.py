# Identify at least 3 states and 3 behaviors for your smartphone. 
# Then, for the listed states and behaviors, create a class with attributes and methods. 
# Try to use verbs in method names as they describe activities. 
# Finally, create a smartphone object, call its methods and display object’s properties.

class Phone():
    def __init__(self, brand, model, percentage):
        self.brand = brand
        self.model = model
        self.percentage = percentage

    def is_on(self):
        self.is_on = True
    
    def change_percentage(self,  percentage):
        self.percentage = percentage

    def display_info(self):
        print(f"Phone brand: {self.brand}")
        print(f"Phone model: {self.model}")
        print(f"Battery percentage: {self.percentage}")


def main():
    my_phone = Phone("Apple", "iPhone 15", "91")
    my_phone.change_percentage("85")
    my_phone.display_info()

if __name__ =="__main__":
    main()

    

