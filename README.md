# Azure-Vision-vs-GCP-Vision

## Overview

### TOOLS
* Install your preferred IDE. Example: VS Code

### HACK PRE-REQUISITES 

* Clone this repository. 
* Navigate to
* Create a new project
* Configure your billing account
* Search for Cloud Vision API -> Enable.
* Search for Vertex AI API 

### HACK #1 Detect Faces

In this hack, we will explore the Vision API features. The one we will experiment with is detecting faces. 

Steps
* Click on the three lines to navigate to the drop down list. Click on APIs & Services -> Credentials. Click  + Create Credentials -> Service Account. Select a role -> Basic -> Owner. Once created, go to keys -> Add Key -> JSON. Save this file inside the directory.
* Create a virtual env inside your preferred IDE. I am using VS Code. Once you are in the correct directory, opena terminal and run this command to create a virtual environment.
*   python -m venv gcpdemo
*   gcpdemo/Scripts/activate
* Install an important library
*   pip install --upgrade google-cloud-vision
*   pip install pandas
*   pip install pillow
* Open the Interpreter (CNTRL + SHIFT + P) to select your virtual environment.
* Run the script 



### HACK #2 Foundation Models

In this hack, we will explore the Generative AI Studio inside Vertex AI component of the GCP console. 

Steps 
* Navigate to the three lines at the top left of the GCP Console. You will see a dropdown list. Scroll down until you find the Artificail Intelligence section. We want to click on Vertex AI. It may be helpful to pin this service so it shows up at the top of the drop down next time. 
* You will see the Generative AI Studio on the left sidebar. Click on Vision. Choose the "Gen-AI-Demo-Img" from the data floder and upload it to the UI.
* We can experiemnt with the two features "Caption" and "Visual Q&A"
  
### HACK #3 Object Detection 

In this hack, we will explore how to create your own custom models in the Vertex AI portal. We will train a simple object detection model to determine between a Buffalo and a Zebra. 

Steps
* 



