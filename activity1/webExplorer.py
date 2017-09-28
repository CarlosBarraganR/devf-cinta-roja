from threading import Timer
import webbrowser

url = 'http://www.python.org/'

"""
    opens a browser window with the url
"""
def open_browser():
    webbrowser.open_new(url)


"""
    starts timer to open browser
"""
def run_open_browser():
    timer = Timer(2, open_browser)
    timer.start()


"""
    validate_state() -> string
    
    user feedback and validates if the user is still working or not 
"""
def validate_state():
    user_input = int(input("yes = 1, no = 0: \n"))
    return user_input


"""
    Opens a web browser every period of time to validate if the user is still working
"""
def open_browser_main():
    done = False

    while not done:
        run_open_browser()
        print "Are you done working?"
        state_answer = validate_state()
        if state_answer == 1:
            print "Exit routine"
            done = True


open_browser_main()