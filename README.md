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
All pages includes a responsive navigation bar and title at the top of the page. The title and logo acts as a "Home" button. On medium and small screen size the navbar reduces to just the title and logo, with the pages buttons concealed in a sidebar accessable via a menu icon in the lefthand corner of the navbar. The navbar contains the Home, Catalogue, Add Song, Genre, Playlist buttonsmenu items and a login button. The login is included as a button to draw attention to it. 

#### Home
The home page includes an "About" section with information about the website followed by two buttons connecting to the "Add Song" and "Catalogue" page. There is also a "Most Likes Songs" section which has a leaderbaord of the top five most liked songs in the catalogue followed by a button which likes to the full catalogue page.
#### Catalogue
The "Catalogue" page present all of the songs added to the database broken up with the use of pagination. Each pages displays 5 songs from the database. 

At the bottom of the page are a collection of pagination buttons which inlcude a previous and next chevron and a list of all the available pages of songs. On the first page the previous chevron is disabled and on the last page the next chevron is disabled thereby preventing the calling of a catalogue page that doesn't have any songs associated with it. Each of the page number buttons is clickable with the current page number highlighted in a outline box. 

At the top of the page is a sort box which is a dropdown menu box. There are 4 options of sorting to chose from: Most Likes, Most Disliked, Newest Song, Oldest Song. The default sort value is the "Most Liked" option.

Each song in the catalogue is displayed in the order that is specified. The video associated with the song is displayed on the left handside of the screen that are greater then 600px using the YouTube iFrame API with the information panel and buttons displayed on the right hand third of the viewport. For viewports less that 600px in width the display changes to the video container on top with the information panel and buttons below.  

The video is contained in a Materialize "video-container" class which allows it to change size responsively. Click the YouTube play logo will play the embedded video on the page. Each song video has YouTube controls active including clicking the song title to launch the song on Youtube, adding to a personal "Watch Later" list, and a share the video using the YouTube link. 

Each song in te catalogue also has an associated information panel on the rightwhich includes information on the specific songs and a number of buttons. The song title, year of release and artist are detailed at the top of the box. This is followed by text showing the current number of "Likes" and "Dislikes" that the songs has. 

Below the song information panel is a number of number of buttons including: "Check Lyrics", "Add to Playlist", "Edit", "Delete", "Like" and "Dislike". When clicked the "Check Lyrics" button will launch a new page with the songs lyrics submitted when the song document was created. The "Add Playlist" button will 
#### Add Song 
#### Genre 
#### Playlist

### Features left to Implement
Search by genre
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
### User Stories Testing

### Manual testing of elements and functionality on each page

#### Home
#### Catalogue
#### Add Song 
#### Genre 
#### Playlist

## Development

### To Run Project Locally
To clone or copy this project from GitHub follow these steps:
1. Follow this link to the [project repository on GitHub] (https://github.com/DarrenCoppinger/playwright-milestone-project)
2. On the left side of the page click the green button labelled "Clone or Download"
3. In the pop up that appears labe;led "Clone with HTTPs" section copy the URL
4. In your local IDE open Git Bash
5. Change the working directory to the to the location for the cloned directory to be stored.
6. Type "git clone" and then paste in the URL copied from GitHub in step 3
7. Hit enter and create your local drive.

## Credits
### Media
Images ussed in this site were used with the permission of <a href="https://www.elorapautrat.com/">Elora Pautrat</a>

### Content

### Acknowledgements
- [Antonio Rodriguez](https://github.com/AkaAnto)
    - My Code Institute mentor.
- [Tim Nelson](https://github.com/TravelTimN/)
    - Code Institute tutor who helped me with the jQuery and JavaScript code required for this project.

#### Disclaimer
This Website was produced for educational purposes only.