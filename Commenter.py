
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string

#Change this list to your wanted comments
comments = ['']

#This are some variables to keep tracking of the posts
posts=0

#Chromedriver path. Make sure to have the same Chromedriver version as your Google Chrome browser
#This is Brave browser path for me you can remove this or use it
driver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
# option.add_argument('headless')
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(5) 

def likeAndComm(): # Likes and Comments the first 9 posts
	global posts
	for y in range (1,4):
		for x in range(1,4):


			#you may get banned if you do this very fast 
			sleep(20)
			post = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div['+str(y)+']/div['+str(x)+']') 
			browser.implicitly_wait(3) 
			post.click()
			sleep(5)
			postLike = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
			sleep(5)
			try:
				comment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click() 
				comment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(random.choice(comments))	
				sleep(5)
				sendComment = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/button[2]') 
				sendComment.click()
				sleep(5)
			except:
				print("commenting is not allowed")
			posts+=1
			closePost=browser.find_element_by_xpath('/html/body/div[6]/div[3]/button')
			closePost.click()
			sleep(5)
		print ('Nr. of posts: ' +str(posts))
	
	sleep(5)
	browser.get('https://www.instagram.com/explore/')
	sleep(5)
	likeAndComm()
	

	
#your strater Function please fill it out and then start
def start():
	username = browser.find_element_by_name('username')
	username.send_keys('') # <- INSERT YOUR INSTAGRAM USERNAME HERE -------------------------------------------------------------------------------------------------------------------------
	password = browser.find_element_by_name('password')
	password.send_keys('') # <- INSERT YOUR INSTAGRAM PASSWORD HERE -----------------------------------------------------------------------------------------------------------------------
	nextButton = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
	nextButton.click()
	sleep(5)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	sleep(5)
	likeAndComm()
	sleep(5)
	
start()