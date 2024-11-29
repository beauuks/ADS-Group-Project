class TreeNode:
    def __init__(self, value=None, outfits=None):
        self.value = value
        self.children = {}
        self.outfits = outfits

# Dictionary for outfits
outfits = {
    'spring': {
        'sunny': {
            'casual': ['Light Jacket and Jeans', 'T-shirt and Shorts'],
            'formal': ['Blazer and Chinos', 'Light Dress'],
            'sporty': ['Running Shoes and T-shirt', 'Track Pants and Hoodie'],
            'chic': ['Floral Dress', 'Cardigan'],
        },
        'rainy': {
            'casual': ['Raincoat and Jeans', 'Rain Boots and Hoodie'],
            'formal': ['Trench Coat and Dress Pants', 'Leather Boots'],
            'sporty': ['Waterproof Jacket and Joggers'],
            'chic': ['Stylish Waterproof Coat', 'Chelsea Boots'],
        }
    },
    'summer': {
        'sunny': {
            'casual': ['T-shirt and Shorts', 'Sundress', 'Tank top and Skirt'],
            'formal': ['Summer Blazer and Pants', 'Light Button-up Shirt'],
            'sporty': ['Sports Top and Shorts', 'Running Shoes and Tank Top'],
            'chic': ['Chic Summer Dress', 'Sunglasses and Hat'],
        },
        'rainy': {
            'casual': ['Raincoat and Jeans', 'Rain Boots and Hoodie'],
            'formal': ['Waterproof Blazer', 'Dress Pants and Boots'],
            'sporty': ['Waterproof Jacket and Sweatpants'],
            'chic': ['Stylish Raincoat', 'Ankle Boots'],
        }
    },
    'fall': {
        'sunny': {
            'casual': ['Sweater and Jeans', 'Cardigan and Leggings'],
            'formal': ['Wool Coat and Trousers', 'Dress Shirt and Chinos'],
            'sporty': ['Jacket and Joggers'],
            'chic': ['Leather Jacket and Skirt', 'Scarf and Boots'],
        },
        'rainy': {
            'casual': ['Rain Jacket and Jeans', 'Waterproof Boots and Sweater'],
            'formal': ['Trench Coat and Dress Pants'],
            'sporty': ['Raincoat and Jogging Pants'],
            'chic': ['Chic Raincoat and Ankle Boots'],
        }
    },
    'winter': {
        'sunny': {
            'casual': ['Sweater and Jeans', 'Scarf and Boots'],
            'formal': ['Wool Coat and Trousers'],
            'sporty': ['Thermal Jacket and Joggers'],
            'chic': ['Winter Coat and Leather Gloves'],
        },
        'rainy': {
            'casual': ['Waterproof Coat and Jeans'],
            'formal': ['Trench Coat and Boots'],
            'sporty': ['Rain Jacket and Jogging Pants'],
            'chic': ['Stylish Waterproof Coat'],
        }
    }
}

def BuildTree(data):
    if isinstance(data, dict):
        node = TreeNode()
        for key, value in data.items():
            node.children[key] = BuildTree(value)
        return node
    else:  # Leaf node
        return TreeNode(outfits=data)


def TraverseTree(root, keys):
    current_node = root
    for key in keys:
        if key in current_node.children:
            current_node = current_node.children[key]
        else:
            print("Invalid input.")
            return None
    return current_node

def ValidateInput(prompt, valid_options): # to make sure that the input is in the valid options
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Choose from {', '.join(valid_options)}.")


def ShowOutfits(outfits):
    if outfits:
        print("\nOutfit Suggestions:")
        for i, outfit in enumerate(outfits, 1):
            print(f"{i}. {outfit}")
    else:
        print("No outfits available.")


def AddOutfit(outfit_tree):
    season = ValidateInput("Enter season (spring, summer, fall, winter): ", ["spring", "summer", "fall", "winter"])
    weather = ValidateInput("Enter weather (sunny, rainy): ", ["sunny", "rainy"])
    style = ValidateInput("Enter style (casual, formal, sporty, chic): ", ["casual", "formal", "sporty", "chic"])

    path = [season, weather, style]
    outfit_node = TraverseTree(outfit_tree, path)

    if outfit_node:
        new_outfit = input("Enter a new outfit to add: ")
        outfit_node.outfits.append(new_outfit)
        print(f"Outfit '{new_outfit}' added successfully.")
    else:
        print("Could not add outfit. Something went wrong.")


def SuggestOutfit(outfit_tree):
    while True:
        season = ValidateInput("Enter season (spring, summer, fall, winter): ", ["spring", "summer", "fall", "winter"])
        weather = ValidateInput("Enter weather (sunny, rainy): ", ["sunny", "rainy"])
        style = ValidateInput("Enter style (casual, formal, sporty, chic): ", ["casual", "formal", "sporty", "chic"])

        path = [season, weather, style]
        outfit_node = TraverseTree(outfit_tree, path)

        if outfit_node and outfit_node.outfits:
            ShowOutfits(outfit_node.outfits)

        add_new = input("\nWould you like to add a new outfit? (yes/no): ").lower()
        if add_new == "yes":
            AddOutfit(outfit_tree)

        again = input("\nWould you like to try another combination? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == '__main__':
    outfit_tree = BuildTree(outfits)
    SuggestOutfit(outfit_tree)
