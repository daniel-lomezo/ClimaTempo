# DevGrid
For this application, what was proposed to me was to perform requests on an API and query weather information from a list of approximately 170 different cities. 

To solve the problem of slowness, I studied a little more the services provided by "Open Wea thermap" I thought it would be better to save the city IDs and their respective names in a SQLite3 database using the data from the file "city.list.json", downloaded from the same platform., as it is simpler and easy to get started for a small project with this type of architecture.


Currently, the project consists of a small web application with a selector button with the names of the cities and which automatically then selects the city's weather data in a small form.
I used to develop this project:
    
    Python;

    Django;
  
    VueJS;

    BootStrap;

    Css;

    HTML;

I uploaded the application image to a Heroku server for faster testing by the evaluators.

    https://devgrid.herokuapp.com/

To get started, download the repository:
    
    git clone https://github.com/daniel-lomezo/DevGrid.git;

Navigate to the DevGrid folder:

    cd DevGrid 

After entering the folder, run the following commands in their respective order:

    sudo docker build --tag devgrid:latest 

    sudo docker run --name devgrid -d -p 8000:8000 devgrid:latest
  
