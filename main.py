from frontend.ui.main_menu import main_menu
from frontend.banners import banners
from frontend.ui.dashboard_menu import dashboard_menu
from data.db_manager import db_manager
def main():
    db = db_manager()
    db.connect()
    db.create_user_table()
    decor = banners
    decor.display_welcome()
    menu = main_menu()
    menu.display_menu()
    if menu.get_shutdown():
        db.disconnect()
        print(f"System Shutting Down...")
        exit()
        
    if menu.get_logged_in():
        dashboard = dashboard_menu()
        dashboard.set_logged_in(menu.get_logged_in())
        dashboard.set_user(menu.get_user())
        dashboard.display()

main()