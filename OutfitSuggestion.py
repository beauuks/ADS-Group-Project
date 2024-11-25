class TreeNode:
    def __init__(self, value = None, left = None, right = None, outfits = None):
        self.value = value
        self.left = left
        self.right = right
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


# Build a binary tree
def build_tree():
    # leaf nodes (the outfits)
    # leaf nodes for spring
    spring_sunny_casual = TreeNode("casual", outfits=outfits['spring']['sunny']['casual'])
    spring_sunny_formal = TreeNode("formal", outfits=outfits['spring']['sunny']['formal'])
    spring_sunny_sporty = TreeNode("sporty", outfits=outfits['spring']['sunny']['sporty'])
    spring_sunny_chic = TreeNode("chic", outfits=outfits['spring']['sunny']['chic'])

    spring_rainy_casual = TreeNode("casual", outfits=outfits['spring']['rainy']['casual'])
    spring_rainy_formal = TreeNode("formal", outfits=outfits['spring']['rainy']['formal'])
    spring_rainy_sporty = TreeNode("sporty", outfits=outfits['spring']['rainy']['sporty'])
    spring_rainy_chic = TreeNode("chic", outfits=outfits['spring']['rainy']['chic'])

    # leaf nodes for summer
    summer_sunny_casual = TreeNode("casual", outfits=outfits['summer']['sunny']['casual'])
    summer_sunny_formal = TreeNode("formal", outfits=outfits['summer']['sunny']['formal'])
    summer_sunny_sporty = TreeNode("sporty", outfits=outfits['summer']['sunny']['sporty'])
    summer_sunny_chic = TreeNode("chic", outfits=outfits['summer']['sunny']['chic'])

    summer_rainy_casual = TreeNode("casual", outfits=outfits['summer']['rainy']['casual'])
    summer_rainy_formal = TreeNode("formal", outfits=outfits['summer']['rainy']['formal'])
    summer_rainy_sporty = TreeNode("sporty", outfits=outfits['summer']['rainy']['sporty'])
    summer_rainy_chic = TreeNode("chic", outfits=outfits['summer']['rainy']['chic'])

    # leaf nodes for fall
    fall_sunny_casual = TreeNode("casual", outfits=outfits['fall']['sunny']['casual'])
    fall_sunny_formal = TreeNode("formal", outfits=outfits['fall']['sunny']['formal'])
    fall_sunny_sporty = TreeNode("sporty", outfits=outfits['fall']['sunny']['sporty'])
    fall_sunny_chic = TreeNode("chic", outfits=outfits['fall']['sunny']['chic'])

    fall_rainy_casual = TreeNode("casual", outfits=outfits['fall']['rainy']['casual'])
    fall_rainy_formal = TreeNode("formal", outfits=outfits['fall']['rainy']['formal'])
    fall_rainy_sporty = TreeNode("sporty", outfits=outfits['fall']['rainy']['sporty'])
    fall_rainy_chic = TreeNode("chic", outfits=outfits['fall']['rainy']['chic'])

    # leaf nodes for winter
    winter_sunny_casual = TreeNode("casual", outfits=outfits['winter']['sunny']['casual'])
    winter_sunny_formal = TreeNode("formal", outfits=outfits['winter']['sunny']['formal'])
    winter_sunny_sporty = TreeNode("sporty", outfits=outfits['winter']['sunny']['sporty'])
    winter_sunny_chic = TreeNode("chic", outfits=outfits['winter']['sunny']['chic'])

    winter_rainy_casual = TreeNode("casual", outfits=outfits['winter']['rainy']['casual'])
    winter_rainy_formal = TreeNode("formal", outfits=outfits['winter']['rainy']['formal'])
    winter_rainy_sporty = TreeNode("sporty", outfits=outfits['winter']['rainy']['sporty'])
    winter_rainy_chic = TreeNode("chic", outfits=outfits['winter']['rainy']['chic'])

    # Group the styles into two categories : casual/formal and sporty/chic
    spring_sunny_casual_formal = TreeNode("casual_formal", left=spring_sunny_casual, right=spring_sunny_formal)
    spring_sunny_sporty_chic = TreeNode("sporty_chic", left=spring_sunny_sporty, right=spring_sunny_chic)
    spring_rainy_casual_formal = TreeNode("casual_formal", left=spring_rainy_casual, right=spring_rainy_formal)
    spring_rainy_sporty_chic = TreeNode("sporty_chic", left=spring_rainy_sporty, right=spring_rainy_chic)

    summer_sunny_casual_formal = TreeNode("casual_formal", left=summer_sunny_casual, right=summer_sunny_formal)
    summer_sunny_sporty_chic = TreeNode("sporty_chic", left=summer_sunny_sporty, right=summer_sunny_chic)
    summer_rainy_casual_formal = TreeNode("casual_formal", left=summer_rainy_casual, right=summer_rainy_formal)
    summer_rainy_sporty_chic = TreeNode("sporty_chic", left=summer_rainy_sporty, right=summer_rainy_chic)

    fall_sunny_casual_formal = TreeNode("casual_formal", left=fall_sunny_casual, right=fall_sunny_formal)
    fall_sunny_sporty_chic = TreeNode("sporty_chic", left=fall_sunny_sporty, right=fall_sunny_chic)
    fall_rainy_casual_formal = TreeNode("casual_formal", left=fall_rainy_casual, right=fall_rainy_formal)
    fall_rainy_sporty_chic = TreeNode("sporty_chic", left=fall_rainy_sporty, right=fall_rainy_chic)

    winter_sunny_casual_formal = TreeNode("casual_formal", left=winter_sunny_casual, right=winter_sunny_formal)
    winter_sunny_sporty_chic = TreeNode("sporty_chic", left=winter_sunny_sporty, right=winter_sunny_chic)
    winter_rainy_casual_formal = TreeNode("casual_formal", left=winter_rainy_casual, right=winter_rainy_formal)
    winter_rainy_sporty_chic = TreeNode("sporty_chic", left=winter_rainy_sporty, right=winter_rainy_chic)

    # Weather : sunny, rainy
    spring_sunny = TreeNode("sunny", left=spring_sunny_casual_formal, right=spring_sunny_sporty_chic)
    spring_rainy = TreeNode("rainy", left=spring_rainy_casual_formal, right=spring_rainy_sporty_chic)

    summer_sunny = TreeNode("sunny", left=summer_sunny_casual_formal, right=summer_sunny_sporty_chic)
    summer_rainy = TreeNode("rainy", left=summer_rainy_casual_formal, right=summer_rainy_sporty_chic)

    fall_sunny = TreeNode("sunny", left=fall_sunny_casual_formal, right=fall_sunny_sporty_chic)
    fall_rainy = TreeNode("rainy", left=fall_rainy_casual_formal, right=fall_rainy_sporty_chic)

    winter_sunny = TreeNode("sunny", left=winter_sunny_casual_formal, right=winter_sunny_sporty_chic)
    winter_rainy = TreeNode("rainy", left=winter_rainy_casual_formal, right=winter_rainy_sporty_chic)

    # Seasons
    spring = TreeNode("spring", left=spring_sunny, right=spring_rainy)
    summer = TreeNode("summer", left=summer_sunny, right=summer_rainy)
    fall = TreeNode("fall", left=fall_sunny, right=fall_rainy)
    winter = TreeNode("winter", left=winter_sunny, right=winter_rainy)

    # Group the seasons into two : spring/summer and fall/winter
    spring_summer = TreeNode("spring_summer", left=spring, right=summer)
    fall_winter = TreeNode("fall_winter", left=fall, right=winter)

    # Root
    season_tree = TreeNode("seasons", left=spring_summer, right=fall_winter)
    return season_tree


def get_outfit():
    outfit_tree = build_tree()

    # Get inputs
    season = input("Enter season (spring, summer, fall, winter): ").lower()
    weather = input("Enter weather (sunny, rainy): ").lower()
    style = input("Enter style (casual, formal, sporty, chic): ").lower()

    if season == "spring" or season == "summer":
        season_node = outfit_tree.left
        if season == "spring":
            season_node = season_node.left
        elif season == "summer":
            season_node = season_node.right
    elif season == "fall" or season == "winter":
        season_node = outfit_tree.right
        if season == "fall":
            season_node = season_node.left
        if season == "winter":
            season_node = season_node.right
    else:
        print("Invalid season input.")
        return

    if weather == "sunny":
        weather_node = season_node.left
    elif weather == "rainy":
        weather_node = season_node.right
    else:
        print("Invalid weather input.")
        return

    if style == "casual" or style == "formal":
        style_node = weather_node.left
        if style == "casual":
            style_node = style_node.left
        elif style == "formal":
            style_node = style_node.right
    elif style == "sporty" or style == "chic":
        style_node = weather_node.right
        if style == "sporty":
            style_node = style_node.left
        elif style == "chic":
            style_node = style_node.left
    else:
        print("Invalid style input.")
        return

    print("\nOutfit Suggestions:")
    if style_node.outfits:
        for i, outfit in enumerate(style_node.outfits, 1):
            print(f"{i}. {outfit}")
    else:
        print("No outfits available.")


if __name__ == '__main__':
    get_outfit()
