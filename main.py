from frontend.ui.main_menu import main_menu
from frontend.banners import banners
from frontend.ui.dashboard_menu import dashboard_menu
def main():
    decor = banners
    decor.display_welcome()
    menu= main_menu()
    menu.display_menu()
    if menu.get_logged_in():
        dashboard = dashboard_menu()
        dashboard.set_logged_in(menu.get_logged_in())
        dashboard.set_user(menu.get_user())
        dashboard.display()

main()