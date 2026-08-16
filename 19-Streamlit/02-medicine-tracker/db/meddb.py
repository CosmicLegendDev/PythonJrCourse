class MedDb:

    def __init__(self):
        print("DB Initiated.")
        self.medicines = {
            "Product": [],
            "Quantity": [],
            "ExpiredIn": []
        }

    def fetch(self):
        print("Returning list of medicines.")
        return self.medicines

    def add(self, med_name, med_quantity, med_expire):
        print(f"Adding medicine {med_name} to inventory.")
        self.medicines.get("Product").append(med_name)
        self.medicines.get("Quantity").append(med_quantity)
        self.medicines.get("ExpiredIn").append(med_expire)

    def update(self, med_name, med_quantity, med_expire):
        print(f"Updating medicine {med_name} in inventory.")
        med_list = self.medicines.get("Product")
    
        try:
            med_index = med_list.index(med_name)
            self.medicines.get("Quantity")[med_index] = med_quantity
            self.medicines.get("ExpiredIn")[med_index] = med_expire
        except ValueError:
            print(f"Medicine '{med_name}' not found, hence adding to inventory.")

    def delete(self, med_name):
        print(f"Deleting medicne {med_name} from inventory.")
        med_list = self.medicines.get("Product")
        try:
            med_index = med_list.index(med_name)
            self.medicines.get("Product").remove(med_name)
            qty_list = self.medicines.get("Quantity")
            self.medicines.get("Quantity").clear()
            for i in range(0, len(qty_list)):
                if i != med_index:
                    self.medicines.get("Quantiy").append(qty_list[i])
            
            exp_list = self.medicines.get("ExpiredIn")
            self.medicines.get("ExpiredIn").clear()
            for i in range(0, len(exp_list)):
                if i != med_index:
                    self.medicines.get("ExpiredIn").append(exp_list[i])

        except ValueError:
            print(f"Error while deleting medicine {med_name}")



med_db = MedDb()

