import requests

# Outfit Suggestions
class TreeNode:
    def __init__(self, value=None, outfits=None):
        self.value = value
        self.children = {}
        self.outfits = outfits

# Dictionary for outfits
outfits = {
    'spring': {
        'sunny': {
            'casual': ['Oversized Denim Jacket and High-Waisted Jeans', 'Linen Shirt and Bermuda Shorts'],
            'formal': ['Pastel Blazer and Tailored Pants', 'Midi Wrap Dress with Heeled Sandals'],
            'sporty': ['Breathable Tracksuit with Sneakers', 'Bike Shorts and an Oversized Graphic Tee'],
            'chic': ['Floral Maxi Skirt with a Knitted Top', 'Fitted Cardigan and Pleated Culottes'],
        },
        'rainy': {
            'casual': ['Cropped Raincoat and Cargo Pants', 'Ankle Rain Boots with a Chunky Knit Sweater'],
            'formal': ['Belted Trench Coat over a Pencil Skirt', 'Leather Chelsea Boots and Slim-Fit Slacks'],
            'sporty': ['Waterproof Pullover and Performance Leggings'],
            'chic': ['Patterned Umbrella with a Waterproof Trench and Heeled Boots'],
        },
        'cloudy': {
            'casual': ['Lightweight Bomber Jacket and Mom Jeans', 'Striped Breton Top and Chinos'],
            'formal': ['Structured Blazer and Tapered Trousers'],
            'sporty': ['Half-Zip Sweatshirt and Joggers'],
            'chic': ['Knit Midi Dress with a Belt and Ankle Boots'],
        },
        'windy': {
            'casual': ['Windproof Utility Jacket and Relaxed Fit Jeans'],
            'formal': ['Tailored Windbreaker and Wool Slacks'],
            'sporty': ['Technical Hoodie and Running Tights'],
            'chic': ['Draped Scarf and Double-Breasted Coat with Loafers'],
        }
    },
    'summer': {
        'sunny': {
            'casual': ['White Linen Shirt and Cropped Wide-Leg Pants', 'Sleeveless Tank and Distressed Denim Shorts'],
            'formal': ['Seersucker Suit and Loafers', 'Off-Shoulder Midi Dress with Strappy Heels'],
            'sporty': ['Quick-Dry Tank Top and Athletic Shorts', 'Performance Sneakers and Mesh Panel Leggings'],
            'chic': ['Wide-Brim Hat with a Tiered Maxi Dress', 'Breezy Co-ord Set with Statement Earrings'],
        },
        'rainy': {
            'casual': ['Packable Rain Jacket and Capri Pants', 'Slip-On Rain Shoes and Lightweight Hoodie'],
            'formal': ['Waterproof Trench Coat over a Summer Dress', 'Tailored Cropped Pants with Leather Loafers'],
            'sporty': ['Rainproof Anorak with Biker Shorts'],
            'chic': ['Clear Vinyl Raincoat with a Stylish Umbrella and Ankle Boots'],
        },
        'cloudy': {
            'casual': ['Boxy T-Shirt and Relaxed Fit Cargo Pants'],
            'formal': ['Linen Blazer with Cropped Cigarette Trousers'],
            'sporty': ['Performance Polo and Drawstring Shorts'],
            'chic': ['Chiffon Blouse and Palazzo Pants'],
        },
        'windy': {
            'casual': ['Hooded Windbreaker and Denim Skirt'],
            'formal': ['Unstructured Blazer with Breezy Trousers'],
            'sporty': ['Windproof Pullover and Training Shorts'],
            'chic': ['Lightweight Trench with a Flowy Midi Dress'],
        }
    },
    'fall': {
        'sunny': {
            'casual': ['Cable-Knit Sweater and Corduroy Pants', 'Layered Flannel and Denim'],
            'formal': ['Textured Wool Coat and Slim Trousers', 'Shirt Dress with a Wide Belt'],
            'sporty': ['Zipped Fleece and Track Pants'],
            'chic': ['Tweed Jacket and A-Line Skirt with Knee-High Boots'],
        },
        'rainy': {
            'casual': ['Waxed Cotton Jacket and Tapered Pants', 'Chunky Knit Sweater with Rainproof Sneakers'],
            'formal': ['Plaid Trench Coat and Heeled Boots'],
            'sporty': ['Waterproof Hoodie and Thermal Leggings'],
            'chic': ['Fitted Rain Jacket with Suede Ankle Boots'],
        },
        'cloudy': {
            'casual': ['Shacket (Shirt-Jacket) and Black Jeans'],
            'formal': ['Cropped Wool Jacket and Wool Pants'],
            'sporty': ['Mock-Neck Sweatshirt and Joggers'],
            'chic': ['Soft Turtleneck Sweater and Paperbag Pants'],
        },
        'windy': {
            'casual': ['Puffer Vest over a Long-Sleeve Tee'],
            'formal': ['Wind-Resistant Coat with Slim Trousers'],
            'sporty': ['Performance Jacket with Tapered Joggers'],
            'chic': ['Cocoon Coat with a Cashmere Scarf and Ankle Boots'],
        }
    },
    'winter': {
        'sunny': {
            'casual': ['Fleece-Lined Parka and Skinny Jeans', 'Chunky Sweater and Ankle Boots'],
            'formal': ['Tailored Overcoat and Wool Suit', 'Turtleneck Sweater with Plaid Trousers'],
            'sporty': ['Puffer Jacket and Thermal Leggings', 'Pom-Pom Beanie and Fleece Gloves'],
            'chic': ['Long Wool Coat with Fur-Lined Boots and a Statement Belt'],
        },
        'rainy': {
            'casual': ['Waterproof Parka and Fleece-Lined Jeans', 'Hunter Boots with a Flannel Shirt'],
            'formal': ['Double-Breasted Raincoat and Dress Boots'],
            'sporty': ['Rain-Resistant Pullover with Sweatpants'],
            'chic': ['Oversized Waterproof Coat with Patterned Rain Boots'],
        },
        'cloudy': {
            'casual': ['Sherpa-Lined Jacket with Relaxed Fit Jeans'],
            'formal': ['Cashmere Coat with a Wool Scarf'],
            'sporty': ['Thermal Hoodie and Insulated Joggers'],
            'chic': ['Oversized Knit Sweater with a Maxi Skirt and Combat Boots'],
        },
        'windy': {
            'casual': ['Down Vest and Layered Knitwear'],
            'formal': ['Structured Wool Coat and Tailored Slacks'],
            'sporty': ['Windproof Parka and Tech-Fleece Pants'],
            'chic': ['Cape Coat with Gloves and Knee-High Boots'],
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
        userinput = input(prompt).lower()
        if userinput in valid_options:
            return userinput
        print(f"Invalid input. Choose from {', '.join(valid_options)}.")

def GetWeather(city):
    api_key = "baa1446feb29da6679ffe024cc14c1f0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:  # Check for successful API response
        data = response.json()
        temperature = data['main']['temp']
        weather_condition = data['weather'][0]['main']
        return temperature, weather_condition
    else:
        print(f"Error: Unable to retrieve weather data for {city}")
        return None, None

def TempToSeasonWeather(temperature, weather_condition):
    season = None
    weather = None

    if 20 <= temperature <= 30:
        season = "spring"
    elif temperature > 30:
        season = "summer"
    elif 10 <= temperature <= 20:
        season = "fall"
    else:
        season = "winter"

    if weather_condition.lower() in ["rain", "drizzle", "shower"]:
        weather = "rainy"
    elif weather_condition.lower() in ["clear", "sunny"]:
        weather = "sunny"
    elif weather_condition.lower() in ["clouds", "cloudy"]:
        weather = "cloudy"
    elif weather_condition.lower() in ["wind", "breeze"]:
        weather = "windy"
    else:
        weather = "other"

    return season, weather

def ShowOutfits(outfits):
    if outfits:
        print("\nOutfit Suggestions:")
        for i, outfit in enumerate(outfits, 1):
            print(f"{i}. {outfit}")
    else:
        print("No outfits available.")

def SuggestOutfit():
    outfit_tree = BuildTree(outfits)

    while True:
        user_choice = input("Choose input method:\n1. Manual input\n2. Location-based\n1 or 2: ")

        if user_choice == "1":
            season = ValidateInput("Enter season (spring, summer, fall, winter): ",
                                   ["spring", "summer", "fall", "winter"])
            weather = ValidateInput("Enter weather (sunny, rainy, cloudy, windy): ",
                                    ["sunny", "rainy", "cloudy", "windy"])
            style = ValidateInput("Enter style (casual, formal, sporty, chic): ",
                                  ["casual", "formal", "sporty", "chic"])
        elif user_choice == "2":
            city = input("Enter city: ").lower()
            style = ValidateInput("Enter style (casual, formal, sporty, chic): ",
                                  ["casual", "formal", "sporty", "chic"])
            temperature, weather_condition = GetWeather(city)
            if temperature and weather_condition:
                season, weather = TempToSeasonWeather(temperature, weather_condition)
                print(f"\nDetected: Season = {season}, Weather = {weather}")
            else:
                print("Error retrieving weather data. Please try again.")
                continue

        else:
            print("Invalid input. Please choose 1 or 2.")
            continue

        path = [season, weather, style]
        outfit_node = TraverseTree(outfit_tree, path)

        if outfit_node and outfit_node.outfits:
            ShowOutfits(outfit_node.outfits)
        else:
            print("No outfit suggestions available for this combination.")

        again = input("\nWould you like to receive another suggestion? (yes/no): ").lower()
        if again != "yes":
            break



# Wardrobe Management
class ClothingItem:
    def __init__(self, name, type, color=None, season=None):
        self.name = name
        self.type = type
        self.color = color
        self.season = season

# make an empty dictionary for wardrobe
wardrobe = {
    "tops": [],
    "bottoms": [],
    "shoes": [],
    "accessories": [],
    "outerwear": [],
    "dresses": [],
    "underwear": [],
    "sleepwear": []
}

def ViewWardrobe(wardrobe):
    empty_wardrobe = True
    for clothing_type, items in wardrobe.items():
        if items:
            empty_wardrobe = False
            break

    if empty_wardrobe:
        print("Your wardrobe is currently empty.")
    else:
        print("\nWardrobe:")
        for clothing_type, items in wardrobe.items():
            print(f" - {clothing_type}:")
            for item in items:
                print(f"   - {item}")

def EditWardrobe(wardrobe):
    while True:
        item_type = ValidateInput("Enter the clothing type to edit (tops, bottoms, shoes, accessories, "
                                  "outerwear, dresses, underwear, sleepwear): ",
                                  ["tops", "bottoms", "shoes", "accessories", "outerwear", "dresses", "underwear",
                                   "sleepwear"])
        item_name = input("Enter the item name to edit: ")

        if item_type in wardrobe and item_name in wardrobe[item_type]:
            item_index = wardrobe[item_type].index(item_name)
            item_to_edit = wardrobe[item_type][item_index]

            new_name = input("Enter the new name (or press Enter to keep the same): ")
            new_color = input("Enter the new color (or press Enter to keep the same): ")
            new_material = input("Enter the new material (or press Enter to keep the same): ")
            new_occasion = input("Enter the new occasion (or press Enter to keep the same): ")
            new_season = input("Enter the new season (or press Enter to keep the same): ")

            if new_name:
                item_to_edit["name"] = new_name
            if new_color:
                item_to_edit["color"] = new_color
            if new_material:
                item_to_edit["material"] = new_material
            if new_occasion:
                item_to_edit["occasion"] = new_occasion
            if new_season:
                item_to_edit["season"] = new_season

            print(f"Item '{item_name}' updated.")

        else:
            print("Item not found in your wardrobe.")

        continue_editing = input("Do you want to edit another item? (yes/no): ").lower()
        if continue_editing != "yes":
            break

def AddClothingItem(wardrobe):
    while True:
        item_name = input("Enter the name of the item: ")
        item_type = ValidateInput("Enter the clothing type to edit (tops, bottoms, shoes, accessories, "
                                  "outerwear, dresses, underwear, sleepwear): ",
                                  ["tops", "bottoms", "shoes", "accessories", "outerwear", "dresses", "underwear",
                                   "sleepwear"])

        # Optional fields:
        color = input("Enter the color of the item (optional): ")
        material = input("Enter the material of the item (optional): ")
        occasion = input("Enter the occasion for the item (e.g., casual, formal, workout): ")
        season = input("Enter the season for the item (optional): ")

        wardrobe[item_type].append({
            "name": item_name,
            "color": color,
            "material": material,
            "occasion": occasion,
            "season": season
        })

        continue_adding = input("Do you want to add another item? (yes/no): ").lower()
        if continue_adding != "yes":
            break

def ManageWardrobe():
    while True:
        action = ValidateInput("What would you like to do? (view/edit/add/back): ",
                               ["view", "edit", "add", "back"])

        if action == "view":
            ViewWardrobe(wardrobe)
        elif action == "edit":
            EditWardrobe(wardrobe)
        elif action == "add":
            AddClothingItem(wardrobe)
        elif action == "back":
            break

def main():
    while True:
        choice = ValidateInput("Welcome! Choose an option: (wardrobe/outfit): ", ["wardrobe", "outfit"])

        if choice == "wardrobe":
            ManageWardrobe()
        elif choice == "outfit":
            SuggestOutfit()

        again = input("\nWould you like to go back to the main page? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == '__main__':
    main()
