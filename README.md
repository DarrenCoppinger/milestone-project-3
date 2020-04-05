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

### Design

The style of the site is inspired by the asetetic of japanese karaoke bars (called Karaokeans). These places tend to have neon signs on the outside and have cyber punky interior with lots of lights brightly color lights and vibrant colors. To communicated this a vapourwave color scheme was chosen using pinks, blues and a small amounts of teal green. 

#### Framework
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
- [Add Genre](hhttps://i.ibb.co/x7JNqrx/Add-Genre.png)
- [Edit Genre](https://i.ibb.co/dGkhdSn/Edit-Genre.png)
- [Playlist Editor](https://i.ibb.co/7XHybqx/Playlist-list.png)
- [Playlist Player](https://i.ibb.co/L1wDFs4/Playlist.png)
- [Login](https://i.ibb.co/D5W147z/Login.png)
- [Register](https://i.ibb.co/Vw1RrVH/Register.png)

## Features

### Existing Features
#### Home
#### Catalogue
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

#### Disclaimer
This Website was produced for educational purposes only.