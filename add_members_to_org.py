from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def main():
    """
    CHANGE:
        members
        roster_page
        path
        username
        password
    """

    """
    CHANGE FILE NAME
    """
    # Read name.# from txt file and convert to list of strings
    members_file = 'YOUR_NEW_MEMBERS_FILE.txt' # text file should have one name.# per line.
    with open(members_file) as f:
        members = f.read().splitlines()

    # URL to club roster in student org management
    roster_page = 'https://activities.osu.edu/secure/studentorgs/roster.aspx?org_id=YOUR_ORG_ID'

    # Add Chrome Options
    options = webdriver.ChromeOptions()
    options.add_argument('-incognito') # New incognito window
    options.add_experimental_option('detach', True) # Leaves browser open after executing the program

    # Create a new Chrome session
    """
    CHANGE THE PATH TO THE LOCATION OF YOUR WEB DRIVER
    """
    path = r'C:\Users\jorda\YOUR_LOCAL_FOLDER\chromedriver' # location of your Chrome Driver
    driver = webdriver.Chrome(executable_path=path, options=options)

    # Tell the user a browser will open
    print("Opening a new browser window.  If it stops in the middle of adding members, just click 'cancel'.")

    # Direct browser to student org
    driver.get(roster_page)
    delay = 3
    driver.implicitly_wait(delay)

    # Provide your OSU username and password
    """
    CHANGE TO YOUR USERNAME & PASSWORD
    """
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'

    # Wait for page to load
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))

    # username
    username_form = driver.find_element_by_id('username')
    username_form.send_keys(username)

    # password
    password_form = driver.find_element_by_id('password')
    password_form.send_keys(password)

    # Intentionally throw error to watch
    login_button = driver.find_element_by_id('submit')
    login_button.click()

    # Store successes and failures
    added_members = []
    failed_members = []

    # Add each member from the list of members to the roster
    for individual in members:
        try:
            # Add members
            add_members_button = driver.find_element_by_id('ctl00_ContentBody_uc1_roster_lnk_add_members')
            add_members_button.click()

            # OSU General Member Box
            OSU_username_box = driver.find_element_by_id('ctl00_ContentBody_uc1_roster_rpt_listing_ctl01_txt_osu_id')
            OSU_username_box.send_keys(individual)

            # Find individual button
            find_individual_button = driver.find_element_by_id('ctl00_ContentBody_uc1_roster_rpt_listing_ctl01_btnGrabStudentInfo')
            find_individual_button.click()

            # Update roster button
            update_roster_button = driver.find_element_by_id('ctl00_ContentBody_uc1_roster_lnk_update_roster')
            update_roster_button.click()

            # Record added members
            added_members.append(individual)
        except:
            # Record failed members
            failed_members.append(individual)
            
            # Click cancel button
            cancel_button = driver.find_element_by_id('ctl00_ContentBody_uc1_roster_lnk_cancel_roster_update')
            cancel_button.click()

    # Print members that were added to roster and those that didn't
    print("Added: {}".format(added_members))
    print("Failed to add: {}".format(failed_members))

    # Print next steps
    print("\nBe sure to checkmark all the red lines and press the 'Approve' button at the bottom to save changes.")

if __name__ == '__main__':
    main()
