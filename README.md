# Email Drafter app

This repositrory represents my project created for authomated drafts creation using Python and Google API.\
The Google Cloud project was created with [official guide](https://developers.google.com/docs/api/quickstart/python).\
In this project I used OOP because it provides a clear and organized structure, class can be reused with different parameters, and simply because I use OOP almost always.

__main.py__ is the main file. After its succesfull execution it creates a draft in your gmail account. It includes a class EmailDrafter with three funcitons:
1. _init_ - standart initialization function. It takes receiver email, subject and content of email as its parameters.
2. _create_message_ - the function for creating MIMEText message (the body for the email).
3. _create_draft_ - the function for creating a draft using Gmail API.

__quickstart.py__ is the file which has been taken from the link above.
It's responsible for creating token.json based on credentionals.json which was downloaded from Google Cloud project API page.

In order to use the program don't forget to install necesarry libraries from requirements.txt.
