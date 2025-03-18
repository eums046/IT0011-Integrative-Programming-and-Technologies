class Item:
    """
    Class representing an item with id, name, description, and price.
    """
    def __init__(self, item_id, name, description, price):
        self.set_id(item_id)
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
    
    def set_id(self, item_id):
        """Set the item ID with validation."""
        try:
            item_id = int(item_id)
            if item_id <= 0:
                raise ValueError("ID must be a positive integer.")
            self._id = item_id
        except ValueError as e:
            if "ID must be" in str(e):
                raise
            raise ValueError("ID must be a valid integer.")
    
    def set_name(self, name):
        """Set the item name with validation."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if len(name) > 100:
            raise ValueError("Name must be 100 characters or less.")
        self._name = name.strip()
    
    def set_description(self, description):
        """Set the item description with validation."""
        if not isinstance(description, str):
            raise TypeError("Description must be a string.")
        self._description = description.strip()
    
    def set_price(self, price):
        """Set the item price with validation."""
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price cannot be negative.")
            self._price = price
        except ValueError as e:
            if "Price cannot be" in str(e):
                raise
            raise ValueError("Price must be a valid number.")
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @property
    def price(self):
        return self._price
    
    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Price: ${self._price:.2f}"
    
    def details(self):
        return f"ID: {self._id}\nName: {self._name}\nDescription: {self._description}\nPrice: ${self._price:.2f}"


class ItemManager:
    """
    Class to manage items with CRUD operations.
    """
    def __init__(self):
        self.items = {}
    
    def create_item(self, item_id, name, description, price):
        """Create a new item and add it to the inventory."""
        try:
            # Convert item_id to integer first
            item_id = int(item_id)
            
            # Check if item ID already exists
            if item_id in self.items:
                raise ValueError(f"Item with ID {item_id} already exists.")
            
            # Create new item
            new_item = Item(item_id, name, description, price)
            self.items[item_id] = new_item
            return new_item
        except (ValueError, TypeError) as e:
            raise e
    
    def read_item(self, item_id):
        """Retrieve an item by its ID."""
        try:
            item_id = int(item_id)
            if item_id not in self.items:
                raise ValueError(f"Item with ID {item_id} not found.")
            return self.items[item_id]
        except ValueError as e:
            if "not found" in str(e):
                raise
            raise ValueError("ID must be a valid integer.")
    
    def update_item(self, item_id, name=None, description=None, price=None):
        """Update an existing item's properties."""
        item = self.read_item(item_id)
        
        try:
            if name is not None:
                item.set_name(name)
            if description is not None:
                item.set_description(description)
            if price is not None:
                item.set_price(price)
            return item
        except (ValueError, TypeError) as e:
            raise e
    
    def delete_item(self, item_id):
        """Delete an item from the inventory."""
        item_id = int(item_id)
        item = self.read_item(item_id)
        del self.items[item_id]
        return True
    
    def list_all_items(self):
        """Return a list of all items."""
        return list(self.items.values())


def main():
    # Create ItemManager outside the loop to maintain state
    item_manager = ItemManager()
    
    while True:
        print("\n===== Item Management System =====")
        print("1. Add New Item")
        print("2. View Item Details")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        try:
            if choice == '1':
                print("\n--- Add New Item ---")
                item_id = input("Enter Item ID: ")
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = input("Enter Item Price: ")
                
                item = item_manager.create_item(item_id, name, description, price)
                print(f"\nItem created successfully!\n{item.details()}")
                
                # Debug info to verify storage
                print(f"\nDebug: Item stored with key {item.id} of type {type(item.id)}")
                print(f"Debug: Current keys in items dict: {list(item_manager.items.keys())}")
                
            elif choice == '2':
                print("\n--- View Item Details ---")
                item_id = input("Enter Item ID: ")
                
                # Debug info before lookup
                print(f"Debug: Looking up ID {item_id}, will convert to {int(item_id)}")
                print(f"Debug: Available keys: {list(item_manager.items.keys())}")
                
                item = item_manager.read_item(item_id)
                print(f"\n{item.details()}")
                
            elif choice == '3':
                print("\n--- Update Item ---")
                item_id = input("Enter Item ID: ")
                
                # First check if the item exists
                item = item_manager.read_item(item_id)
                
                print("\nLeave blank if you don't want to update that field.")
                name = input(f"Enter New Name (current: {item.name}): ")
                description = input(f"Enter New Description (current: {item.description}): ")
                price = input(f"Enter New Price (current: ${item.price:.2f}): ")
                
                # Only update fields that were provided
                name = name if name.strip() else None
                description = description if description.strip() else None
                price = price if price.strip() else None
                
                item = item_manager.update_item(item_id, name, description, price)
                print(f"\nItem updated successfully!\n{item.details()}")
                
            elif choice == '4':
                print("\n--- Delete Item ---")
                item_id = input("Enter Item ID: ")
                item_manager.delete_item(item_id)
                print(f"\nItem {item_id} deleted successfully!")
                
            elif choice == '5':
                print("\n--- All Items ---")
                items = item_manager.list_all_items()
                if not items:
                    print("No items found.")
                else:
                    print(f"Debug: Found {len(items)} items")
                    for item in items:
                        print(f"{item}")
                
            elif choice == '6':
                print("\nExiting program. Goodbye!")
                break
                
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")
                
        except (ValueError, TypeError) as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()