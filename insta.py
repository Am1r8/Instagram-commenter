print("""\n\n\n\n
 _____          _          _____                                      _            
|_   _|        | |        /  __ \                                    | |           
  | | _ __  ___| |_ __ _  | /  \/ ___  _ __ ___  _ __ ___   ___ _ __ | |_ ___ _ __ 
  | || '_ \/ __| __/ _` | | |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __/ _ \ '__|
 _| || | | \__ \ || (_| | | \__/\ (_) | | | | | | | | | | |  __/ | | | ||  __/ |   
 \___/_| |_|___/\__\__,_|  \____/\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__\___|_|   
                                                                                   
                                                                                   
\n\n\n\n""")
print("You May Get Banned By Doing This, I AM NOT RESPONSIBLE FOR ANYTHING.\n\n\n")
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import random
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.1)

print_slow("Importing The Modules\n\n")
sleep(3)

# starting the program
# installing Chrome Driver
print_slow("Opening The Browser ... \n\n")
sleep(2)
browser = webdriver.Chrome(ChromeDriverManager().install())


# enter Your youtube Urls here
comments = input("Enter the comments you want to post under the posts and split them with ',':\n\n")
comm = comments.split(",")


usern = input("enter your instagram Username, so we can write comments!\n")
passw = input("enter your instagram Password, so we can write comments!\n")

#This are some variables to keep tracking of the posts
posts=0


browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(5) 

print_slow("\n\nPlease Do Not click on anything in the opened browser, you can get errors if you click.\n\n")
print_slow("You May Get Banned By Doing This, I AM NOT RESPONSIBLE FOR ANYTHING.\n\n\n")

def likeAndComm():
	global posts
	for y in range (1,4):
		for x in range(1,4):
			sleep(10)
			post = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div['+str(y)+']/div['+str(x)+']') 
			browser.implicitly_wait(3) 
			post.click()
			sleep(5)
			postLike = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
			sleep(5)
			try:
				comment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click() 
				comment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(random.choice(comm))	
				sleep(5)
				sendComment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/button[2]') 
				sendComment.click()
				sleep(5)
			except:
				print("commenting is not allowed on this post")
			posts+=1
			closePost=browser.find_element_by_xpath('/html/body/div[6]/div[3]/button')
			closePost.click()
			sleep(5)
		print('Number of posts: ' + str(posts))
	
	sleep(5)
	browser.get('https://www.instagram.com/explore/')
	sleep(5)
	likeAndComm()
	
		
def start():
	username = browser.find_element_by_name('username')
	username.send_keys(usern) 
	password = browser.find_element_by_name('password')
	password.send_keys(passw) 
	nextButton = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
	nextButton.click()
	sleep(5)
	try:
		notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
		notification.click()
	except:
		print_slow("Your Username or Password is Incorrect!")
	browser.get('https://www.instagram.com/explore/')
	sleep(5)
	likeAndComm()
	sleep(5)

try:	
	start()
except:
	print_slow("There is an error in the code please, contact AlPHA(developer)")