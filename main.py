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
    dashboard = DashboardMenu(user_controller)

    while not menu.get_shutdown():
        if not dashboard.get_logged_in():
            menu.set_logged_in(False)

        if not menu.get_logged_in():
            menu.set_user(None)
            menu.set_decision(False)
            menu.display_menu()
        
        if menu.get_logged_in and not menu.get_shutdown():
            dashboard.set_logged_in(True)
            dashboard.set_user(menu.get_user())
            dashboard.set_decision(False)
            dashboard.display()

    db.disconnect()
    print("System Shutting Down...")

if __name__ == "__main__":
    main()
