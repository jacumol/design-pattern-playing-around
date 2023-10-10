from online_manager.electronic_online_manager import ElectronicOnlineManager
from online_manager.clothes_online_manager import ClothesOnlineManager
from online_manager.food_online_manager import FoodOnlineManager  

def main():
    electronic_online_manager = ElectronicOnlineManager()
    electronic_online_manager.sell_product() 

    clothes_online_manager = ClothesOnlineManager()
    clothes_online_manager.sell_product() 

    food_online_manager = FoodOnlineManager()
    food_online_manager.sell_product() 

    

if __name__ == "__main__":
    main()