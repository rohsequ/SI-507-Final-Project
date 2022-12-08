# SI-507-Final-Project
# Project Overview:
The main objective of this project is to build a web application using a Python Framework that allows users to get top places to visit recommendations for their country, state, and city of choice. The web application also picks up your current location based on the system IP address. The user will be able to log in to the web application, create a profile and modify certain information like photo, bio, etc. The final page will display the top Places to visit in the selected city based on top reviews on Yelp. 

# GitHub Link:
-
# Instructions for running the code:
•	Please download the code zip file and unzip it at your desired location.
•	Open a terminal and navigate to that location using the “cd” command.
•	Run the command “pip install -r requirements.txt --user” to install the necessary dependencies.
•	The next main step is to get the API key from Yelp Fusion API Developers page:
o	Go to https://www.yelp.com/developers/documentation/v3/authentication and create your app according to the instruction.
o	Once you get your API key, create a file called .env under “front_page_ip” folder.
o	Inside the “.env” file add the following line: 
YELP_API_KEY=<ADD_YOUR_API_KEY>
o	Replace the <ADD_YOUR_API_KEY> part with the API key you copied from the previous steps.
•	Next, we need to get the API key from your Google developer account for OAuth Sign-in using the Google Account feature.
o	Step 1 - Go to Google Developers Console
https://console.cloud.google.com/projectselector2/apis/dashboard?supportedpurview=project. 
o	Step 2 - Go to the “Credentials” section in the left menu and create a new project
o	Step 3 - In the Create credentials menu, select OAuth client ID
o	Step 4 - Select web application as the type of application and fill in the required information.
o	Authorized redirect URIs is where users will be redirected to after they are authenticated.

 ![image](https://user-images.githubusercontent.com/81701847/206368260-7860381f-fbd3-4ee4-98e7-1e4933579708.png)

o	Please copy the URL from the above image as it is in your case as well.
o	Now you will be provided with a Client ID and Client Secret which we will be adding  in the “.env” file that you would need to create in the “mypage” folder that contains “settings.py” file.
o	Open the “.env” file that you just created and copy the following lines with the necessary modifications:
GOOGLE_KEY=<ADD_YOUR_API_KEY>
GOOGLE_SECRET=<ADD_YOUR_SECRET_KEY>
o	Copy the API key and the Secret Key from the previous GitHub page and paste it into the mentioned location in the .env file.
•	We also need to get the API key from your GitHub account for OAuth Sign-in using the GitHub Account feature.
o	Step 1 - Login to your GitHub account
o	Step 2 - Go to Settings -> Developer Settings -> OAuth Apps -> New OAuth App
o	Step 3 - Fill in the information 

![image](https://user-images.githubusercontent.com/81701847/206368344-0cf889dd-76d1-4cd5-8260-1e68bff5d647.png)

o	Except for the Authorization callback URL, you can fill out the rest of the information as you like.
o	Authorization callback URL is the most important part of setting up your OAuth application. After a user is successfully authenticated, Github returns him/her to this callback URL. PLEASE USE THE SAME ONE IN YOUR CASE AS WELL.
o	Once you have access to the API key and Secret key, go to the “mypage” folder which has the “settings.py” file, and create a new file and name it “.env”.
o	Open the “.env” file that you just created and copy the following lines with the necessary modifications:

GITHUB_KEY=<ADD_YOUR_API_KEY>
GITHUB_SECRET=<ADD_YOUR_SECRET_KEY>
o	Copy the API key and the Secret Key from the previous GitHub page and paste it into the mentioned location in the .env file.
•	Once all the previous steps have been successfully completed, you can run the program by using the command:
$ python manage.py runserver
•	Open http://127.0.0.1:8000/ in a browser.
# Data Sources:
1.	Yelp Fusion, which is the data source for the table "Restaurants" in the database.
https://www.yelp.com/developers/documentation/v3/business_search 
Data was scraped from Yelp website using authentication key.
2.	GitHub page that provides a json format for country-state-cities database.
https://github.com/dr5hn/countries-states-cities-database
Format stored: SQL
Data Structure used: Tree Structure
Data was scraped from the huge JSON file and necessary data is stored in a Tree-structured SQL database, to access it when needed in Forms.
# Data Structure:
I used a generic Tree structure to store all the country, state, and city data. I have also loaded all the states and cities for the “United States” into a tree-structured SQL database for me to use in the web application. This can be seen in one of the pages where I have coded a dynamically populated Dropdown list for Country, State and Cities. 

# Interaction and Presentation:
The web application is designed using the Django Web Framework. The Webpages were designed using HTML, CSS, Bootstrap 5, and necessary JavaScript. The website is an Activities Recommendation system that will recommend the top-rated Places to visit in either the City you are currently logging in from or from a City of your choice from any State in the United States. If the user finds any place that interests him, he can click on the “More Info” button found on the respective Restaurant card and it will redirect him to the Yelp Page where the user can proceed. 
This web application also has a user management system, wherein a new user is prompted to Login using GitHub or Google Account or Create a new Account. 

![image](https://user-images.githubusercontent.com/81701847/206368385-ba68e036-e1d9-4eff-97ee-7a9e18359fbc.png) 

Once successfully logged in, the User will be redirected to the “Home Page” which looks as follows:
 
![image](https://user-images.githubusercontent.com/81701847/206368418-f89f046b-42a1-488a-88ab-203b6ba0c492.png)

As seen, the page will pick up your current location based on my IP address. In my example it shows Ann Arbor.
By clicking “Continue”, the page will move on to show Top Rated Places to visit in Ann Arbor as shown below:

![image](https://user-images.githubusercontent.com/81701847/206368447-b06c3147-ac44-4003-ab44-0253e88a1d9a.png)

By Clicking “Different Location”, it takes you to a form where you can choose the Country, State and City in which you want to search.

![image](https://user-images.githubusercontent.com/81701847/206368478-983e66e7-496a-4f49-bd43-404266e0ae5e.png)

By Clicking “Next” it will display the Top-Rated Places in Ault Field.

![image](https://user-images.githubusercontent.com/81701847/206368491-9f01c341-ffc6-4f35-a632-7616ede408fe.png)

Other than this, the User can also Edit his Profile data by Clicking on the “Profile” option in the nav bar top-right. The following web page will be displayed with options that you can change and update.
 
![image](https://user-images.githubusercontent.com/81701847/206368503-fc3d6a2e-3b2f-433a-9733-d23916ddadd7.png)

