# Microsoft-Engage-Recommendation-System
MicroFlix: Movie Recommendation System

[Link to the deployed website](https://share.streamlit.io/manika137/microsoft-engage-recommendation-system/main/main.py)  
[Link to the demo video]()  
[Link to document explaining the functionalities](https://mm.tt/map/2307094474?t=KiDIRKIWcp)  

## SALIENT FEATURES  
* **MOVIE RECOMMENDATION FEATURE**: User can choose their movie and the number of recommendations they need. Also shows the accuracy for each recommended movie and the Youtube link to its trailer. This uses content based filtering system.
* **USER RATINGS**: User can choose to rate hundreds of movies from a scale of 0 to 5 and get the top five recommended movies along with their Pearson correlation value. This uses collaborative based filtering system.  
* **CROSS RECOMMENDATION**: User can get their next perfect read by providing the name of their favourite movie.
* **BUZZ-INGA**: Inspired from Buzzfeed questions, this section contains questions from selecting the funnier meme to choosing your favourite food item. The results of these will be used to recommend movies based on user's mood and state of mind.
* **MAP**- Aimed at promoting Indian states's regional movies, the user can select any state and he'll be redirected to a page with information about the the top regional movies of the area. This application currently has movies for 18 states.
* **PROFILE**- The top recommendations of user from the movie recommendation and the buzz-inga section will be saved here.  
* Developed using Streamlit, Python, HTML and CSS. Deployed on Streamlit Cloud.

## GETTING STARTED  
* Clone or download this repository to your local machine.
* Install all the required libraries with the command ```pip install -r requirements.txt ```
* Open your terminal/command prompt from your project directory and run the file main.py by executing the command ```streamlit run main.py```
* You can also open your browser and type 'http://localhost:8501' in the address bar to see the result.

