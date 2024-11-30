# Outfitly
This is a project for Algorithms and Data Structures course
## Demo

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Current Status](#current-status)
- [Future Improvements](#future-improvements)
- [Technologies](#technologies)
- [Contributors](#contributors)

## Installation
### Prerequisites
- **Python 3** should be installed. You can check by typing `python --version` in the command line ot Terminal. If you don't have it installed you can download it for free from https://www.python.org/downloads/.
- A working **command line** or **Terminal** is required.
  
#### 1. Clone the Repository
```bash
git clone https://github.com/beauuks/ADS-Group-Project.git
```
#### 2. Change into the Project Directory
```bash
cd ADS-Group-Project
```
#### 3. Create and Activate a Virtual Environment
- Create
```bash
python3 -m venv venv
```
- Activate
  - On **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - On **MacOS/Linux**:
    ```bash
    source venv/bin/activate
    ```
#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 5. Run the Application
```bash
python app.py
```
## Features
#### 1. Wardrobe Management 
- **View wardrobe**: See all the items. If empty, you will be notified.
- **Add item**: Enter item name, type(e.g., tops, accessories, shoes), and optional details (color, material, occasion, season).
- **Edit item**: Modify the attributes of existing items.
#### 2. Outfit Suggestion
The app suggests outfits based on **season, weather, and style**.
- **Manual Input**: Enter season, weather, and style for suggestions.
- **Location-based Input**: Enter city and style to receive outfit suggestion based on **real-time** weather data.
## Current Status
- The Python app provides functionality of the algorithms, but there's no interaction with the frontend yet. 
- The frontend is currently only a demo of what the user interface will look like.
## Future Improvements
- **Integrating frontend and backend** for a fully functional website.
- **Community Features**: Implement user accounts, so that the users can save the outfits, see the past suggestions, interact with the community.
- **Additional features**: Recommendation system based on user history/preferences, additional outfit categories.
- **Image Support**: Allowg users to upload and receive suggestions in pictures.
- **Database**: to store user profiles / actions.
## Technologies
- Python 3
- HTML
- CSS
## Contributors
- Kanthad Sangudomlert
- Ana Khosiashvili
- Leen Hussein
- Rania Mansouri
- Sofía Meléndez Cabero
