# This script checks http://www.mangapanda.com/ to test when a new volume of anime is released.

from selenium import webdriver
import smtplib
import logging

class WebDriver():
	def __init__(self, link="", driver = webdriver.Firefox(), element=[], chapters=[]):
		self.driver = driver
		self.link = link
		self.driver.get(self.link)
		self.element = element
		self.chapters = chapters

	def getElement(self, xpath):
		self.element = self.driver.find_element_by_xpath(xpath)

	def getChapters(self, tag):
		self.chapters = self.element.find_elements_by_tag_name(tag)

	def done(self):
		self.driver.close()

class Text():
	def __init__(self, server = smtplib.SMTP( "smtp.gmail.com", 587 )):
		self.server = server
		self.server = smtplib.SMTP( "smtp.gmail.com", 587 )
		self.server.starttls()
		self.server.login( 'email@gmail.com', 'password' )
	
	def sendText(self, message):
		# Send text message through SMS gateway of destination number
		self.server.sendmail( 'Subject', 'phone_number@txt.att.net', message)
		logging.info(message)
	
class Anime():
	def __init__(self, anime_name="", anime_file="", current_volume_name=0, previous_volume_name=0, logging=logging.basicConfig(level=logging.INFO,filename='anime_update.log',format='%(asctime)s %(message)s')):
		self.anime_name = anime_name
		self.anime_file = anime_file
		self.current_volume_name = current_volume_name
		self.previous_volume_name = previous_volume_name
		self.logging = logging

	def convertStr(self, s):
		# Convert string to int. If there is an error set it to 0 int.
	    try:
	        ret = int(s)
	    except ValueError:
	        ret = 0
	    return ret

	def compareVersions(self, chapters):
		# Volume name and number from website.
		most_recent_volume = self.obtainVolumeNumber(chapters[0].text)
		most_recent_volume_name = chapters[0].text

		print("The newest chapters is: ", chapters[0].text)
		print("Volume: ", self.obtainVolumeNumber(chapters[0].text))

		# Dragon Ball Super text file to keep track of new volumes.
		#db_super = 'super.txt'

		# Convert volume numbers in both the text file (previous), and new from the website to int.
		# That way we can do comparisons.
		most_recent_volume_current = str(most_recent_volume).replace("[","").replace("]","") + "\n"
		previous_most_recent_file = self.readNewestIssueInFile()

		print("Comparing previously recorded values vs. obtains value")
		print(int(most_recent_volume_current), ">", int(previous_most_recent_file))
		if (int(most_recent_volume_current) > int(previous_most_recent_file)):
			print("There is a new volume out")
			self.writeToFile(most_recent_volume_current)
			print("Newest issue reads: ", self.readNewestIssueInFile())
			text_message = Text()
			message=self.anime_name + " " + most_recent_volume_current
			text_message.sendText(message)
			logging.info(self.anime_name + ", New Volume: " + most_recent_volume_name)
		else:
			print("No new volume")
			print("Current volume at: ", previous_most_recent_file)
			logging.info(self.anime_name + ", No new volume")

	# Obtain the int value from a string.
	def obtainVolumeNumber(self, name):
		found = [int(s) for s in name.split() if s.isdigit()]
		return found

	# Append the volume number to the file.
	def writeToFile(self, line):
		with open(self.anime_file, "a") as file_name:
			file_name.write(line)
		file_name.close()

	# Reads all lines of the anime file, sorts them, and then selects the greatest value.
	def readNewestIssueInFile(self):
		lines=[]
		f = open(self.anime_file, 'r+')
		for line in f:
			print(line)
			lines.append(self.convertStr(line))
		f.close()
		lines.sort()
		#print("Lines read in file: ", lines)
		if len(lines) <= 0:
			return 0
		else:
			return lines[len(lines) - 1]

	def removeBrackets(self, item):
		return str(item).replace("[","").replace("]","")


DRAGON_BALL_SUPER_LINK="http://www.mangapanda.com/dragon-ball-super"
RECENT_MANGA_XPATH='//*[@id="latestchapters"]/ul'
TAG='li'
web_driver = WebDriver(DRAGON_BALL_SUPER_LINK)
web_driver.getElement(RECENT_MANGA_XPATH)
web_driver.getChapters(TAG)

DRAGON_BALL_SUPER_NAME="Dragon Ball Super"
DRAGON_BALL_SUPER_FILE='super.txt'
dragon_ball_super = Anime(DRAGON_BALL_SUPER_NAME, DRAGON_BALL_SUPER_FILE)
dragon_ball_super.compareVersions(web_driver.chapters)



ONE_PIECE_LINK="http://www.mangapanda.com/one-piece"
RECENT_MANGA_XPATH='//*[@id="latestchapters"]/ul'
TAG='li'
web_driver = WebDriver(ONE_PIECE_LINK)
web_driver.getElement(RECENT_MANGA_XPATH)
web_driver.getChapters(TAG)

ONE_PIECE_NAME="One Piece"
ONE_PIECE_FILE='one_piece.txt'
one_piece = Anime(ONE_PIECE_NAME, ONE_PIECE_FILE)
one_piece.compareVersions(web_driver.chapters)


web_driver.done()
