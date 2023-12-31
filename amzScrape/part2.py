# importing libraries
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def main(URL):

	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

	webpage = requests.get(URL, headers=HEADERS)

	soup = BeautifulSoup(webpage.content, "lxml")

	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	print("product Title = ", title_string)


	# retrieving price
	try:
		price = soup.find(
			"span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
		# we are omitting unnecessary spaces
		# and commas form our string
	except AttributeError:
		price = "NA"
	print("Products price = ", price)


	# retrieving product rating
	try:
		rating = soup.find("i", attrs={
						'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

	except AttributeError:

		try:
			rating = soup.find(
				"span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = "NA"
	print("Overall rating = ", rating)

	try:
		review_count = soup.find(
			"span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

	except AttributeError:
		review_count = "NA"
	print("Total reviews = ", review_count)

	# print availablility status
	try:
		available = soup.find("div", attrs={'id': 'availability'})
		available = available.find("span").string.strip().replace(',', '')

	except AttributeError:
		available = "NA"
	print("Availability = ", available)



if __name__ == '__main__':

	# iterating over the urls
	# for url in urls:
	main('https://www.amazon.in/Skybags-Brat-Black-Casual-Backpack/dp/B08Z1HHHTD/ref=sr_1_3?keywords=bags&qid=1692722807&sr=8-3')
