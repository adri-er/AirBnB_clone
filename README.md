# 0x00. AirBnB clone - The console ✈️
The AirBnB project is one of the crowns jewels in the Holberton academic pensum, the first approach is to make a user interface from which we can create, modify and delete in our file storage. You are probably asking yourself what is that useful for? well, this is a tool to interiorize the knowledge and comprehend what works and doesn't work in storage before developing any web application.
![Logo Airbnb PNG transparente - StickPNG](http://assets.stickpng.com/images/580b57fcd9996e24bc43c513.png)

Airbnb is a company that provides a digital platform dedicated to the offer of accommodation of individuals and tourists (vacation rentals) through which hosts can advertise and hire the rental of their properties with their guests. Hosts and guests can rate each other as a reference for future users.

## Overview 🔍
Like any other user interface, our console works running a list of commands to execute a specific action that could be related to the creation, update, or deletion of a given instance inside the program. These instances belong to one of the classes listed below:
 - BaseModel
 - User
 - State
	@@ -14,28 +14,27 @@ Like any other user interface, our console works running a list of commands to e
 - Place 
- Review

BaseModel is a class that defines all common attributes and methods of other classes. To have a better understanding of how this inheritance model works, follow the next UML diagram.
![enter image description here](https://github.com/Juand0145/AirBnB_clone/blob/main/Untitled%20Diagram.png?raw=true)

## How to run the console 
The first step is to clone the repository using the following command:

    $ git clone https://github.com/Juand0145/AirBnB_clone.git
   Now to execute the console in interactive mode just enter to the repository and use the command:  

    $./console.py

   If everything works properly you should see a prompt (hbnb) and have a space to write your commands. If you want to access in not interactive mode use the following command:

    echo "<command>" | ./console.py

## How to use it
Next, there is a list of the features that the console interprets with specific commands. Some of these are:

 - `EOF`: It is the acronym for End Of File and will exit the console.
 - `quit`: Exit the console.
 - `<emptyline>`: overwrites default emptyline method and does nothing.
 - `create`: Creates a new instance using the classes presented in the overview section, saves it (to the JSON file) and prints the id.
```
juand0145@DESKTOP-HTDB37B:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
	@@ -48,7 +47,7 @@ d2393706-55e1-47ca-b86f-83faea4cc60e
** class doesn't exist **
(hbnb) 
```
 - `destroy`: Deletes an instance based on the class name and id (saves the changes into the JSON file).
 ```
(hbnb) destroy BaseModel d2393706-55e1-47ca-b86f-83faea4cc60e
(hbnb) destroy User 5119a616-6a57-4a64-9d76-1745058a54bb
	@@ -68,7 +67,7 @@ d2393706-55e1-47ca-b86f-83faea4cc60e
(hbnb) 
 
```
 - `all`: Prints all string representation of all instances based on the class name or if empty, prints all instances previusly saved.
 ```
(hbnb) all
["[User] (abead54c-c971-4f2a-a36a-5499137a7fb8) {'id': 'abead54c-c971-4f2a-a36a-5499137a7fb8', 'created_at': '2021-06-30T13:09:01.415673', 'updated_at': '2021-06-30T13:09:01.415673', '__class__': 'User'}", "[BaseModel] (f726cacb-3f8d-4bb1-b4d8-06158a7e21d0) {'id': 'f726cacb-3f8d-4bb1-b4d8-06158a7e21d0', 'created_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451), 'updated_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451)}", "[BaseModel] (d7b166fe-f669-4d76-b333-b258b0303b30) {'id': 'd7b166fe-f669-4d76-b333-b258b0303b30', 'created_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329), 'updated_at': datetime.datetime
	@@ -82,7 +81,7 @@ d2393706-55e1-47ca-b86f-83faea4cc60e
** class doesn't exist **
(hbnb) 
```
 - `update`: Updates an instance based on the class name and id by adding or updating attribute (saves the changes into the JSON file).
 ```
hbnb) create BaseModel
6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a
	@@ -92,8 +91,4 @@ hbnb) create BaseModel
(hbnb) all
['[BaseModel] (6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a) {\'id\': \'6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a\', \'created_at\': datetime.datetime(2021, 6, 30, 13, 24, 10, 879556), \'updated_at\': datetime.datetime(2021, 6, 30, 13, 24, 55, 392339), \'first_name\': \'"Juan"\'}']
(hbnb) 
```

## Authors ✒️
- Adriana Echeverri - [adri-er](https://github.com/adri-er)
- Juan David Tuta - [Juand0145](https://github.com/Juand0145)