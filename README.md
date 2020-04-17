# Karaokean - Milestone 3 Project

![Karaokean Project Image](https://i.ibb.co/Y2vw7XC/Readme.jpg)

## [Deployed Karaokean website here](https://karaokean.herokuapp.com/)

---

## Introduction
This website, [Karaokean](https://karaokean.herokuapp.com/), is an online catalogue of Karaoke track freely available on [YouTube](https://www.youtube.com/). It is a designed to be a website for parties where groups of friends can enjoy their favourite Karaoke numbers! Users can sign up to get their  free account and create their own personal playlist. Users can add songs to the catalogue as well as liking/disliking existing songs on the website. 

## Table of Contents
0. [**Introduction**](#introduction)
1. [**UX**](#ux)
    - [**Design Objectives**](#design-objectives)
        - [**Appropriate for Audience**](#appropriate-for-audience)
        - [**Content Relavence and Accuracy**](#content-relevence-and-accuracy)
        - [**Content Grouping**](#content-grouping)
        - [**Technology**](#technology)
    - [**User stories**](#user-tories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Colors**](#colors)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframe**](#wireframe)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
        - [**All Pages**](#all-pages)
        - [**Home**](#home)
        - [**Catalogue**](#catalogue)
        - [**Add Track / Edit Track**](#add-track/-edit-track)
        - [**Genre**](#genre)
        - [**Add Genre / Edit Genre**](#add-genre/-edit-genre)
        - [**Playlist**](#playlist)
            - [**Playlist Editor**](#playlist-editor)
            - [**Playlist Player**](#playlist-player)
        - [**Login**](#login)
        - [**Registration**](#registration)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Technologies Used**](#technologies-used)
    - [**Frontend Technologies**](#frontend-technologies)
    - [**Backend Technologies**](#Backend-technologies)

3. [**Testing**](#testing)
    - [**Code Validators**](#code-validators)
        - [**WC3 Markup Validator**](#frontend-technologies)
        - [**W3C Jigsaw CSS Validator**](#w3c-jigsaw-css-validator)
    - [**Browers Testing**](#browers-testing)
    - [**User Stories Testing**](#user-stories0-testing)
        - [**User Story 1**](#user-story-1)
        - [**User Story 2**](#user-story-3)
        - [**User Story 3**](#user-story-3)
    - [**Manual testing**](#manual-testing)
        - [**Home**](#home)
        - [**Catalogue**](#catalogue)
        - [**Add Track**](#add-track )
        - [**Genre**](#genre)
        - [**Playlist**](#playlist)
    - [**Known Issues**](#known-issues)

3. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment on Heroku**](#remote-deployment-on-heroku)
4. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)
    - [**Disclaimer**](#isclaimer)


---

## UX
This website was designed as a part of my Code Institute Full Stack Development course, specifically the Data Centric Development module. The objective of this project was to design a website that allowed users to interact with data using CRUD (Create, Read, Update and Delete) operations. 

The website provides users with a location to collect and rate great karaoke tracks as well as putting together their own playlist for a Karaoke party. 

### Design Objectives
The following are the main design objectives for the project:

#### Deign a Application Appropriate for Audience
The website must be appropriate for the audience. The audience for this website will be English speaking, technology savvy and will likely access the site on mobile devices. Although the website will accommodate all visitors, its primary audience will be technology literate. THe site will perform well on a large screen sizes but also has the ability to perform on mobile devices.

#### Content Relevance and Accuracy
The content to the site must be relevant to the audience. To accomplise this, the users of the website have the ability to add their own choice of karaoke songs to the catalogue. The users can also edit the catalogue and delete specific song entries. It is essential to include a delete feature for songs in the catalogue as this is one of the requirements for the project's assessment. However, it does make the catalogue vulnerable to being completely deleted, whether by accident or by a nefarious user.

#### Content Grouping
The website content is grouped into easily understood sections (Home, Catalogue page, Add Track page, Genres page, playlist page, login page). Additionally, the catalogue page sorts the songs in the catalogue by most "Likes", most "Dislikes", "Newest" by date added, and Oldest by date added. 

#### Technology 
Appropriate technologies were used to design the website such as [Materialize](https://materializecss.com/) and the [Youtube iFrame API](https://developers.google.com/youtube/iframe_api_reference) to provide the user with a high-quality experience. 

[MongoDB](https://www.mongodb.com/) was used to manage the date for the website. A schematic for the database model used for this project are shown below:

![database model](https://i.ibb.co/9Zwb4Zz/Database-Model.jpg)

As this database model links data from different collections (as shown above in schematic) a relational (SQL) database may have been used for this project. However, I wished to use this project to use a non-relational(NoSQL) database, such as MongoDB, in a milestone project. I will have the opportunity to use a relational database in a milestone project in the Fullstack Development Module.

### User stories
A user who visits the website might follow one of these forms:
- A user wants to see what tracks are available on the website
- A user wants to add a karaoke song, found on YouTube, to the catalogue so that the other users of the site can play and rate it.
- A user wants to use the site to generate a playlist of existing songs in the catalogue.


Additionally, the following requirements should be met by the website:

"As a user of this website, I would like to- _____________________"

- view the website from all device types (mobile, tablet or desktop)
- view the entire catalogue of available songs on the site (even while not logged in as a user)
- sort catalogue by newest entry, oldest entry, most liked song, most disliked song
- add a new song to the catalogue
- edit a song that already exists within the catalogue
- delete a song that exists within the catalogue
- like a song that exists within the catalogue
- dislike a song that exists within the catalogue
- check the lyrics of a song that exists within the catalogue
- create an user account for the website by registering
- be able to log in to an existing user account
- be able to log out of an existing user account
- create a playlist of songs that a user wishes to play
- edit a playlist created by the user by deleting unwanted songs
- play the playlist created by the users
- have a live upcoming song sidebar that allows me to see what song will be played next

### Design
The style of the site is inspired by the aesthetic of Japanese karaoke bars (called Karaokeans). These places tend to have neon signs on the outside and have cyberpunk inspired interior with lots of brightly color lights and vibrant colors. To communicated this a [vapourwave](https://en.wikipedia.org/wiki/Vaporwave) color scheme was chosen using pinks, blues and a small amounts of teal green. 

#### Framework
For this project, I used the framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) to render the python code which is in place at the backend of the website. I also used the framework [Materialize](https://materializecss.com/) as I wished to use an alternative to bootstrap and I like the clean modern look of the framework. Its documentation was also concise and easy to read. [jQuery](https://code.jquery.com/jquery/) was also used to as I found it more straight forward to used than basic JavaScript. 

#### Colors
The main colors used are as follows:

- ![#9C27B0](https://placehold.it/15/e487d8/e487d8) `#e487d8` (**light pink** - *primary color*)
- ![#79acfb](https://placehold.it/15/79acfb/79acfb) `#79acfb` (**light blu3** - *secondary color*)
- ![#4db6ac](https://placehold.it/15/4db6ac/4db6ac) `#79acfb` (**light blu3** - *tertiary color*)

#### Icons
- [Materialize Icons](https://materializecss.com/icons.html)
    - The built in materialize icons where used as they provide a wide array of attractive and useful icons and I found these to be sufficient for my project.

#### Typography
The fonts were chosen to evoke a jJapanese aesthetic. A cursive font, East Sea Dokdo, was chosen for the headings which mimic the calligraphy japanese kanji. Another header font, Do Hyeon, was used to give 1980s Japanese video game feel. All other text is in Google's sans-serif Robotico font providing information in a clean, clear way. The each fonts were sourced from Google Fonts and links to them are provided below:
- [East Sea Dokdo](https://fonts.google.com/specimen/East+Sea+Dokdo)
- [Do Hyeon](https://fonts.google.com/specimen/Do+Hyeon)
- [Roboto](https://fonts.google.com/specimen/Roboto)

### Wireframe
Wireframes for both the desktop and mobile versions of the website were produced. They are include below:

#### Desktop Wireframes
- [Home](https://i.ibb.co/LSw1K0d/Home.png)
- [Add Track](https://i.ibb.co/rx1xzCK/Add-Song.png)
- [Edit Track](https://i.ibb.co/5v8mWKy/Edit-Song.png)
- [Catalogue](https://i.ibb.co/HL8S3pC/Catalogue.png)
- [Genre](https://i.ibb.co/B4fS0fS/Genres.png)
- [Add Genre](https://i.ibb.co/HP5QrV8/Add-Genre.png)
- [Edit Genre](https://i.ibb.co/60RRTJw/Edit-Genre.png)
- [Playlist Editor](https://i.ibb.co/02tBHnJ/Playlist-Editor.png)
- [Playlist Player](https://i.ibb.co/ZYBdJ3D/Playlist-Player.png)
- [Login](https://i.ibb.co/PcsFkS1/Login.png)
- [Register](https://i.ibb.co/GMSLpXJ/Register.png)

#### Mobile Wireframes
- [Home - mobile](https://i.ibb.co/7QJFcJB/Home-mobile.png)
- [Add Track - mobile](https://i.ibb.co/566NYPx/Add-Song-mobile.png)
- [Edit Track - mobile](https://i.ibb.co/hYPJPMP/Edit-Song-mobile.png)
- [Catalogue - mobile](https://i.ibb.co/WnvKMzZ/Catalogue-mobile.png)
- [Genre - mobile](https://i.ibb.co/7Rg8ZNG/Genre-mobile.png)
- [Add Genre - mobile](https://i.ibb.co/Kr2dMHj/Add-Genre-mobile.png)
- [Edit Genre - mobile](https://i.ibb.co/1Zn05Zt/Edit-Genre-mobile.png)
- [Playlist Editor - mobile](https://i.ibb.co/ZGBDY6j/Playlist-Editor-mobile.png)
- [Playlist Player - mobile](https://i.ibb.co/ZX594Ry/Playlist-Player-mobile.png)
- [Login - mobile](https://i.ibb.co/6DKdgxs/Login-mobile.png)
- [Register - mobile](https://i.ibb.co/GPdP2kC/Register-mobile.png)

## Features
Major features to be developed and deployed on this website are summarized in the following table and graph. In the below opportunites analysis, the viability/feasibility is lower than the importance total. Therefore, all the features on this list will not be implemented. The “Sort by Genre” feature was left for a later development sprint as a result.

| Opportunities | Importance | Viability/feasibility | Difficulty |
|:---|:---:|:---:|:---:|
| Catalogue page to display all songs with pagination | 5 | 4 | 4 |
| General sorting for songs on catalogue page | 5 | 3 | 2 | 
| User Registration and Login | 4 | 5 | 3 | 
| Add/ Edit songs page | 4 | 4 | 3 | 
| Playlist Player and upcoming songs list  | 4 | 3 | 4 | 
| Playlist editor  | 3 | 3 | 3 | 
| Genre editor | 2 | 3 | 5 | 
| Sort by Genre | 2 | 2 | 5 | 
| **Total** | **29** | **27** |  | 
 
![feasibility-viability analysis](https://i.ibb.co/G2jcJ74/viability-feasibility.jpg)

### Existing Features
#### All Pages
All pages include a responsive navigation bar and title at the top of the page. The title and logo act as a "Home" button. On medium and small screen size the navbar reduces to just the title and logo, with the page's buttons concealed in a sidebar accessible via a menu icon in the left-hand corner of the navbar. The navbar contains the Home, Catalogue, Add Track, Genre, Playlist buttons menu items and a login button. The login is included as a button to draw attention to it. If the user is logged into an account  the login button will change to a "Logout" button and the user's username will appear beside the button highlighed in teal.

#### Home
The home page includes an "About" section with information about the website followed by two buttons connecting to the "Add Track" and "Catalogue" page. There is also a "Most Likes Songs" section which has a leaderbaord of the top five most liked songs in the catalogue followed by a button which links to the full catalogue page.

#### Catalogue
The "Catalogue" page presents all of the songs added to the database broken up with the use of pagination. Each pages displays five songs from the database. 

At the bottom of the page are a collection of pagination buttons. These include previous and next chevron buttons and a list of all the available catalogue pages. On the first page the previous chevron is disabled, and on the last page the next chevron is disabled thereby preventing the calling of a catalogue page that doesn't have any songs associated with it. Each of the page number buttons is clickable with the current page number highlighted in an outline box. 

At the top of the page is a sort box which is a drop-down menu box. There are four options of sorting to chose from: Most Likes, Most Disliked, Newest Song, Oldest Song. The default sort value is the "Most Liked" option.

Each song in the catalogue is displayed in the order that is specified. The video associated with the song is displayed on the left of the screen that are greater than 600px using the YouTube iFrame API. An information panel and buttons are displayed on the right-hand third of the viewport. For viewports less than 600px, the display changes to the video container on top with the information panel and buttons below.  

The video is contained in a Materialize "video-container" class which allows it to change size responsively. Click the YouTube play logo will play the embedded video on the page. Each song video has YouTube controls active including clicking the song title to launch the song on YouTube, adding to a personal "Watch Later" list, and a share the video using the YouTube link. 

Each song in the catalogue also has an associated information panel on the rightwhich includes information on the specific songs and a number of buttons. The song title, year of release and artist name are detailed at the top of the box. This is followed by text showing the current number of "Likes" and "Dislikes" that the songs has. 

Below the song information panel is a number of buttons including: "Check Lyrics", "Add to Playlist", "Edit", "Delete", "Like" and "Dislike". 
- When clicked the "Check Lyrics" button will launch a new page with the song's lyrics submitted when the song document was created. 
- Pressing the "Add Playlist" button will add a song to a logged-in users playlist and flash a Materialize Toast message confirming the submission. If the users is not logged in an Toast message will appear telling the user to register or login to their account.
- Clicking the "Edit" button will launch the Edit Song page where the information from the songs document is displayed. The user can alter this information if a piece of it is incorrect. 
- Clicking the "Delete" button will permanently remove the song document from the database and the catalogue.
- Clicking the "Like" or "Dislike" buttons will increase the number of likes or dislikes that a song has and a toast message will confirm that this has been completed. However, the number displayed does not update until the page is reloaded. This issue is due to time constraints working on the project and a feature left to implement in the next development sprint will be to use ajax to allow the numbers to increase on the information panel without the page reloading.

#### Add Track / Edit Track
The Add Track/ Edit Track pages include input fields for all the required fields in the song document in the database. Much of this work was inspired by the validation done on this previous code institute [project](https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3).

Each field must be populated with it data for the form to be submitted. The "Song Name" and "Artist Name" fields must be text below a stated character length which appears underneath the input field. The "Year" field must be 4 numbers along with the first number being either 1 or 2. 

The "Genre" field is a drop-down menu from which the user must select an existing option or select the final entry of the list which is "Add a new genre". Selecting the "Add a new Genre" option will launch the "Add New Genre" page. This solution is again from a previous Code Institute [student project](https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3). 

The "Lyric Link" field must be populated with a URL.

The "YouTube Link" field must have a YouTube link for a video placed in it to work. This is achieved by check that the link follows the YouTube format. This solution was inspired by the article found [here](https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box) on Stackoverflow.

If the information does not satisfy the validation checks the form will not submit, and each field that is not validate will be underlines with a redline and an error message will appear underneath the field. 

If the data entered into the input field is the correct type (text, number, URL or YouTube link) 

#### Genre 
The Genre page lists all the genres added to the database by the website users. Each genre name entry can be edited. If an entry is edited, it must still be a text entry of between 1 and 30 character. However, as each song is associated with a genre, through the genre Object_id, it is not possible to completely delete a genre, as this might result in a number of songs having no genre. It is possible however, to change the genre of any song through the Edit song page. 

At the bottom of the Genre page is a "Add Genre" button which a user can click to add a new Genre to the list. THis is the same page that is accessible though the drop-down list on the Add Track and Edit Song pages.

#### Add Genre / Edit Genre
Add Genre/ Edit Genre are similar forms are similar to the Add Track / Edit Song pages already discussed above. They require validation for one required field. This field has the required type of text and there is also a characted limit of 30 put on the field. 

#### Playlist
The playlist page has two parts: the Playlist Editor page and the Playlist Player page. The user must be logged into an account to fully access either of these pages, otherwise a informational message is display (this is discussed in detail below). The menu button for "Playlist" will launch the Playlist Editor page. The Playlist Player page is only accessible the the "Play Playlist" button at the bottom of the Playlist Editor page. 

##### Playlist Editor
If they visit the Playlist page without being logged in they will be greeted by a message asking them to register for an account by clicking the register button or logging in by clicking the Login button both of which are presented on the page.

If the users is logged into an account, has no songs added to their playlist and visits the playlist page they will be greeted by a information message. This message says "There are no songs in your playlist!" and directs the user to the Catalogue page. Below the messages a button called "Catalogue" is available for the user to click.

If the user is logged in to an account and has added songs to their playlist, the user will be presented with the Playlist Editor page. The users a list of the songs they have picked and a button on the right of each song name allows the user to remove the song from their playlist. If the user is finished editing their playlist they can click the "Play Playlist" Button at the bottom of the page to initiate the playlist.

If the user added a track to their playlist and then deletes that track from the catalogue this could cause an error. This is becase it asks the application to play a track that no longer exists in the database. To defend against this the application performs a check at the backend when the users launches to the Playlist Editor page. If the track exists in the database it is displayed. If the track doesn't exist in Catalogue stored in the database (has been deleted) the track is deleted from the playlist by calling the view function "playlist_delete".

##### Playlist Player
The Playlist Player page has two elements the video-container on the lefthand 2 thirds of the page and in the final third a list of the songs they have picked. The song on the top of the list that is currently playing will also have the text "Currently playing" in red next to it.

The video will autoplay on the page loading as each song in the playlist will play through until the end is reached. When the video player is ready to autoplay the border around the video will turn pink and the video will autoplay. At the bottom of the page is a "Skip" button which allows the user to skip to the next song at any stage during the currently playing song. When the end of the playlist is reached the user will see a tost message telling them that the end of the playlist has beeen reached. After a delay of 4 seconds for the toast to be read the page will auto-redirect back to the Playlist Editor page.

#### Login 
The login page is accessed via a button on the navbar or the sidenav on mobile devices. Clicking this brings the user to a typical user login form screen with a submit button labelled "Login". 
- If the users has not registered for an account but tries to login by inputing an unregistered username and password they will receive a flash message saying the "Username doesn't exist".
- If the user has previously registered for an account and input a username that already exists in the database then they will receive the flash message "Password was incorrect".
- If the user enters both an existing username and a correct password they will be redirected to the home page of the site and shown a flash message saying "Kon'nichiwa *their username*".
- If the user doesn't have an account already they can click the "Sign up Here!" button at the bottom of the page to be directed to the registration page.

Also, note that if the user is logged into an account the "Login" button in the navbar will change to a "Logout" button and the user's username will appear beside the button highlighed in a teal box. This is the same in the case of the side nav bar for mobile devices.
If the user clicks the Logout button the button will return to "Login" and the highlighted username will disappear. They users will be redirect to the home page where they will see the flash message "Sayōnara *username*".

#### Registration
The registration page has the same two inputs as the login with username and password fields. - If the user enters an existing username from the data (with a password) a flash message will appear saying "*username* already exists"
- If the users enters in a new unique username (along with a password) they will be redirected to the home page of the site and see the flash message "Welcome to Karaokean *username*".

### Features Left to Implement
During planning this project it was decided that the feature of sorting songs by genre on the catalogue page would be left for a future development sprint. During development and testing of this application, additional features where imagined to be added in a later date. These addtional features are as follows: 
- Sorting of songs in the catalogue by genre
- Pagination of catalogue for large numbers of pages, where all pages are not displayed as buttons
- Live updating of the like and dislike numbers on the catalogue page (currently page must be reloaded for numbers to update)

## Technologies Used
### Frontend Technologies
- [HTML](https://www.w3schools.com/html/html5_intro.asp) - Employed for markup text. 
- [CSS](https://www.w3schools.com/css/) - Used for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used for JavaScript functionality.
- [Materialize 1.0.0](https://materializecss.com/) - Used for the design framework.

### Back-End Technologies
**Python**
    - [Python 3.7.6](https://www.python.org/) - Used as the programming language at the back-end.
    - [PyMongo 3.10.1](https://pymongo.readthedocs.io/en/stable/) - Used as the Python API for MongoDB.

**Flask**
    - [Flask 1.1.1](https://flask.palletsprojects.com/en/1.1.x/) - Used as mirocframework. 
    - [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/) - Flask-PyMongo bridges Flask and PyMongo and provides some convenience helpers.
    - [Jinja 2.10](https://jinja.palletsprojects.com/en/2.11.x/) - The templating language with Flask. 
    - [Werkzeug 1.0.0](https://werkzeug.palletsprojects.com/en/1.0.x/) - Used for password hashing and checking. 

**MongoDB**
    - [MongoDB](https://www.mongodb.com/) - MongoDB is the database used to manage the data for this website. It is a cross-platform document-oriented database program.

**Heroku**
    - [Heroku](https://www.heroku.com) - Used for hosting the deployed website.

## Testing
### Code Validators

The follow validators were used to check the code developed from this project:
- [WC3 Markup Validator](https://validator.w3.org/)
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/)

#### WC3 Markup Validator
 [WC3 Markup Validator](https://validator.w3.org/) was used to validate the HTML code. However, the validator is not able to recognise the Jinja templating syntax so some errors were recorded. All code other than the jinja syntax was successfully validated.

#### W3C Jigsaw CSS Validator
[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code. The CSS successfully passed this check with no errors.

### Browers Testing
This website was tested on multiple browsers. They included:
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)

### User Stories Testing

#### A user wants to see what tracks are available on the website

1. The User loads the  app and is directed to the index.html page. The user sees About Karaokean section of the page and reads the instructions. They also see the table beside this section which list the songs with the most "likes" in the catalogue. 
2. The user chooses to see the full list of liked videos by clicking the "See Full catalogue" button at the bottom of the "Most Liked Songs" section which redirects the user to the Catalogue page. The default sort setting for the catalogue page is to sort likes in descending order.
3. The users scrolls down the page and at the bottom clicks the next chevron to go the the second five entries in this sorting setting. 
4. The user sees a song that they think they might enjoy. They click the play button in the centre of the video to play it. They notice that the name of the song in the video is misspelt so they click the edit button which directs them to the edit page.
5. The user changes the typo in the "song name" input field, the color of the boxes underline changes reflecting that it is a valid entry. The users then saves the edits by clicking the "Save Edits" on the bottom left of the screen.
6. The user is returned to same catalogue screen they left when they clicked the edit button (same sorting order and same page).
7. The user sees a song they like and clicks the "Like" button associated with it. They see another song which they dislike and click the "Dislike" button beside that. Both clicks result in a toast message popping up on the right side of their screen confirming the like or dislike of the particular song.

#### A user wants to add a karaoke song, found on YouTube, to the catalogue so that the other users of the site can play and rate it.

1. The user finds a karaoke song on YouTube and copies the link.
2. The user loads the  app and is directed to the index.html page. The users sees About Karaokean section of the page and reads the instructions.
3. User clicks the "Add Track" button at the bottom of the About section and is redirected to the Add Track page (addtrack.html).
4. The user pastes in the YouTube link and add in the other required information but forgets to choose a genre for the song. On clicking the "Add Track" button the field and it's underline go red and an error message "Please select a genre e.g. Rock" is displayed. The underline of the other fields turn green and display a success message e.g "Valid Entry".
5. The user clicks the drop-down trigger icon and a list of all the currently record genres is displayed. They choose their genre of the son then press submit.

#### A user wants to use the site to generate a playlist of existing songs in the catalogue.
1.The user loads the  app and is directed to the index.html page. The user sees the "About Karaokean" section of the page and reads the instructions.
2. The user then clicks the "See Full Catalogue" button on the page or the Catalogue menu item in the navbar.
3. On the Catalogue page, the user sees a song that they like that they wish to add to a playlist so they click the "add to playlist button". However, they are not logged into an account so they receive the toast message "To add song to your Playlist either register or login to your account!".
4. The user clicks the "Login" button and are brought to the login page. They do not have an account so they click the "Sign Up here" button and are redirected to the registration page. 
5. The user inputs a username and a password and is redirected to the home page of the site and see the flash message "Welcome to Karaokean *username*". The username also appears in a container on the right of the navbar beside the "Logout" (previously "Login" button). 
6. The user then can click the "Catalogue" button again to go to the Catalogue page. They can then click the "Add to Playlist" button to add a song to the playlist. This will generate a toast message of "Song added to your Playlist!".
7. The user can go through the full catalogue by clicking the pagination buttons on the bottom of the catalogue page or changing the sorting order by clicking the sort button at the top of the page with the drop-down trigger give four different sorting options (# Likes, # Dislikes, Newest, Oldest)

### Manual Testing
#### Navbar and Footer (All pages)
1. Navbar 
    - Visit the index.html/Home page on a desktop sized screen (lg)
    - Hover over the name text "Karaokean" and logo to check that the hover effects work.
    - Click the Name Header text "Karaokean" to check that it links to the Home page.
    - Hover over each navbar item to check the hover effect works for each one.
    - Click on each one of the navbar buttons to ensure that each links to the correct page.
    - Alter the screen size from desktop size down to medium devices (<992px) size to check that the navbar is responsive. At that size the navbar changes to the toggler icon with just the site name and logo. The menu items move to the sidenav menu.
    - Click the toggler icon to check that the drop-down sidenav menu activates.
    - Hover over each of the sidenav menu menu items and the login button to make sure their hover effect activates.
    - Click each of the drop-down menu buttons to make sure that they links to the correct page.
2. Footer
    - Check that the footer is correctly stuck to the bottom of the screen
    - Check that YouTube link in the footer works correctly
    - Alter the screen size from desktop size down to medium devices (<992px) size to check that the footer is responsive. 
3. Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/)

#### Home
- Check that both "Add Song" and "See Full Catalogue" buttons bring user to correct page. 
- Check that the sorting for the "Most Liked Songs" list is correct.

#### Catalogue
- Click sort button to make sure that the drop-down menu is trigger. Check that the sort options correspond to the sort option they implement on the page.
- Check that pagination is loading five videos. On page 1 check the previous chevron is disabled. An last page check the next chevron is disabled.
- Check that all pagination buttons work. Check that the current page is highlighted in a light blue box. Check that the wave-effects on all buttons work.
- Check that the "Check Lyrics" button launch new page for all songs
- Check that the "Add to Playlist" button generates toast message "To add song to your Playlist either register or login to your account!" when user not logged in and when logged in "Song added to your Playlist!"
- Check that the "Edit" button launches the edittrack.html page with all field holding the correct data
- Check that the "Delete" button removes the catalogue entry and that the same page is reloaded with a flash message of "*song name* deleted from catalogue"
- Check that the "Like" and "Dislike" buttons generated a toast message of "You Like/Dislike this Song!", respectively. And check that when the page is reloaded that the Like and Dislike numbers in the information panel of the song update (these do not update until after the page is reloaded).

#### Add Track / Edit Track
- Check that on pressing submit on blank inputs in all fields that the underlines, labels of each field all turn red and error message appears. Check that fields turn green on the input of a value and that a success message appears.
- Check that on pressing the "Submit" button when all fields are filled correctly that the user is  redirected back to the catalogue page and that the sorting order is set to newest so their entry is visable to them imediately.
- Check that on pressing the "Cancel" that the user is directed to the catalogue page in its default sorting order (# Likes).
- Check that on the Edit Track Page (edittrack.html) that the values for each field are correctly loaded from the database.

#### Genre
- On the Genres page (genres.html) check that clicking the "Add New Genre" button directs you to the addgenre.html page.
- Check that clicking the "Edit" button beside each genre in the list of genres directs you to the editgenre.html page where you can edit the genre name.

####  Add Genre / Edit Genre
- Check that on both the Add Genre and Edit Genre pages that on successful submission of the form, by clicking the "Add", "Edit Genre" , that the user is directed back to the genres page (genres.html).
- Check that on successfully adding a new genre on the Add Genre page the message "New genre *genre-name* added!" appears.
- Check that on successfully editing a genre on the Edit Genre page the message "Genre *genre-name* edited!" appears.
- Check that on clicking the "Cancel" button on both the Add Genre and Edit Genre page that the user is directed back to the genres page (genres.html).
- Check that when you change the name input field a genre name to another existing genre name and click the "Submit" button that an error message appears saying "Genre *genre-name* already exists".

#### Playlist

##### Playlist Editor
- Check that if you access the Playlist Editor page (playlist_page.html) without being logged into an account that the users are directed to a screen that asks them to loggin or register. Then Check that the login and register buttons direct the user to the login (loginpage.html) or registration (register.html) pages, respectively. 
- Check that if the user goes to the playlist page without having added any songs to their playlist that they are shown a screen asking them to add a song to their playlist on the catalogue page (catalogue.html) and a "Catalogue" button. Check that the "Catalogue" button directs the user to the catalogue page (catalogue.html).
- Check that when songs are added to the user's playlist that the list of added songs appears when the users visits playlist page (playlist_page.html).
- Check that the users can click the remove button beside the song name on the playlist list and that it deletes the entry and updates the list. 
- Check that duplicate songs on the playlist page can be individually deleted.
- Check that the "Play Playlist" button launches the Playlist Player page (playlist_play.html).

##### Playlist Player
- Check that the video associated with the first video on the playlist autoplays when the Playlist Player page (playlist_page.html) loads.
- Check that the volume and track progress bar controls for the video on the player page are disabled.
- Check that the "Skip" button will play the next song on the playlist immediately on being clicked.
- Check that the playlist panel on the right side of the playlist player page includes all the upcoming songs on the created playlist. Check that the song at the top of the list has the red text "Currently Playing" beside it. 
- Check that when the end of the last song on the playlist is reached that the toast message "You have reached the end of your playlist!" is displayed and that after three seconds the user is directed to the Playlist Editor page.

#### Login
- Check that if an unregistered user but tries to login with a unregistered username and password that they will receive a flash message saying the "Username doesn't exist".
- Check that if a registered user, who has input a existing username by incorrect password receives the flash message "Password was incorrect".
- Check that if  the user enters both an existing username and a correct password they will be redirected to the home page of the site and shown a flash message saying "Kon'nichiwa *their username*".
- Check that if  the user clicks the "Sign up Here!" button at the bottom of the page they are directed to the registration page.
- Check that when the user is logged into an account  the "login" button in the navbar changes to a "Logout" button and the users username appears beside the button highlighted in teal. 
- Check that the users username appears, highlighted, in the side nav bar for mobile devices.
- Check that when the user is logged in that the "Login" button becomes "Logout" button.
- Check that when the user clicks the Logout button the button will return to "Login" and that the  username  disappears.
- Check that on logout that the user is redirect to the home page and see the flash message "Sayōnara *username*".

#### Registration
- Check that if the user enters an existing username (with a password) a flash message will appear saying "*username* already exists"
- Check that if the users successfully enters a unique username (along with a password) that they are directed to the home page of the site and see the flash message "Welcome to Karaokean *username*".

#### Known Issues
There are a small number of known issues not dealt with during this development print. They are noted below and will be fixed in a future development sprint.

##### Lost Data when adding Genre

If a users partially inputs the data for a song into the input field on the "Add Track" page but doesn't see their desired genre in the drop-down list their next step would be to click the Add new genre option at the bottom of the list. This will bring them to the "Add Genre" page. However, when they return to the "Add Track" page, they will have lost the data that they had enter before clicking this option on the list. 

##### Console Error on Playlist Player Page
On the Playlist Player page (playlist_play.html), if the page is reloaded, a console error appears. This error states the following:

```
Failed to execute 'postMessage' on 'DOMWindow': The target origin provided ('https://www.youtube.com') does not match the recipient window's origin ('https://karaokean.herokuapp.com').
```
The source of this error is unclear as an origin parameter is provided in the YouTube API parameters code (see line 82 on playlist_play.html page). Reseach online fail to provide a solution to this error. However, it does not affect the performance of the API or the application overall so I was deem acceptable to submit the project with this error. This decision was discussed with my Mentor before submission.

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
3. In the pop up that appears labelled "Clone with HTTPs" section copy the URL
4. In your local IDE open Git Bash
5. Change the working directory to the location for the cloned directory to be stored.
6. Type "git clone" into the GIT CLI terminal and then paste in the URL copied from GitHub in step 3 (i.e. git clone https://github.com/DarrenCoppinger/milestone-project-3.git )
7. Hit enter and create your local drive.
8. Install the necessary requirements from the requirements.txt file using the command `pip3 install -r requirements.txt`
9. Generated a env.py file where you will store your MONGO_URI and SERCRET_KEY environmental variables. 
10. Set the SERCRET_KEY to your preferred value. 
11. Sign up for [MongoDB](https://www.mongodb.com) and create a named database, e.g. **Karaokean**. The app will uses the following *Collections* in that database with the following titles and fields (the app will generate fields):

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

10. Go to your created cluster in MongoDB and click the connect button, click "Connect your application". Then copy the connection string and set it equal to MONGO_URI in the env.py file. The connection string will be of the form: 
```
mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority
```
11. Run the application by typing the following command into the CLI:
    - python3 app.py


### Remote Deployment on Heroku
This app is currently deployed on heroku. The deployment is the code stored on the master branch of the project on GitHub. To deploy this project to Heroku required the following steps:
1. Register for Heroku and once signed in click the "New" button on the dashboard to create a new app.
2. In Heroku Name the app and specify the region (Europe in my case). 
3. Create a requirement.txt file to allow Heroku to install the required dependencies to run the app. The CLI text to input is as follows `pip3 freeze --local > requirements.txt`
4. Create a Procfile to inform Heroku what type of app is being deployed `echo web: python run.py > Procfile`
5. On the deployment tab of your project in Heroku click the Heroku GIT method for deployment.
6. In the CLI of you IDE input the following:
 ```
 $ heroku login
 $ heroku git:remote -a <karaokean>
 $ git push heroku master
 ```
 7. In the Heroku settings tab, click on the  "Real Config Vars" button to set environmental variables as follows:
 
 - IP: `0.0.0.0`
 - PORT: `5000`
 - MONGO_URI: `mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority`
 - SERCET_KEY: `<your_value>`
 
 8. In the top right of the heroku dashboard press the "Open App" button to view your deployed Heroku app.


## Credits
### Media
Images used in this site were used with the permission of [Elora Pautrat](https://www.elorapautrat.com/).

### Acknowledgements
- [Antonio Rodriguez](https://github.com/AkaAnto)
    - My Code Institute mentor.
- [Tim Nelson](https://github.com/TravelTimN/)
    - Code Institute tutor who helped me with the jQuery and JavaScript code required for this project.

### Disclaimer
This Website was produced for educational purposes only.

