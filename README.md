# Microsoft-Engage-Recommendation-System  
MicroFlix: Movie Recommendation System 
 
<img width="111" alt="image" src="https://user-images.githubusercontent.com/80244229/170878515-f2f73ab7-ed53-4239-8632-6927da3e09cb.png">


[Link to the deployed website](https://share.streamlit.io/manika137/microsoft-engage-recommendation-system/main/main.py)  
[Link to the demo video](https://www.youtube.com/watch?v=eMgymJA_zfc)  
[Link to document explaining the functionalities](https://mm.tt/map/2307094474?t=KiDIRKIWcp)  

## SALIENT FEATURES  
* **MOVIE RECOMMENDATION FEATURE**: User can choose their movie and the number of recommendations they need. Also shows the accuracy for each recommended movie and the Youtube link to its trailer. This uses content based filtering system.  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/80244229/170878170-003a3000-d454-4b47-883c-f9ae6d866388.png">


* **USER RATINGS**: User can choose to rate hundreds of movies from a scale of 0 to 5 and get the top five recommended movies along with their Pearson correlation value. This uses collaborative based filtering system.  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/80244229/170878249-0989111a-099f-4d95-b1ed-8ac19098718f.png">


* **CROSS RECOMMENDATION**: User can get their next perfect read by providing the name of their favourite movie.  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/80244229/170878298-8fd585b7-540a-42dd-870d-b934bc908c3a.png">


* **BUZZ-INGA**: Inspired from Buzzfeed questions, this section contains questions from selecting the funnier meme to choosing your favourite food item. The results of these will be used to recommend movies based on user's mood and state of mind.  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/80244229/170878377-5eea4120-7157-4d6d-88e7-1c0ac4cc042e.png">


* **MAP**- Aimed at promoting Indian states's regional movies, the user can select any state and he'll be redirected to a page with information about the the top regional movies of the area. This application currently has movies for 18 states.  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/80244229/170878397-3f986587-4ca0-4bef-b168-c1f40f35e4b1.png">


* **PROFILE**- The top recommendations of user from the movie recommendation and the buzz-inga section will be saved here.  
<img width="959" alt="image" src="https://user-images.githubusercontent.com/80244229/170878411-f6276b70-ace4-4152-953d-fc8ce3b3031a.png">  


* Developed using Streamlit, Python, HTML and CSS. Deployed on Streamlit Cloud.  


## GETTING STARTED  
* Clone or download this repository to your local machine.
* Install all the required libraries with the command ```pip install -r requirements.txt ```
* Open your terminal/command prompt from your project directory and run the file main.py by executing the command ```streamlit run main.py```
* You can also open your browser and type 'http://localhost:8501' in the address bar to see the result.

