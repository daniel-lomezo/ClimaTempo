# DevGrid

To get started, download the repository
  --> git clone https://github.com/daniel-lomezo/DevGrid/
  
Navigate to the DevGrid folder:
  --> cd DevGrid 

After entering the folder, run the following commands in their respective order:
  --> sudo docker build --tag devgrid:latest 
  --> sudo docker run --name devgrid -d -p 8000:8000 devgrid:latest
  
