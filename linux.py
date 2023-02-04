import os
from time import sleep
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
import random
from pystyle import Colors, Colorate
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN

initialize_VPN(save=1,area_input=['complete rotation'])

#for i in range(3):
#    rotate_VPN()
#    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
#    time.sleep(10)


PROXY = "96.70.52.227:48324" #  HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("ignore-certificate-errors")




mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
sex = ["Un homme","Une femme"]
names = [  "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",  "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Avery", "Sofia",  "Ella", "Madison", "Scarlett", "Victoria", "Aria", "Grace", "Chloe",  "Camila", "Penelope", "Riley", "Layla", "Lillian", "Natalie", "Hazel",  "Bella", "Violet", "Aurora", "Lucy", "Savannah", "Audrey", "Brooklyn",  "Nova", "Mila", "Aaliyah", "Arianna", "Allison", "Genevieve", "Adalynn",  "Aubree", "Kaylee", "Aurora", "Ellie", "Aurora", "Hannah", "Aurora",  "Lydia", "Aurora", "Eleanor", "Aurora", "Stella", "Aurora", "Paisley",  "Aurora", "Everly", "Aurora", "Anna", "Aurora", "Caroline", "Aurora",  "Natalie", "Aurora", "Samantha", "Aurora",  "Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah",  "Lucas", "Mason", "Logan", "Alexander", "Ethan", "Michael", "Daniel",  "Matthew", "Aiden", "Henry", "Joseph", "Jackson", "Samuel", "Sebastian",  "David", "Carter", "Wyatt", "Jayden", "John", "Owen", "Dylan", "Luke",  "Gabriel", "Anthony", "Isaac", "Grayson", "Jack", "Julian", "Levi",  "Christopher", " Joshua", "Andrew", "Lincoln", "Mateo", "Ryan", "Jaxon",  "Nathan", "Aaron", "Isaiah", "Thomas", "Charles", "Caleb", "Josiah",  "Christian", "Hunter", "Eli", "Jonathan", "Connor", "Landon", "Adrian",  "Asher", "Cameron", "Leo", "Theodore", "Jeremiah", "Hudson", "Robert",  "Easton", "Nolan", "Nicholas", "Ezra", "Colton", "Angel", "Brayden",  "Jordan", "Dominic", "Austin", "Ian", "Adam", "Elias", "Jaxson",  "Greysen", "Evan", "Jose", "Ezekiel"]
low_names = [  "emma", "olivia", "ava", "isabella", "sophia", "mia", "charlotte", "amelia",  "harper", "evelyn", "abigail", "emily", "elizabeth", "avery", "sofia",  "ella", "madison", "scarlett", "victoria", "aria", "grace", "chloe",  "camila", "penelope", "riley", "layla", "lillian", "natalie", "hazel",  "bella", "violet", "aurora", "lucy", "savannah", "audrey", "brooklyn",  "nova", "mila", "aaliyah", "arianna", "allison", "genevieve", "adalynn",  "aubree", "kaylee", "aurora", "ellie", "aurora", "hannah", "aurora",  "lydia", "aurora", "eleanor", "aurora", "stella", "aurora", "paisley",  "aurora", "everly", "aurora", "anna", "aurora", "caroline", "aurora",  "natalie", "aurora", "samantha", "aurora",  "liam", "noah", "william", "james", "oliver", "benjamin", "elijah",  "lucas", "mason", "logan", "alexander", "ethan", "michael", "daniel",  "matthew", "aiden", "henry", "joseph", "jackson", "samuel", "sebastian",  "david", "carter", "wyatt", "jayden", "john", "owen", "dylan", "luke",  "gabriel", "anthony", "isaac", "grayson", "jack", "julian", "levi",  "christopher", " joshua", "andrew", "lincoln", "mateo", "ryan", "jaxon",  "nathan", "aaron", "isaiah", "thomas", "charles", "caleb", "josiah",  "christian", "hunter", "eli", "jonathan", "connor", "landon", "adrian",  "asher", "cameron", "leo", "theodore", "jeremiah", "hudson", "robert",  "easton", "nolan", "nicholas", "ezra", "colton", "angel", "brayden",  "jordan", "dominic", "austin", "ian", "adam", "elias", "jaxson",  "greysen", "evan", "jose", "ezekiel"]

def rdmVal(a,b):
    return str(random.randrange(a,b,1))

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password

def name(a):
    if a:
        return f"{random.choice(names)}_{random.choice(names)}{rdmVal(1000,10000)}"
    else:
        return f"{random.choice(low_names)}{rdmVal(1000,10000)}"

def tsleep():
    return random.uniform(0.25,1)

def send_keys_delay_random(controller,keys,min_delay,max_delay):
    for key in keys:
        controller.send_keys(key)
        time.sleep(random.uniform(min_delay,max_delay))

accountAmount = 6976976

def counter():
    accountAmount = accountAmount + 1

class createAccount():
    def __init__(self):
        rotate_VPN()
        isCreating = rdmVal(1,100)
        print(isCreating)
        print(isCreating)
        print(isCreating)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("ignore-certificate-errors")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-3d-apis")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(
            executable_path="chromedriver",
            options=options
            )
        bot = self.driver
        #self.driver.get('chaturbate.com/in/?tour=g4pe&campaign=WeT21&track=default')
        #self.driver.get('https://chaturbate.com/in/?tour=4uT2&campaign=LkrKo&track=default')
        self.driver.get('https://chaturbate.com/in/?tour=g4pe&campaign=WeT21&track=default')

        if int(isCreating) >35:
            print(Colorate.Horizontal(Colors.green_to_black, "Compte en cour de création.", 1))
            print(Colorate.Horizontal(Colors.green_to_black, "Compte en cour de création.", 1))
            print(Colorate.Horizontal(Colors.green_to_black, "Compte en cour de création.", 1))

            self.driver.find_element(By.CSS_SELECTOR, f".room_list_room:nth-child({rdmVal(1,10)}) .png").click()

            frame = self.driver.find_element(By.ID,'join_iframe')
            print('Frame Trouvé')
            self.driver.switch_to.frame(frame)
            print('Frame selectionné')
            #Nom d'utilisateur
            in_username = self.driver.find_element(By.ID, "husername")
            print('username trouver')
            in_username.click()
            print('username cliquer')
            send_keys_delay_random(in_username,name(True),0.01,0.05)
            print('username ecrit')

            #Mot de passe
            in_password = self.driver.find_element(By.ID, "hpassword")
            print('mdp trouver')
            in_password.click()
            print('mdp cliquer')
            send_keys_delay_random(in_password,generate_password(int(rdmVal(13,18))),0.01,0.05)
            print('mdp ecrit')

            #Adresse mail
            in_email = self.driver.find_element(By.ID, "id_email")
            print('email trouver')
            in_email.click()
            print('email cliquer')
            send_keys_delay_random(in_email,f"{name(False)}@gmail.com",0.01,0.05)
            print('email ecrit')

            self.driver.find_element(By.ID, "id_birthday_day").click()
            print('jour trouver')
            dropdown = self.driver.find_element(By.ID, "id_birthday_day")
            sleep(tsleep())
            dropdown.find_element(By.XPATH, f"//option[. = '{rdmVal(1,27)}']").click()
            print('jour selectionner')

            self.driver.find_element(By.ID, "id_birthday_month").click()
            print('mois trouver')
            dropdown = self.driver.find_element(By.ID, "id_birthday_month")
            sleep(tsleep())
            dropdown.find_element(By.XPATH, f"//option[. = '{random.choice(mois)}']").click()
            print('mois selectionner')

            self.driver.find_element(By.ID, "id_birthday_year").click()
            print('année trouver')
            dropdown = self.driver.find_element(By.ID, "id_birthday_year")
            sleep(tsleep())
            dropdown.find_element(By.XPATH, f"//option[. = '{rdmVal(1950,2003)}']").click()
            print('année selectionner')

            self.driver.find_element(By.ID, "id_gender").click()
            print('sexe trouver')
            dropdown = self.driver.find_element(By.ID, "id_gender")
            dropdown.find_element(By.XPATH, f"//option[. = '{random.choice(sex)}']").click()
            print('sexe selectionner')

            self.driver.find_element(By.ID, "id_terms").click()
            print('checkbox 1 trouver')
            sleep(tsleep())
            self.driver.find_element(By.ID, "id_privacy_policy").click()
            print('checkbox 2 trouver')
            sleep(tsleep()) 
            self.driver.find_element(By.ID, "formsubmit").click()
            print('Confirmation trouver')
            waitTime = rdmVal(13,17)
            #accountAmount = accountAmount + 1
            print(f'Attente de {waitTime} secondes avant relance du script.')
            sleep(int(waitTime))
        else:
            print(Colorate.Horizontal(Colors.red_to_black, "Aucun compte crée cette fois-ci.", 1))
            print(Colorate.Horizontal(Colors.red_to_black, "Aucun compte crée cette fois-ci.", 1))
            print(Colorate.Horizontal(Colors.red_to_black, "Aucun compte crée cette fois-ci.", 1))
            sleep(1)
        self.driver.quit()
        relaunch()


def relaunch():
    createAccount()


createAccount()