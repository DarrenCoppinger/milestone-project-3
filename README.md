<img src="https://i.ibb.co/Y2vw7XC/Readme.jpg" alt="Karaokean Project Image" border="0" width="100%" >

# [Deployed Karaokean website here](https://karaokean.herokuapp.com/)

---

This website, [Karaokean](https://karaokean.herokuapp.com/), is an online catalogue of Karaoke track freely available on Youtube[YouTube](https://www.youtube.com/). It is a designed to be a website for parties where groups of friends can enjoy their favourite Karaoke numbers! Users can sign up to get their own free account and create their own personal playlist. Users can add songs to the catalogue as well as liking/disliking existing songs on the website. 

## Table of Contents
1. [**UX**](#ux)
    - [**Design Objectives**](#design-objectives)
    - [**User stories**](#user-tories)
    - [**Wireframe**](#wireframe)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)

---

## UX
This website was designed as a part of my Code Institute Full Stack Developement course, specifically the Data Centric Development module. The objective of this project was to design a website that allowed users to interact with data using CRUD (Create, Read, Update and Delete) operations. 

The website provides users with a location to collect and rate great karaoke tracks as well as putting together their own playlist for a Karaoke party. 

### Design Objectives
The following are the main design objectives for the project
#### Appropriate for Audience
The website must be appropriate for the audience. The audience for this website will be english speaking karaoke fans. The audience is likely a young technology savvy audience and will likely access the site on mobile devices. A mobile first approach was considered appropriate for this type of audience. Although the website will accommodate all visitors, its primary audience will be technology literate.

#### Content Relevence and accuracy
The content to the site must be relevent to the audience. To accomplise this the users of the sight can add karaoke songs to the catalogue. THe audiences can also edit the cataolgue and delete specific song entries. It is important to include a delete feature for songs in the catalogue as this is one of the requirements for the projects assessment. However, it does make the catalogue vunerable to being completely deleted, whether by accident or by a nefarious user.

#### Content Grouping
The website content is grouped into easily understood sections (Home, Catalogue page, Add Song page, Genres page, playlist page, login page)
#### Technology 
Appropiate technologies were used to design the website such as [Materialize](https://materializecss.com/) and the [Youtube iFrame API](https://developers.google.com/youtube/iframe_api_reference) to provide the user with a high quality experience.

### User stories

"As a user of this website, I would like to- _____________________"

- view the website from all device types (mobile, tablet or desktop)
- view the entire catalogue of available songs on the site (even while not logged in as a user)
- sort catalogue by newest entry, oldest entry, most liked song, most disliked song
- add a new song to the catalogue
- edit a song that already exist within the catalogue
- delete a song that exists within the catalogue
- like a song that exists within the catalogue
- dislike a song that exists within the catalogue
- check the lyrics of a song that exists within the catalogue
- create an user account for the website by registering
- be able to log into an existing user account
- be able to log out of an existing user account
- create a playlist of songs that a user wishes to play
- edit a playlist created by the user by delete unwanted songs
- play the playlist created by the users
- have a live upcoming song sidebar that allows users to see what song will be played next

A user who visits the website might follow one of the follow forms:
- I am interested to see what tracks are available on the website
- I find a karaoke songs on youtube that would like to add it to Karaoke so that the other users of the site can play and rate it.
- I am having a karaoke party and would like to use the site to generate a playlist of existing songs in the catalogue.


### Design

The style of the site is inspired by the asetetic of japanese karaoke bars (called Karaokeans). These places tend to have neon signs on the outside and have cyber punky interior with lots of lights brightly color lights and vibrant colors. To communicated this a vapourwave color scheme was chosen using pinks, blues and a small amounts of teal green. 

#### Framework
For this project I used the framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) to render the python code which is in place at the back-end of the website. I also used the framework [Materialize](https://materializecss.com/) as I wished to uses something other than bootstrap and I likes the clean modern look the framework. It's documentation was also concise and easy to read. [jQuery](https://code.jquery.com/jquery/) was also used to as I found it slightly simpler to used than basic JavaScript. 

#### Colors
The main colors used are as follows:

- ![#9C27B0](https://placehold.it/15/e487d8/e487d8) `#e487d8` (**light pink** - *primary color*)
- ![#79acfb](https://placehold.it/15/79acfb/79acfb) `#79acfb` (**light blu3** - *secondary color*)
- ![#4db6ac](https://placehold.it/15/4db6ac/4db6ac) `#79acfb` (**light blu3** - *tertiary color*)

#### Icons
- [Materialize Icons](https://materializecss.com/icons.html)
    - The built in materialize icons where used as they provide a wide array of attractive and useful icons and I found these to be sufficent for my project.

#### Typography
The fonts were chosen to give a japanese/eastern feel. A cursive font, East Sea Dokdo, was chosen for the headings which mimics the calligraphy japanese kanji. Another header font, Do Hyeon, was used to give 1980s retro-futuristic feel. All other text is in Googles sans-serif Robotico font giving information in a clean clear way. The each fonts were sourced from Google Fonts and links to them are provided below:
- [East Sea Dokdo](https://fonts.google.com/specimen/East+Sea+Dokdo)
- [Do Hyeon](https://fonts.google.com/specimen/Do+Hyeon)
- [Roboto](https://fonts.google.com/specimen/Roboto)

### Wireframe
- [Home](https://i.ibb.co/PxL7h23/Home.png)
- [Add Song](https://i.ibb.co/V9zCxHt/Add-Song.png)
- [Edit Song](https://i.ibb.co/8bpfRmV/Edit-Song.png)
- [Catalogue](https://i.ibb.co/X3kpZxv/Catalogue.png)
- [Genre](https://i.ibb.co/kGVr9n1/Genres.png)
- [Add Genre](https://i.ibb.co/x7JNqrx/Add-Genre.png)
- [Edit Genre](https://i.ibb.co/dGkhdSn/Edit-Genre.png)
- [Playlist Editor](https://i.ibb.co/7XHybqx/Playlist-list.png)
- [Playlist Player](https://i.ibb.co/L1wDFs4/Playlist.png)
- [Login](https://i.ibb.co/D5W147z/Login.png)
- [Register](https://i.ibb.co/Vw1RrVH/Register.png)

## Features

### Existing Features
#### All Pages
All pages includes a responsive navigation bar and title at the top of the page. The title and logo acts as a "Home" button. On medium and small screen size the navbar reduces to just the title and logo, with the pages buttons concealed in a sidebar accessable via a menu icon in the lefthand corner of the navbar. The navbar contains the Home, Catalogue, Add Song, Genre, Playlist buttonsmenu items and a login button. The login is included as a button to draw attention to it. If the user is logged into an account  the login button will change to a "Logout" button and the users username will appear beside the button highlighed in teal.

#### Home
The home page includes an "About" section with information about the website followed by two buttons connecting to the "Add Song" and "Catalogue" page. There is also a "Most Likes Songs" section which has a leaderbaord of the top five most liked songs in the catalogue followed by a button which likes to the full catalogue page.
#### Catalogue
The "Catalogue" page present all of the songs added to the database broken up with the use of pagination. Each pages displays 5 songs from the database. 

At the bottom of the page are a collection of pagination buttons which inlcude a previous and next chevron and a list of all the available pages of songs. On the first page the previous chevron is disabled and on the last page the next chevron is disabled thereby preventing the calling of a catalogue page that doesn't have any songs associated with it. Each of the page number buttons is clickable with the current page number highlighted in a outline box. 

At the top of the page is a sort box which is a dropdown menu box. There are 4 options of sorting to chose from: Most Likes, Most Disliked, Newest Song, Oldest Song. The default sort value is the "Most Liked" option.

Each song in the catalogue is displayed in the order that is specified. The video associated with the song is displayed on the left handside of the screen that are greater then 600px using the YouTube iFrame API with the information panel and buttons displayed on the right hand third of the viewport. For viewports less that 600px in width the display changes to the video container on top with the information panel and buttons below.  

The video is contained in a Materialize "video-container" class which allows it to change size responsively. Click the YouTube play logo will play the embedded video on the page. Each song video has YouTube controls active including clicking the song title to launch the song on Youtube, adding to a personal "Watch Later" list, and a share the video using the YouTube link. 

Each song in te catalogue also has an associated information panel on the rightwhich includes information on the specific songs and a number of buttons. The song title, year of release and artist are detailed at the top of the box. This is followed by text showing the current number of "Likes" and "Dislikes" that the songs has. 

Below the song information panel is a number of number of buttons including: "Check Lyrics", "Add to Playlist", "Edit", "Delete", "Like" and "Dislike". 
- When clicked the "Check Lyrics" button will launch a new page with the songs lyrics submitted when the song document was created. 
- Pressing the "Add Playlist" button will add a song to a logged in users playlist and flash a Materialize Toast message confirming the submission. If the users is not logged in an Toast message with appear telling the user to register or log into their account.
- Clicking the "Edit" button will launch the Edit Song page where the information from the songs document is displayed. The user can alter this information if a piece of it is incorrect. 
- Clicking the "Delete" button will permenantly remove the song document from the database and the catalogue.
- Clicking the "Like" or "Dislike" buttons will increase the number of likes or dislikes that a song has and a toast message will confirm that this has been completed. However, the number displayed does not update until the page is reloaded. This issue is due to time constaints working on the project and a feature left to implement in the next development sprint will be to use ajax to allow the numbers to increase on the information panel without the page reloading.

#### Add Song / Edit Song Page / Add Genre / Edit Genre
The Add Song/ Edit Song pages include input fields for all of the required fields in the song document in the database. The Much of this work was inspired by the validation done on this previous code institute [project](https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3).

Each of field must be populated with it data for the form to be submitted. The "Song Name" and "Artist Name" fields must be text below a stated character length which appears underneath the input field. The "Year" field must be 4 numbers long with the first number being either 1 or 2. 

The "Genre" field is a drop down menu from which the use must select an existing option or select the final entry of the list which is "Add a new genre".

The "Lyric Link" field must be populated with a url.

The "YouTube Link" field must have a youtube link for a video placed in it to work. This is achieved by check that the link follows the YouTube format. This solution was inspired by the article found [here](https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box) on Stackoverflow.

If the information does not satisty the validation checks the form will not submit and each field that is not validate will be underlines with a redline and an error message will be displayed underneath the field. 

If the data entered into the input field is the correct type (text, number, url or youtube link) 
#### Genre 

The Genre page lists all of the genres added to the database by the website users. Each genre name entry can be editted. If and entry is edit it must the name must still be a text entry of no more than 30 character. However, as each song is associated with a genre, through the genre Object_id it is not possible to completely delete a genre, as this might result in a number of songs having no genre. It is possible however, to change the genre of any song through the Edit song page. 

At the bottom of the Genre page is a button which a user can click to add a new Genre to the list. THis is the same page that is accessible though the dropdown list on the Add Song and Edit Song pages.

#### Add Genre / Edit Genre
Add Genre/ Edit Genre are similar forms are similar to the Add Song / Edit Song pages already discussed above. They require for validation one entry which is of the text type in the input field. There is also a characted limit of 30 put on the field. 

#### Playlist
The playlist pages has two parts: the Playlist Editor page and the Playlist Player page. To access either of these pages a user must be logged into an account. 

##### Playlist Editor
If they visit the Playlist page without being logged in they will be greeted by a message asking them to register for an account by clicking the register button or logging in by clicking the Login button both of which are presented on the page.

If the users is logged into an account but has no songs added to the playlist and visits the playlist page they will be greeted by a message that say they don't have any songs on their playlist and directs them to the Catalogue page and presents a button called Catalogue to follow.

If the user is logged in to an account and has added songs to their playlist the user will be presented with the Playlist Editor page. The user see a list of the songs they have picked and a button on the right of each song name allows the user to remove the song from their playlist. If the user is finished edit their playlist they can click the "Play Playlist" Button at the bottom of the page to initiate the playlist.

##### Playlist Player
The Playlist Player page has two elements the video-container on the lefthand 2 thirds of the page and in the final third a list of the songs they have picked. The song on the top of the list that is currently playing will also have the text "Currently playing" in red next to it.

The video will autoplay on the page loading as each song in the playlist will play through until the end is reached. At the bottom of the page is a "Skip" button which allows the user to skip to the next song at any stage during the currently playing song. When the end of the playlist is reached the user will see a tost message telling them that the end of the playlist has beeen reached. After a delay of 4 seconds for the toast to be read the page will auto redirect back to the Playlist Editor page.

#### Login 
The login page is access via a button on teh navbar of the site. Clicking this brings the user to a typical user login form screen with a submit button labelled "Login". 
- If the users does not have an account but tries to login with a made up username they will receive a flash message saying the "Username doesn't exist".
- If the users has already register for an account and has input a username that already exists in the database then they will receive the flash message "Password was incorrect".
- If the user enters both an existing username and a correct password they will be redirected to the home page of the site and shown a flash message saying "Kon'nichiwa *their username*".
- If the user doesn't have have an account already they can click the "Sign up Here!" button at the bottom of the page to be directed to the registeration page.

Also note that if the user is logged into an account  the "login" button in the navbar will change to a "Logout" button and the users username will appear beside the button highlighed in teal. This is the same in the case of the side nav bar for mobile devices.
If the user clicks the Logout button the button will return to "Login" the highlighted username will disappear and they will be redirect to the home page were they will receive the flash message "Sayōnara *username*".

#### Registeration
The registration page has the same two inputs as the login with username and password fields. - If the user enters an existing username from the data (with a password) a flash message will appear saying "*username* already exists"
- If the users enters in a new unique username (along with a password) they will be redirected to the home page of the site and see the flash message "Welcome to Karaokean *username*".

### Features left to Implement
- Live updating of the like and dislike numbers on the catalogue page
- Sorting of catalogue by genre
- pagination for large numbers of pages. 
## Technologies Used
### Front-End Technologies
- [HTML](https://www.w3schools.com/html/html5_intro.asp) - Employed for markup text. 
- [CSS](https://www.w3schools.com/css/) - Used for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used for JavaScript functionality.
- [Materialize 1.0.0](https://materializecss.com/) - Used for design framework.

### Back-End Technologies
- **Python**
    - [Python 3.7.6](https://www.python.org/) - Used as the programming language at the back-end.
    - [PyMongo 3.10.1](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

- **Flask**
    - [Flask 1.1.1](https://flask.palletsprojects.com/en/1.1.x/) - Used as mirocframework. 
    - [Jinja 2.10](https://jinja.palletsprojects.com/en/2.11.x/) - The templating language with Flask. 
    - [Werkzeug 1.0.0](https://werkzeug.palletsprojects.com/en/1.0.x/) - Used for password hashing and checking. 

- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for hosting the deployed website.

## Testing
### Code Validators
The follow validators were used to check the code developed from this project:
- 
- 

#### HTML
 [WC3 Markup Validator](https://validator.w3.org/) was used to validate the HTML code. However, unfortunately the validator is not able to recognise the Jinja templating sentax so some errors were recorded. All code other than the jinja sentax was successfully validated.

#### CSS
[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code. The CSS successfully pass the check with no errors.


This website was tested on multiple browsers. They included:
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)

### User Stories Testing
#### I am interested to see what tracks are available on the website
1. User loads the  app and is directed to the index.html page. The users sees About Karaokean section of the page and reads the instructions. They also see the table beside this section which list the songs with the most "likes" in the catalogue. 
2. The user choses to see the full list of liked videos by clicking the "See Full catalogue" button at the bottom of the "Most Liked Songs" section which redirects the user to the Catalogue page. The default sort setting for the catalogue page is to sort likes in descending order.
3. The users scrolls down the page and at the bottom clicks the next cheveron to go the the second 5 entries in this sorting setting. 
4. The user see as song that they think they might enjoy. They click the play button in the centre of the video to play it. They see that the name of the song in the video is mispelled so they click the edit button which directs them to the edit page.
5. The users changes the typo in the "song name" input field, the color of the boxes underline changes reflecting that it is a valid entry. The users then saves the edits by clicking the "Save Edits" on the bottom left of the screen.
6. The user is returned to same catalogue screen they left when they clicked the edit button (same sorting order and same page).
7. The user sees a song they like and click the like button beside it. They see another song which they dislike and click the dislike button beside that. Both clicks reult in a toast message popping up on the right hand side of their screen confirming the like or dislike of the particular song.
8. 
#### A user user wishes to an a karaoke song, found on youtube, to the catalogue so that the other users of the site can play and rate it.
1. The user finds a karaoke song on YouTube and copies the link.
2. The user loads the  app and is directed to the index.html page. The users sees About Karaokean section of the page and reads the instructions.
3. User Clicks the "Add Song" button at the bottom of the About section and is redirected to the Add Song page (addtrack.html).
4. The user paste in the youtube link and add in the other required information but forgets to choose a genre for the song. On clicking the "Add Track" button the field and it's underline go red and an error message "Please select a genre e.g. Rock" is displayed. All the other fields underline turn green and the display a success message.
5. The user clicks the dropdown trigger icon and a list of all the currently record genres is displayed. They choose their genre of the son then press submit.

#### A user wants to use the site to generate a playlist of existing songs in the catalogue.
1. User loads the  app and is directed to the index.html page. The users sees About Karaokean section of the page and reads the instructions.
2. The user then clicks the "See Full Catalogue" button on the page or the Catalogue menu item in the navbar.
3. On the Catalogue page the user see a song that they like that they wish to add to a playlist so they click the "add to playlist button". However, they are not logged into an account so they receive the toast message "To add song to your Playlist either register or login to your account!".
4. The user clicks the "Login" button and are brought to the login page. They do not have an account so they click the "Sign Up here" button and are redirected to the registeration page. 
5. The user inputs a username and a password and is redirected to the home page of the site and see the flash message "Welcome to Karaokean *username*". The username also appears in a container on the right of the navbar beside the "Logout" (previously "Login" button). 
6. The user then can click the "Catalogue" button again to go to the Catalogue page. They can then click the "Add to Playlist" button to add a song to the playlist. This will generate a toast message of "Song added to your Playlist!".
7. The user can go though the full catalogue by clicking the pagination buttons on the bottom of the catalogue page or changing the sorting order by clicking the sort button at the top of the page with the dropdown trigger give four different sorting options (# Likes, # Dislikes, Newest, Oldest)

### Manual testing of elements and functionality on each page
#### Home
#### Catalogue
#### Add Song 
#### Genre 
#### Playlist

#### Known Issues
If a users partially inputs the data for a song into the input field on the "Add Track" page but doesn't see their desired genre in the drop down list their next step would be to click the Add new genre option at the botttom of the list. This will bring them to the "Add Genre" page. However, when they return to the "Add Track" page they will have lost the data that they had enter before clicking this option on the list. 

## Deployment

### Local Deployment
To run this project locally on any system the following will need to be installed

- [Python3](https://www.python.org/downloads/) to run the app.py files and the application
- [PIP](https://pip.pypa.io/en/stable/)
- An IDE such as [Gitpod](https://gitpod.io/) or [Microsoft Visual Studio](https://code.visualstudio.com/)
- [GIT](https://www.atlassian.com/git/tutorials/install-git)
- [MongoDB](https://www.mongodb.com/)

To clone or copy this project from GitHub follow these steps:
1. Follow this link to the [project repository on GitHub] (https://github.com/DarrenCoppinger/milestone-project-3.git)
2. On the left side of the page click the green button labelled "Clone or Download"
3. In the pop up that appears labe;led "Clone with HTTPs" section copy the URL
4. In your local IDE open Git Bash
5. Change the working directory to the to the location for the cloned directory to be stored.
6. Type "git clone" into the GIT CLI terminal and then paste in the URL copied from GitHub in step 3 (i.e. git clone https://github.com/DarrenCoppinger/milestone-project-3.git )
7. Hit enter and create your local drive.
8. Install the necessary requirements from the requirements.txt file using the command `pip3 install -r requirements.txt`
9. Generated a env.py file where you will store your MONGO_URI and SERCRET_KEY environmental variables. 
10. Set the SERCRET_KEY to your preferred value. 
11. Sign up for [MongoDB](https://www.mongodb.com) and make a database called **Karaokean**. The app will uses the following *Collections* in that database with the following titles and fields (fields will be generated by app):

**genre**
```
    _id: <ObjectId>
    name: <string>
```
**tracks**
```
    _id: <ObjectId>
    name: <string>
    artist: <string>
    year: <int32>
    genre: <string>
    lyrics: <string>
    video: <string>
    likes: <int32>
    dislikes: <int32>
```
**users**
```
    _id: <ObjectId>
    name: <string>
    password: <string>
    playlist (array)
```

10. Go to your created cluster in MongoDB and click the connect button, click "Connect your application". Then copy the connection string and set it equal to MONGO_URI in the env.py file. The connection string the will be of the form: 
```
mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority
```
11. Run the application by typing the follow command into the CLI:
    - python3 app.py


### Remote Deployment on Heroku

## Credits
### Media
Images used in this site were used with the permission of [Elora Pautrat](https://www.elorapautrat.com/).

### Content

### Acknowledgements
- [Antonio Rodriguez](https://github.com/AkaAnto)
    - My Code Institute mentor.
- [Tim Nelson](https://github.com/TravelTimN/)
    - Code Institute tutor who helped me with the jQuery and JavaScript code required for this project.

#### Disclaimer
This Website was produced for educational purposes only.