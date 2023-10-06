#

Title Bucket List Travels

The aim of the website is to allow users to view different countries and find out which cities they contain, and also allow the user to add them to their bucket list, and check off which destinations have been visited, and which ones are still to be visited.

The user can create a country and add it to the list of countries on the destinations page. Each country can be edited, and the cities within the countries can be added or removed.

On the bucket list page, they can choose from the list of countries that are available on the destinations page and add them to a visited list or not visited list.  

The website was made using HTML, CSS and Python(with flask ,SQLAlchemy and PostgreSQL).
To run this project, you will need to install SQLAlchemy and Migrate.
In the terminal:  

```pip3 install flask-sqlalchemy```  

```pip3 install flask-migrate```  

```createdb bucket_list```  

```flask db init```  

```flask db migrate```  

```flask db upgrade```  


To populate the database, I have included a seed.py file that contains data for Countries and Cities. To run this, type into the terminal:  

```flask seed```

Finally, to run the server, use:  

```flask run```



PLANNING -

I started off by drawing class diagrams to ensure I had an understanding of the relationships between the classes.
Each country can have many cities, so city has the foreign key country_id, which links these 2 tables together.

<img src ="/static/images/class_diagrams.jpg" width=500px height=500px/>


I then moved on to drawing a wireframe for each page to get a rough idea of how I wanted my website to look, as you will see, as I have worked on my website I have made some changes to the original plan.

When implementing css into my website, I had a play around with many different styles, and decided to keep the background image constant throughout the website, and have a hero section on my home page, as you can see this is different to my original wireframe plan. 

<img src ="/static/images/home_wireframe.jpg" width=500px height=500px/>  

Figma was used to design a logo for my home page.
<img src ="/static/images/figma_logo.jpg" width=500px height=500px/> 

My destinations page has pretty much stayed identical except I decided to make the add country form part of this page, instead of being redirected to another page.
There is no search bar here as I planned for the MVP, and the search bar was an extension.  


<img src ="/static/images/destinations_wireframe.jpg" width=500px height=500px/>  

My Bucket List page has also stayed very similar, but again I kept the add to bucket list form on the same page, as I had quite a lot of empty space on this page.

<img src ="/static/images/bucket_list_wireframe.jpg" width=500px height=500px/>  





<img src ="/static/images/bucket_list_wireframe.jpg" width=500px height=500px/>


USER CASE DIAGRAM:

After creating the wireframes, I created a user case diagram to determine what routes I would need to create and for which pages I would need to create them for.

![user case diagram](/static/images/user_case_diagram.png)

USER SITEMAP :

I then created a user sitemap to determine the structure of the website so it was clear, and easy to navigate for the user.

![user sitemap](/static/images/user_sitemap.png)

TRELLO

To help break down my project into smaller, more manageable chunks, I used trello. This was helpful to track tasks that still needed to be done, what I was in the process of doing and what I had completed.

![trello planning](/static/images/trello.png)




A coding problem I solved:

I couldn't figure out how to make the cities change to either the visited, or not-visited tables when the checkbox was checked or unchecked.

By wrapping the checkbox in a form, and using the line  

```onchange="this.form.submit()```  

as a property of the checkbox, this allows the checkbox to essentially act as a submit button.
When the checkbox is then clicked, the form actions  
```/my_list/{{item.id}}/toggle-visit```  

I then made a route with a post method which has a function to update the visited value of the city that was checked or unchecked.
The line  
```item.visited = not (item.visited)```  
 
will return the opposite value, so if the Value is True, it will return false, and be committed to the database, and finally a redirect to the same page, so this will happen seamlessly.

![coding problem solved](/static/images/coding_problem_solved.png)




MAIN LEARNING POINTS: 
-Getting a lot more confident with setting up routes and knowing which routes I need.
-Confident with using template inheritance and conditional rendering as I wasn't so confident with that before this project.
-I made a lot of mistakes throughout the project and came across many errors and bugs, so I feel I have greatly improved on debugging my code and I look at errors as a challenge and an opportunity to learn.
