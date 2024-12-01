import requests
import os
from dotenv import load_dotenv
load_dotenv()

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
            'casual': [
                'Oversized Denim Jacket and High-Waisted Jeans',
                'Linen Shirt and Bermuda Shorts',
                'Ribbed Tank Top with Wide-Legged Trousers',
                'Button-Up Shirt Dress with White Sneakers',
                'Crop Top with Flowy Midi Skirt'],
            'formal': [
                'Pastel Blazer and Tailored Pants',
                'Midi Wrap Dress with Heeled Sandals',
                'Sheath Dress with a Short Cardigan',
                'Pinstriped Suit and Neutral Pumps',
                'Silk Blouse with Pleated Trousers'],
            'sporty': [
                'Breathable Tracksuit with Sneakers',
                'Bike Shorts and an Oversized Graphic Tee',
                'Tank Top with Mesh Leggings',
                'Athletic Hoodie with Running Shorts',
                'Cropped Windbreaker with Jogger Pants'],
            'chic': [
                'Floral Maxi Skirt with a Knitted Top',
                'Fitted Cardigan and Pleated Culottes',
                'Ballet Wrap Top with High-Waisted Jeans',
                'Puff-Sleeve Blouse with a Paperbag Skirt',
                'Chiffon Wrap Blouse with Slim Fit Trousers']
        },
        'rainy': {
            'casual': [
                'Cropped Raincoat and Cargo Pants',
                'Ankle Rain Boots with a Chunky Knit Sweater',
                'Rainproof Hoodie with Straight-Leg Jeans',
                'Fleece-Lined Anorak with Joggers',
                'Water-Resistant Shirt Jacket with Leggings'],
            'formal': [
                'Belted Trench Coat over a Pencil Skirt',
                'Leather Chelsea Boots and Slim-Fit Slacks',
                'Blouse with a Knee-Length Rain Skirt',
                'Tailored Dress with Waterproof Pumps',
                'Faux Leather Jacket with Midi Pencil Skirt'],
            'sporty': [
                'Waterproof Pullover and Performance Leggings',
                'Quick-Dry Hoodie and Cargo Shorts',
                'Seamless Rain Jacket with Biker Shorts',
                'Lightweight Rain Shell with Jogging Pants',
                'Insulated Running Jacket with Capris'],
            'chic': [
                'Patterned Umbrella with a Waterproof Trench and Heeled Boots',
                'Transparent Rain Poncho with Bold Jewelry',
                'Vinyl Trench with High-Heeled Rain Boots',
                'Wrap Dress with a Designer Umbrella',
                'Layered Knit Vest with Waterproof Ankle Boots']
        },
        'cloudy': {
            'casual': [
                'Lightweight Bomber Jacket and Mom Jeans',
                'Striped Breton Top and Chinos',
                'Cotton Hoodie with Slim Fit Sweatpants',
                'Knitted Sweater with Wide-Leg Pants',
                'Casual Blazer with Rolled-Up Jeans'],
            'formal': [
                'Structured Blazer and Tapered Trousers',
                'Pencil Dress with a Button-Up Cardigan',
                'Plaid Suit with Polished Loafers',
                'Silk Midi Skirt with a Tailored Coat',
                'Lace Blouse with High-Waisted Trousers'],
            'sporty': [
                'Half-Zip Sweatshirt and Joggers',
                'Performance Tank Top with Stretch Leggings',
                'Hooded Windbreaker with Jogging Shorts',
                'Breathable Track Pants with a Zip-Up Jacket',
                'Moisture-Wicking Hoodie with Capri Joggers'],
            'chic': [
                'Knit Midi Dress with a Belt and Ankle Boots',
                'Puffed Sleeves with a Pleated Midi Skirt',
                'Flared Pants with a Ribbed Sweater',
                'Silk Wrap Blouse with Straight-Leg Trousers',
                'Patterned Maxi Dress with a Statement Necklace']
        },
        'windy': {
            'casual': [
                'Windproof Utility Jacket and Relaxed Fit Jeans',
                'Oversized Sweater with Jogger Pants',
                'Hooded Pullover with Tapered Leggings',
                'Layered Flannel Shirt with Stretch Chinos',
                'Windbreaker Coat with Skinny Jeans'],
            'formal': [
                'Tailored Windbreaker and Wool Slacks',
                'Cropped Blazer with Tapered Dress Pants',
                'Fitted Long Coat with Polished Loafers',
                'High-Neck Sweater with Wide-Leg Trousers',
                'Layered Turtleneck with a Tailored Skirt'],
            'sporty': [
                'Technical Hoodie and Running Tights',
                'Windproof Jogging Suit with Sneakers',
                'Water-Resistant Sweatshirt and Track Pants',
                'Breathable Pullover and High-Performance Shorts',
                'Layered Hoodie with Compression Leggings'],
            'chic': [
                'Draped Scarf and Double-Breasted Coat with Loafers',
                'Wool Maxi Coat with High-Heeled Boots',
                'Leather Gloves with a Cashmere Sweater and Slim Jeans',
                'Fringed Poncho with Ankle Boots',
                'Trench Coat with Wide-Leg Culottes and Ballet Flats']
        }
    },
    'summer': {
        'sunny': {
            'casual': [
                'White Linen Shirt and Cropped Wide-Leg Pants',
                'Sleeveless Tank and Distressed Denim Shorts',
                'Lightweight Chambray Shirt and Cargo Shorts',
                'Striped Cotton Dress with Slip-On Sandals',
                'Tie-Front Top with High-Waisted Shorts'],
            'formal': [
                'Seersucker Suit and Loafers',
                'Off-Shoulder Midi Dress with Strappy Heels',
                'Linen Shirt Dress with Espadrilles',
                'Floral Blouse and Pleated Palazzo Pants',
                'Tailored Jumpsuit with Metallic Sandals'],
            'sporty': [
                'Quick-Dry Tank Top and Athletic Shorts',
                'Performance Sneakers and Mesh Panel Leggings',
                'Moisture-Wicking Sports Bra and Running Shorts',
                'Zip-Up Vest with Stretch Joggers',
                'Athletic Crop Top and Capri Leggings'],
            'chic': [
                'Wide-Brim Hat with a Tiered Maxi Dress',
                'Breezy Co-ord Set with Statement Earrings',
                'Silky Slip Dress with Strappy Sandals',
                'One-Shoulder Top with Wrap Skirt',
                'Lace-Trimmed Romper with Chunky Jewelry']
        },
        'rainy': {
            'casual': [
                'Packable Rain Jacket and Capri Pants',
                'Slip-On Rain Shoes and Lightweight Hoodie',
                'Waterproof Bucket Hat with Cropped Pants',
                'Fleece-Lined Raincoat with Cotton Shorts',
                'Polyester Tunic and Rain Sneakers'],
            'formal': [
                'Waterproof Trench Coat over a Summer Dress',
                'Tailored Cropped Pants with Leather Loafers',
                'A-Line Dress with Waterproof Wedges',
                'Silk Shirt with Pleated Skirt and Rain Flats',
                'Embellished Midi Dress with Rainproof Pumps'],
            'sporty': [
                'Rainproof Anorak with Biker Shorts',
                'Hooded Pullover with Compression Leggings',
                'Seam-Sealed Windbreaker and Training Pants',
                'Quick-Dry Long-Sleeve Tee with Joggers',
                'Insulated Vest with Mesh Shorts'],
            'chic': [
                'Clear Vinyl Raincoat with a Stylish Umbrella and Ankle Boots',
                'Water-Resistant Poncho over a Maxi Dress',
                'Transparent Trench with Metallic Accessories',
                'Frill-Sleeve Rain Top with High-Waisted Trousers',
                'Chiffon Skirt with Waterproof Kitten Heels']
        },
        'cloudy': {
            'casual': [
                'Boxy T-Shirt and Relaxed Fit Cargo Pants',
                'Tie-Dye Top with Linen Joggers',
                'Knitted Tank and High-Waisted Shorts',
                'Sleeveless Hoodie and Cropped Jeans',
                'Relaxed Button-Up Shirt with Paperbag Waist Pants'],
            'formal': [
                'Linen Blazer with Cropped Cigarette Trousers',
                'Empire-Waist Dress with Heeled Sandals',
                'Structured Top with Tailored Culottes',
                'Cap Sleeve Jumpsuit with Pointed Flats',
                'Peplum Top with Silk Wide-Leg Pants'],
            'sporty': [
                'Performance Polo and Drawstring Shorts',
                'Mesh Racerback Tank with Compression Pants',
                'Sun-Blocking Jacket with Biker Leggings',
                'Longline Sports Tee with Workout Shorts',
                'Water-Resistant Hoodie with Training Capris'],
            'chic': [
                'Chiffon Blouse and Palazzo Pants',
                'Asymmetrical Wrap Dress with Heeled Sandals',
                'Fringe Hem Top with Embellished Skirt',
                'Wide-Leg Jumpsuit with Statement Jewelry',
                'Linen Wrap Top with Cropped Cigarette Pants']
        },
        'windy': {
            'casual': [
                'Hooded Windbreaker and Denim Skirt',
                'Off-Shoulder Top with Flared Capris',
                'Rolled-Up Cotton Shirt with Slim Jeans',
                'Layered Tank and Lightweight Cardigan with Shorts',
                'Utility Jacket with Distressed Denim'],
            'formal': [
                'Unstructured Blazer with Breezy Trousers',
                'Wrap Dress with a Lightweight Shawl',
                'Pleated Dress with a Thin Belt and Flats',
                'Silk Camisole with Tailored Pencil Pants',
                'Sheer Button-Up Blouse with Flowy Skirt'],
            'sporty': [
                'Windproof Pullover and Training Shorts',
                'Moisture-Wicking Hoodie with Capri Pants',
                'Breathable Tights with an Athletic Jacket',
                'Quick-Dry Windbreaker with Leggings',
                'Vented Running Jacket with Gym Shorts'],
            'chic': [
                'Lightweight Trench with a Flowy Midi Dress',
                'Statement Earrings with a High-Neck Jumpsuit',
                'Silky Wrap Top with Tailored Pants',
                'Belted Tunic Dress with Strappy Sandals',
                'Floral Kimono Jacket with Culottes']
        }
    },
    'fall': {
        'sunny': {
            'casual': [
                'Cable-Knit Sweater and Corduroy Pants',
                'Layered Flannel and Denim',
                'Plaid Shirt with Rolled-Up Jeans',
                'Hooded Cardigan with Fitted Trousers',
                'Cozy Knit Vest over a Turtleneck with Wide-Leg Jeans'],
            'formal': [
                'Textured Wool Coat and Slim Trousers',
                'Shirt Dress with a Wide Belt',
                'Velvet Blazer with Tailored Pants',
                'A-Line Skirt with Fitted Blouse and Ankle Boots',
                'Double-Breasted Jacket with Midi Pencil Skirt'],
            'sporty': [
                'Zipped Fleece and Track Pants',
                'Quilted Vest with Joggers',
                'Thermal Hoodie with Tapered Tights',
                'Half-Zip Pullover with Athletic Leggings',
                'Moisture-Wicking Long Sleeve with Gym Pants'],
            'chic': [
                'Tweed Jacket and A-Line Skirt with Knee-High Boots',
                'Leather Leggings with an Oversized Sweater',
                'Statement Scarf with a Long Wool Coat',
                'Ribbed Knit Dress with Heeled Booties',
                'Wide-Brim Hat with a Midi Trench Dress']
        },
        'rainy': {
            'casual': [
                'Waxed Cotton Jacket and Tapered Pants',
                'Chunky Knit Sweater with Rainproof Sneakers',
                'Fleece Hoodie with Waterproof Trousers',
                'Oversized Pullover with Rain Boots',
                'Light Quilted Coat with Cropped Jeans'],
            'formal': [
                'Plaid Trench Coat and Heeled Boots',
                'Silk Blouse with Wool Pants and Loafers',
                'Peplum Jacket with a Pencil Skirt',
                'Tailored Coat with a Velvet Dress',
                'A-Line Plaid Skirt with a Turtleneck and Ankle Boots'],
            'sporty': [
                'Waterproof Hoodie and Thermal Leggings',
                'Performance Rain Jacket with Joggers',
                'Seam-Sealed Vest with Compression Pants',
                'Layered Pullover with Quick-Dry Sweatpants',
                'Windproof Hoodie with Thermal Shorts'],
            'chic': [
                'Fitted Rain Jacket with Suede Ankle Boots',
                'Longline Raincoat over a Turtleneck Dress',
                'Waterproof Blazer with Leather Leggings',
                'Stylish Cape Coat with Umbrella Accessories',
                'Patterned Rainproof Boots with a Matching Poncho']
        },
        'cloudy': {
            'casual': [
                'Shacket (Shirt-Jacket) and Black Jeans',
                'Mock-Neck Sweater with Relaxed Pants',
                'Fitted Knit Vest over a Button-Up Shirt',
                'Raglan Sleeve Hoodie with Cargo Joggers',
                'Plaid Poncho over Skinny Jeans'],
            'formal': [
                'Cropped Wool Jacket and Wool Pants',
                'Longline Blazer with Tapered Trousers',
                'Layered Blouse with a Pleated Skirt',
                'Wool-Blend Shift Dress with Leather Boots',
                'Tailored Vest over a Long-Sleeve Shirt and Pants'],
            'sporty': [
                'Mock-Neck Sweatshirt and Joggers',
                'Fleece-Lined Hoodie with Training Pants',
                'Insulated Anorak with Compression Leggings',
                'Breathable Pullover with Performance Shorts',
                'Quick-Dry Long-Sleeve Tee with Joggers'],
            'chic': [
                'Soft Turtleneck Sweater and Paperbag Pants',
                'Puffer Vest over a Midi Skirt',
                'Layered Blanket Scarf with Heeled Ankle Boots',
                'Oversized Cardigan with Leather Pants',
                'Belted Duster Coat with Matching Gloves']
        },
        'windy': {
            'casual': [
                'Puffer Vest over a Long-Sleeve Tee',
                'Thick Hoodie with Cropped Joggers',
                'Knit Sweater with Corduroy Skirt',
                'Flannel Shirt with Layered Knitwear',
                'Windproof Bomber Jacket with Slim Jeans'],
            'formal': [
                'Wind-Resistant Coat with Slim Trousers',
                'Fleece-Lined Blazer over a Midi Dress',
                'Structured Overcoat with Tapered Pants',
                'Wool Cape with Tailored Boots',
                'Trench Coat with Silk Accessories'],
            'sporty': [
                'Performance Jacket with Tapered Joggers',
                'Waterproof Windbreaker with Quick-Dry Pants',
                'Lightweight Pullover with Insulated Shorts',
                'Breathable Hoodie with Stretch Leggings',
                'Rainproof Vest with Performance Tights'],
            'chic': [
                'Cocoon Coat with a Cashmere Scarf and Ankle Boots',
                'Wool Wrap Dress with Statement Earrings',
                'Tailored Skirt Suit with Gloves',
                'Layered Cardigan with Satin Pants',
                'Belted Long Coat with Heeled Booties']
        }
    },
    'winter': {
        'sunny': {
            'casual': [
                'Fleece-Lined Parka and Skinny Jeans',
                'Chunky Sweater and Ankle Boots',
                'Oversized Cardigan with Knit Leggings',
                'Plaid Scarf with a Wool Coat and Jeans',
                'Puffer Jacket with Fleece-Lined Pants'],
            'formal': [
                'Tailored Overcoat and Wool Suit',
                'Turtleneck Sweater with Plaid Trousers',
                'Velvet Blazer with Matching Skirt',
                'Cashmere Dress with Leather Heels',
                'Wool Wrap Coat with Lace Gloves'],
            'sporty': [
                'Puffer Jacket and Thermal Leggings',
                'Pom-Pom Beanie and Fleece Gloves',
                'Insulated Windbreaker with Training Tights',
                'Performance Hoodie with Athletic Trousers',
                'Breathable Winter Coat with Joggers'],
            'chic': [
                'Long Wool Coat with Fur-Lined Boots and a Statement Belt',
                'Shearling Jacket over a Pleated Skirt',
                'Embellished Sweater Dress with Chunky Jewelry',
                'Leather Trench with High-Waisted Jeans',
                'Wrap Coat with Oversized Earrings and Heeled Boots']
        },
        'rainy': {
            'casual': [
                'Waterproof Parka and Fleece-Lined Jeans',
                'Hunter Boots with a Flannel Shirt',
                'Hooded Rain Jacket with Wool Leggings',
                'Quilted Rain Coat with Waterproof Pants',
                'Insulated Vest with Thick Turtleneck'],
            'formal': [
                'Double-Breasted Raincoat and Dress Boots',
                'Tailored Wool Pants with Weather-Resistant Heels',
                'Sheer Waterproof Cape with Formal Trousers',
                'Belted Trench with a Wool Pencil Skirt',
                'Leather Gloves with an A-Line Rain Dress'],
            'sporty': [
                'Rain-Resistant Pullover with Sweatpants',
                'Hooded Anorak with Compression Tights',
                'Performance Rain Jacket with Insulated Leggings',
                'Rainproof Vest over a Hoodie and Joggers',
                'Quick-Dry Hoodie with Waterproof Track Pants'],
            'chic': [
                'Oversized Waterproof Coat with Patterned Rain Boots',
                'Stylish Transparent Rain Poncho with Velvet Gloves',
                'Statement Umbrella with Matching Trench',
                'Waterproof Wool Coat over a Midi Dress',
                'Clear Rain Jacket with a Fur-Lined Hood']
        },
        'cloudy': {
            'casual': [
                'Sherpa-Lined Jacket with Relaxed Fit Jeans',
                'Chunky Knit Pullover with Cropped Pants',
                'Cable Knit Cardigan with Plaid Trousers',
                'Oversized Sweater with High-Waisted Jeans',
                'Quilted Jacket with Corduroy Pants'],
            'formal': [
                'Cashmere Coat with a Wool Scarf',
                'Tailored Suit with Leather Gloves',
                'Wrap Skirt with a Mock-Neck Sweater',
                'Velvet Tunic with Tapered Trousers',
                'Double-Breasted Coat with Silk Stockings'],
            'sporty': [
                'Thermal Hoodie and Insulated Joggers',
                'Windproof Pullover with Training Pants',
                'Fleece Jacket over Stretch Leggings',
                'Breathable Sweatshirt with Quick-Dry Shorts',
                'Padded Anorak with Performance Pants'],
            'chic': [
                'Oversized Knit Sweater with a Maxi Skirt and Combat Boots',
                'Layered Poncho with Statement Jewelry',
                'Wool Turtleneck Dress with Knee-High Boots',
                'Fringed Wool Coat with Heeled Loafers',
                'Velvet Midi Skirt with a Sheer Blouse']
        },
        'windy': {
            'casual': [
                'Down Vest and Layered Knitwear',
                'Wool Scarf with a Quilted Jacket',
                'Longline Hoodie with Cropped Jeans',
                'Chunky Knit Pullover and Stretch Pants',
                'Heavy Bomber Jacket with Ankle Boots'],
            'formal': [
                'Tailored Longline Coat with Slim Trousers',
                'Structured Cape with Knee-Length Boots',
                'Woolen Dress and a Wide-Brim Hat',
                'Cashmere Wrap with Formal Pants',
                'Oversized Blazer with a Midi Skirt'],
            'sporty': [
                'Windproof Hoodie with Insulated Shorts',
                'Thermal Pullover with Fleece Leggings',
                'Performance Vest and Layered Long-Sleeve Tee',
                'Breathable Jacket with Tapered Joggers',
                'Moisture-Wicking Long Sleeve with Quick-Dry Pants'],
            'chic': [
                'Layered Trench with Leather Gloves',
                'Shearling-Lined Coat with Ankle Boots',
                'Belted Puffer Jacket with a Statement Scarf',
                'Oversized Wool Coat with Leather Leggings',
                'Fringe Poncho over a Turtleneck Dress']
        }
    }
}


def buildTree(data):
    if isinstance(data, dict):
        node = TreeNode()
        for key, value in data.items():
            node.children[key] = buildTree(value)
        return node
    else:  # Leaf node
        return TreeNode(outfits=data)


def traverseTree(root, keys):
    current_node = root
    for key in keys:
        if key in current_node.children:
            current_node = current_node.children[key]
        else:
            print("Invalid input.")
            return None
    return current_node

def validateInput(prompt, valid_options): # to make sure that the input is in the valid options
    while True:
        userinput = input(prompt).lower()
        if userinput in valid_options:
            return userinput
        print(f"Invalid input. Choose from {', '.join(valid_options)}.")

def getWeather(city):
    api_key = os.getenv('WEATHER_API_KEY')
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

# based on temperature and weather condition, we're converting them to season and weather.
def tempToSeasonWeather(temperature, weather_condition):
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

def showOutfits(outfits):
    if outfits:
        print("\nOutfit Suggestions:")
        for i, outfit in enumerate(outfits, 1):
            print(f"{i}. {outfit}")
    else:
        print("No outfits available.")

def suggestOutfit():
    outfit_tree = buildTree(outfits)

    while True:
        user_choice = input("\nChoose input method:\n1. Manual\n2. Location-based\n1 or 2: ")

        if user_choice == "1":
            season = validateInput("Enter season (spring, summer, fall, winter): ",
                                   ["spring", "summer", "fall", "winter"])
            weather = validateInput("Enter weather (sunny, rainy, cloudy, windy): ",
                                    ["sunny", "rainy", "cloudy", "windy"])
            style = validateInput("Enter style (casual, formal, sporty, chic): ",
                                  ["casual", "formal", "sporty", "chic"])
        elif user_choice == "2":
            city = input("Enter city: ").lower()
            style = validateInput("Enter style (casual, formal, sporty, chic): ",
                                  ["casual", "formal", "sporty", "chic"])
            temperature, weather_condition = getWeather(city)
            if temperature and weather_condition:
                season, weather = tempToSeasonWeather(temperature, weather_condition)
                print(f"\nDetected: Season = {season}, Weather = {weather}")
            else:
                print("Error retrieving weather data. Please try again.")
                continue

        else:
            print("Invalid input. Please choose 1 or 2.")
            continue

        path = [season, weather, style]
        outfit_node = traverseTree(outfit_tree, path)

        if outfit_node and outfit_node.outfits:
            showOutfits(outfit_node.outfits)
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

def viewWardrobe(wardrobe):
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

def editWardrobe(wardrobe):
    while True:
        item_type = validateInput("Enter the clothing type to edit (tops, bottoms, shoes, accessories, "
                                  "outerwear, dresses, underwear, sleepwear): ",
                                  ["tops", "bottoms", "shoes", "accessories", "outerwear", "dresses", "underwear",
                                   "sleepwear"])
        item_name = input("Enter the item name to edit: ")

        found = False
        for item in wardrobe[item_type]:
            if item["name"].lower() == item_name.lower():
                found = True

                # Edit item properties
                new_name = input("Enter the new name (or press Enter to keep the same): ")
                new_color = input("Enter the new color (or press Enter to keep the same): ")
                new_material = input("Enter the new material (or press Enter to keep the same): ")
                new_occasion = input("Enter the new occasion (or press Enter to keep the same): ")
                new_season = input("Enter the new season (or press Enter to keep the same): ")

                if new_name:
                    item["name"] = new_name
                if new_color:
                    item["color"] = new_color
                if new_material:
                    item["material"] = new_material
                if new_occasion:
                    item["occasion"] = new_occasion
                if new_season:
                    item["season"] = new_season

                print(f"Item '{item_name}' updated.")
                break

        if not found:
            print("Item not found in your wardrobe.")

        continue_editing = input("Do you want to edit another item? (yes/no): ").lower()
        if continue_editing != "yes":
            break

def addItem(wardrobe):
    while True:
        item_name = input("Enter the name of the item to add: ")
        item_type = validateInput("Enter the clothing type (tops, bottoms, shoes, accessories, "
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

def manageWardrobe():
    while True:
        action = validateInput("What would you like to do? (view/add/edit/back): ",
                               ["view", "add", "edit", "back"])

        if action == "view":
            viewWardrobe(wardrobe)
        elif action == "add":
            addItem(wardrobe)
        elif action == "edit":
            editWardrobe(wardrobe)
        elif action == "back":
            break

def main():
    while True:
        choice = input("\nWelcome! Choose an option:\n1. Wardrobe Management\n2. Outfit Suggestion\n1 or 2: ")

        if choice == "1":
            manageWardrobe()
        elif choice == "2":
            suggestOutfit()
        else:
            print("Invalid input. Please choose 1 or 2.")
            continue

        again = input("\nWould you like to go back to the main page?\nType 'yes' to go back or 'no' to quit the app: ").lower()
        if again != "yes":
            break

if __name__ == '__main__':
    main()
