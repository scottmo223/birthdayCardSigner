# Birthday Card Signer

I use this simple program to sign birthday cards I'm invited to sign at openme.com.

I receive 5 - 10 birthday cards a month to sign. I write the same exact thing in all of them and it has gotten pretty tedious. I decided to keep it fun and easy by writing this little program.


## Set Up
There needs to be a CSV file with two columns in it: **firstname** and **url**.

### It will looke like this 
```csv
firstname,url
Nikki,https://www.openme.com/###
Philip,https://www.openme.com/###
```

## How to Use
I hard coded everything except my password in the program. Go in and change what you need. You will then need to create the csv file which I named birthdayNames.csv - this file needs to be in the same directory as the birthdayCardSigner.py file.

Run the program and it will go to each URL listed in the csv file. It will then write the message and add the firstname from the csv file in the message. Before the card signing is submitted the program will ask if you want to procede - so you can double check the card names and stuff. Type **y** for yes and **n** to skip that card.

## BTW
This program uses selenium. I use the chrome driver. The chrome driver will need to be installed if it is used. Check out Selenium's docs for more info.