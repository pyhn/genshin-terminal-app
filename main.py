from frontend.ui.main_menu import MainMenu
from frontend.banners import banners
from frontend.ui.dashboard_menu import DashboardMenu
from data.db_manager import DatabaseManager
from controllers.user_controller import UserController

def main():
    db = DatabaseManager()
    db.connect()
    db.create_user_table()
    
    decor = banners
    decor.display_welcome()
    
    user_controller = UserController(db)
    menu = MainMenu(user_controller)
    
    
    while not menu.get_shutdown():
        menu.display_menu() 
        if menu.get_logged_in():
            dashboard = DashboardMenu(user_controller, menu.get_user())
            dashboard.display()
    
    db.disconnect()
    print("System Shutting Down...")

if __name__ == "__main__":
    main()
