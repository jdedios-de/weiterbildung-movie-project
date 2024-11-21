
# 🎬 Movie Library

A Python-based project to manage and explore your movie collections effectively.  

## 🌟 Features  
- **List**: Display all the movies in the CSV or JSON file.
- **Add, Update, Delete**: Easily manage your movie collection.  
- **Stats**: Show the best and worst movie with rating  
- **Random movie**: Generate a random movie.
- **Search movie**: Quickly find movies by title.
- **Movies sorted by rating**: Sort movies based on their ratings.
- **Movies sorted by year**: Sort movies by their release year.
- **Filter movies**: Filter movies by year and rating.
- **Generate website**: Create an index.html file containing the movies in your library.


## 🛠️ Technologies Used  
- **Python**  
- **Requests**: Fetch external movie data via APIs.  
- **Python-Dotenv**: Secure environment variables.  
- **Pytest**: Ensure robust code through testing.  

## 🚀 Installation  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/masterschool-weiterbildung/weiterbildung-movie-project.git  
   cd weiterbildung-movie-project  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Create a `.env` file** for environment variables:  
   ```plaintext  
   key=your_api_key 
   ```  

4. **Run the application**:  
   ```bash  
   python main.py  
   ```  

## 📁 Project Structure  
```plaintext  
weiterbildung-movie-project/  
│  
├── main.py              # Main application file  
├── movie_app.py         # A command-line movie management application.
├── requirements.txt     # Project dependencies  
├── _static/             # Static files (CSS, JS, Images) and HTML templates 
├── movie/               # Directories data, services, storage and utilities for managing the movie applications  
├── .env                 # Environment variables
└── README.md            # Project documentation  
```  
