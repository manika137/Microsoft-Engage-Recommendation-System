# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:53:22 2022

@author: manika
"""

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pickle
import random
import pandas as pd
import requests
from functools import lru_cache
import urllib.request
import re




           
def main():
    st.markdown("""<style> p {
                            text-align: center};
                            </style>""", unsafe_allow_html=True)
    st.markdown(""" <style> img {
         border-radius:10px; 
         } </style> """, unsafe_allow_html=True)
                            
            
                                
    #INITIALISING SESSION STATE VARIABLES 
    if 'drama' not in st.session_state:
        st.session_state.drama = 0
    if 'comedy' not in st.session_state:
        st.session_state.comedy = 0
    if 'thriller' not in st.session_state:
        st.session_state.thriller = 0
    if 'animation' not in st.session_state:
        st.session_state.animation = 0
    if 'romance' not in st.session_state:
        st.session_state.romance = 0
    if 'family' not in st.session_state:
        st.session_state.family = 0
    if 'scifiction' not in st.session_state:
        st.session_state.scifiction = 0
    if 'action' not in st.session_state:
        st.session_state.action = 0

    if 'profile_content_recommendations' not in st.session_state:
        st.session_state.profile_content_recommendations = []
    if 'movie_key' not in st.session_state:
        st.session_state.movie_key = 0
        
    if 'profile_buzzfeed_recommendations' not in st.session_state:
        st.session_state.profile_buzzfeed_recommendations = []
    if 'buzzfeed_key' not in st.session_state:
        st.session_state.buzzfeed_key = 0
        
    #FUNCTION TO GET THE YOUTUBE TRAILER URL
    @lru_cache(maxsize=10)
    def play_yt_video(selected_movie_name):
        search_keyword = selected_movie_name+"trailer"
        search_keyword = search_keyword.replace(" ", "+")
        html = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        
        # Get URL for the first search result in Youtube
        yt_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        return yt_link
        
    
    #USER SEARCH DISPLAY DATA
    def profile_data(poster_link,num):
           
           if num==0:
               st.session_state.movie_key+=1
               st.session_state.profile_content_recommendations.append({"movie_key": st.session_state.movie_key, "link": poster_link})
               
           elif num==1:
               st.session_state.buzzfeed_key+=1
               st.session_state.profile_buzzfeed_recommendations.append({"buzzfeed_key": st.session_state.buzzfeed_key, "link": poster_link})
             
    #IMPORTING PICKLE FILES
    movies_dict = pickle.load(open('Pickle-files/movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('Pickle-files/similarity.pkl', 'rb'))
    
    ratings_dict = pickle.load(open('Pickle-files/ratings.pkl', 'rb'))
    ratings = pd.DataFrame(ratings_dict)

    books_dict = pickle.load(open('Pickle-files/books_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)

    book_images_dict = pickle.load(open('Pickle-files/book_images_dict.pkl', 'rb'))
    book_images = pd.DataFrame(book_images_dict)

    quiz_data = pickle.load(open('Pickle-files/quiz_data.pkl', 'rb'))
    quiz = pd.DataFrame(quiz_data)
    
    user_rating_movie_dict = pickle.load(open('Pickle-files/user_rating_movie.pkl', 'rb'))
    user_rating_movie = pd.DataFrame(user_rating_movie_dict)

    
    logo = Image.open(r'Images/logo.png')
    
    #CREATING WEBSITE'S MAIN NAVBAR
    with st.sidebar:
        choose = option_menu(menu_title="MicroFlix", options=["About", "Movie Recommendation", "User Ratings", "Cross Recommendation", 
                                                        "Buzz-inga", "Map", "Profile"],
                             icons=['house-fill', 'bookmark-heart', 'kanban',
                                    'book', 'patch-question-fill', 'pin-map-fill', 'save2'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
                                 "menu-title": {"color": "orange"},
            "container": {"padding": "5!important", "background-color": "#00000"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"color": "orange", "background-colour": "red", "font-size": "16px", 
                         "text-align": "left", "margin": "0px", "--hover-color": "#fae5df"},
            "nav-link-selected": {"background-color": "#fae5df"},
        }
        )

    
    
    
    
    
    
    if choose == "About":
        st.markdown("""<style> p {
                            text-align: left; font-size:18px; }
                        h3{text-align:center; font-size: 27px; color:#ed7966; background-color:#f5cac2; font-family:'georgia' }
            
                            </style>""", unsafe_allow_html=True)
                        
                            
        col1, col2 = st.columns([0.2, 0.8])
        
        with col1:               
            st.image(logo, width=130 )
        st.write("Welcome to my recommendation engine! This engine has 5 major recommendation features-")
        
        st.subheader("Movie recommendation- content based filtering")
        st.write("Choose your preferred movie and the number of recommendations you require to get the movie recommendations based on genre, cast members and storyline.")
        
        st.subheader("Movie recommendation- collaborative based filtering")
        st.write("Rate movies out of 5 and we'll recommend movies based on user similarity. You can rate as many movies as you like to get more precise recommendations!")
        
        st.subheader("Cross Recommendation (Books)")
        st.write("Name your favourite movie and leave the responsibility of getting the perfect book recommendation on us.",
                 "Perfect opportunity to begin your reading journey or save the hassle of finding the next perfect read.")
        
        st.subheader("Buzz-inga")
        st.write("Inspired from Buzzfeed quizzes, Buzz-inga has quirky questions from your preferred food item to your favourite meme.",
                 "Answer under the four sections in Buzz-inga and we'll figure out your movie liking according to your mood and state of mind.")
        
        st.subheader("Map")
        st.write("From Parasite to Spider Man, we'll checklisted all. Time to do the same for our regional movies too.",
                 "Select any state on the Indian map and we'll direct you to the best feature movies of the area.")
        
      
        with col2:               
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}  </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">INTRODUCTION</p>',unsafe_allow_html=True)

        





    #RECOMMENDING MOVIES BASED ON CONTENT RECOMMENDATION (MATCHING GENRE, CAST NAME, STORYLINE)
    elif choose == "Movie Recommendation":        
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">MOVIE RECOMMENDATION</p>', unsafe_allow_html=True)
        
        st.markdown(""" <style> img {
        height:300px; width: 300px} 
        </style> """, unsafe_allow_html=True)
    
        st.markdown(""" <style> code {
        color='pink'} 
        </style> """, unsafe_allow_html=True)

        
        #FUNCTION TO GET MOVIE POSTER FOR THE RECOMMENDED MOVIE
        def fetch_poster(movie_id):
            url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
                movie_id)
            data = requests.get(url)
            data = data.json()  # ???
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        
        
        #FUNCTION TO FIND THE RECOMMENDED MOVIE ACCORDING TO THE MOVIE NAME PROVIDED
        @lru_cache(maxsize=3)
        def recommend_movie(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]

            #Getting the top 5 movies based on distance
            movies_list = sorted(list(enumerate(distances)),
                                 reverse=True, key=lambda x: x[1])[1:6]
            movies_list_final = []
            
            #Getting the top recommendations considering the votes 
            for count, ele in movies_list:
                ele = ele * movies['vote_average'][count]
                temp = [count, ele]
                movies_list_final.append(temp)

            movies_list_final.sort(reverse=True, key=lambda x: x[1])

            recommended_movies = []
            recommended_movies_posters = []
            accuracy = []

            for i in movies_list_final:
                movie_id = movies.iloc[i[0]].id
                accuracy.append(i)
                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            
            #Sending the top movie recommendation to the profile's page
            profile_data(recommended_movies_posters[0],0)
            return recommended_movies, recommended_movies_posters, accuracy    

        st.write("Search for your favourite movie and select the number of recommendations you need.")
        st.write("")
        
        selected_movie_name = st.selectbox(
            'SEARCH FOR YOUR FAVOURITE MOVIE!', movies['title'].values)

        number_of_recommendations = st.selectbox(
            'NUMBER OF RECOMMENDATIONS NEEDED', (1, 2, 3))
        
        if st.button('Recommend'):
            names, posters, accuracy = recommend_movie(selected_movie_name)
            
            if number_of_recommendations == 1:
                st.markdown(""" <style> h2 {text-align:center}</style>""", unsafe_allow_html=True)
                st.header(names[0])
                col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                col2.image(posters[0],use_column_width=True)
               
                #st.image(posters[0])
                
                if(accuracy[0][1] > 2):
                    st.code("ACCURACY MATCH: 100%")
                else:
                    text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                    st.code(text)
                    
                with st.expander("PLAY THE TRAILER"):
                    yt_link = play_yt_video(names[0])
                    st.video(yt_link)
            


            elif number_of_recommendations == 2:
                col1, col2 = st.columns(2)
                with col1:
                    st.write()
                    st.subheader(names[0])
                    st.image(posters[0])
                    
                    if(accuracy[0][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[0])
                        st.video(yt_link)

                with col2:
                    st.subheader(names[1])
                    st.image(posters[1])
                    if(accuracy[1][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[1][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[1])
                        st.video(yt_link)
           
            elif number_of_recommendations == 3:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text(names[0])
                    st.image(posters[0])
                    
                    if(accuracy[0][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[0][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[0])
                        st.video(yt_link)

                with col2:
                    st.text(names[1])
                    st.image(posters[1])
                    
                    if(accuracy[1][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[1][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[1])
                        st.video(yt_link)

                with col3:
                    st.text(names[2])
                    st.image(posters[2])
                    
                    if(accuracy[2][1] > 2):
                        st.code("ACCURACY MATCH: 100%")
                    else:
                        text="ACCURACY MATCH:"+ str(round((accuracy[2][1]-1)*100,2))+ "%"
                        st.code(text)
                        
                    with st.expander("PLAY THE TRAILER"):
                        yt_link = play_yt_video(names[2])
                        st.video(yt_link)








    #RECOMMENDING MOVIES BASED ON USER RATINGS (FINDING SIMILARITIES AMONG USERS- COLLABORATIVE FILTERING)
    elif choose == "User Ratings":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">COLLABORATIVE FILTERING</p>',
                    unsafe_allow_html=True)
        
        st.markdown(""" <style> h3 {
        text-align: center;} 
        </style> """, unsafe_allow_html=True)
    
        
        st.write("Rate the movies (out of 5) according to your taste and we'll take care of the rest! To get your top recommendations",
                 ", select the option of not rating the movies further.")
        #FUNCTION TO GET SIMILARITY SCORES BASED ON USER RATINGS
        def get_similar_movies(movie_name, user_rating):
            similar_score = ratings[movie_name]*(user_rating-2.5)
            similar_score = similar_score.sort_values(ascending=False)
            return similar_score


        i = 0
        option = []
        while i < 10:
            option.append(random.randrange(0, 4))
            i += 1


        user_ratings = []

        #FUNCTION TO PRINT THE STARS BASED ON USER RATINGS
        @lru_cache(maxsize=3)
        def get_stars(score):
            if score == 1:
                return "⭐"
            elif score == 2:
                return "⭐⭐"
            elif score == 3:
                return "⭐⭐⭐"
            elif score == 4:
                return "⭐⭐⭐⭐"
            elif score == 5:
                return "⭐⭐⭐⭐⭐"
            
            
        #FUNCTION TO PRINT THE MOVIE NAME AND IT'S RATING THAT USER ADDED
        @lru_cache(maxsize=3) 
        def show(movie, score):
            a = [movie, score]
            user_ratings.append(a)
            if(score > 0):
                string = movie+"         " + get_stars(score)
                show_ratings.append(string)


        i = 0
        x = 0
        flag = 0
        f = 0
        show_ratings = []
        for x in range(500):
            movie1 = user_rating_movie[0][x]
            with st.expander(movie1):
                score = st.number_input('INSTERT NUMBER', 0, 5, 0, 0, key=x)
                show(movie1, score)

            if(x % 10 == 0 and x != 0):
                st.subheader("YOUR MOVIE RATINGS:")
                for i in show_ratings:
                    st.write(i)
                option = st.selectbox('Want to rate more movies?', ('', 'Yes, why not', 'Nope'), key=x)
                if(option == 'Yes, why not'):
                    continue
                elif(option == 'Nope'):
                    f = 1
                    break
                else:
                    f = 0
                    break
            x += 1
            

        flag = 1
        similar_movies = pd.DataFrame()
        if(flag == 1 and f == 1):
            for movie, rating in user_ratings:
                similar_movies = similar_movies.append(
                    get_similar_movies(movie, rating), ignore_index=True)
            st.subheader("TOP 5 MOVIE RECOMMENDATIONS:")
            st.write(similar_movies.sum().sort_values(ascending=False)[:5])
           







    #RECOMMENDING BOOKS BASED ON USER'S FAVOURITE MOVIE(CROSS RECOMMENDATION)
    elif choose == "Cross Recommendation":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">BOOK RECOMMENDATION</p>',
                    unsafe_allow_html=True)
        
        #STYLING 
        st.markdown("""<style> 
                        img{
                            height:300px
                            };
                        </style>""", unsafe_allow_html=True
                )
        
        #FUNCTION TO GIVE BOOK RECOMMENDATION BASED ON USER'S FAVOURITE MOVIE
        @lru_cache(maxsize=3)
        def recommend_book(movie):
            if movie not in books['title'].unique():
                movie_index = movies.loc[movies['title'] == movie].index[0]
                maxi = 0
                book_index = 0
                num = 0
                list2 = movies['genres'][movie_index]
                
                for i in books.index:
                    list1 = books['genre'][i]
                    num = len(set(list1) & set(list2))
                    
                    if num > maxi:
                        maxi = num
                        book_index = i
                
                name = books['title'][book_index]
                
                if (book_images['name'] == name).any():
                    book_image_index = book_images[book_images['name']== name].index[0]
                    link = book_images['l'][book_image_index]
                
                elif(books['author'][book_index]=="Tyler Edwards"):
                    link="https://images-eu.ssl-images-amazon.com/images/I/51I89NSwLGL._SX342_SY445_QL70_ML2_.jpg"
                    
                elif(books['author'][book_index]=="David Dennis"):
                    link="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1354880275l/16240980.jpg"
                    
                else:
                    link = "https://pbs.twimg.com/media/DL-ORRkVAAEey8m.jpg"

                author = books['author'][book_index]
                goodreads_link = books['book_link'][book_index]
                pages = books['num_of_page'][book_index]
                rating = books['rate'][book_index]
                return link, author, goodreads_link, rating, pages


            else:
                book_index = books.loc[books['title'] == movie].index[0]
                book_image_index = book_images.loc[book_images['name']
                                                   == movie].index[0]
                author = books['author'][book_index]
                link = book_images['l'][book_image_index]
                goodreads_link = books['book_link'][book_index]
                pages = books['num_of_page'][book_index]
                rating = books['rate'][book_index]
                return link, author, goodreads_link, rating, pages

        selected_movie_name = st.selectbox(
            'SEARCH FOR YOUR MOVIE HERE!', movies['title'].values)
        
        
        if st.button('Recommend'):
            link, author, goodreads_link, rating, pages = recommend_book(
                selected_movie_name)
            
            with st.expander("*Drumroll*    Your book recommendation is ready!"):
                if(link!="https://pbs.twimg.com/media/DL-ORRkVAAEey8m.jpg"):
                    col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                    col2.image(link, caption="Novel Coverpage", use_column_width=True)
                else:
                    st.image(link, caption="Novel Coverpage")
                st.write(author)
                st.write("RATING: ", rating)
                st.write("CHECK OUT THE BOOK: ", goodreads_link)
                st.write("NUMBER OF PAGES: ", pages)







    elif choose == "Buzz-inga":

        st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633; text-align:center;} 
            </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">BUZZFEED</p>', unsafe_allow_html=True)

        #STYLING
        st.markdown("""<style> img {
                            height: 250px};
                            </style>""", unsafe_allow_html=True
                    )
        st.markdown("""<style> button {
                            margin-left:100px
                              position: relative;
                              left: 2000px;
                            </style>""", unsafe_allow_html=True
                    )
        st.markdown(""" <style> .question_font {
            font-size:18px ; font-family: 'Spade'; border-radius: 5px; padding:10px; text-align: center; color: red; background-colour: white} 
            </style> """, unsafe_allow_html=True)

        choose = option_menu(menu_title=None, options=["FILMY", "CUISINE", "CHOICES", "MEMES", "RESULTS"],
                             #icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                             default_index=0,
                             orientation="horizontal"
                             )

        if choose == 'FILMY':
            col1, col2 = st.columns(2)
            # THRILLER
            list1 = ["Frankly, my dear, I don't give a damn.",
                     "You’d be surprised what even a good man is capable of in the right situation.",
                     "You better wake up. The world you live in is just a sugarcoated topping. There is another world beneath it, the real world. And if you want to survive it, you better learn to pull the trigger.",
                     "See, I’m not a monster. I’m just ahead of the curve.",
                     "He’s Not A Hero. He’s A Silent Guardian, A Watchful Protector. A Dark Knight",
                     "Rishtey mein toh hum tumhare baap lagte hai, naam hai Shahenshaah!",
                     "Crime Master Gogo naam hai mera, aankhen nikal ke gotiyan khelta hun main.",
                     "How’s the josh?",
                     "Don’t underestimate the power of a common man!",
                     "Main aaj bhi pheke hue paise nahin uthata."]

            # ANIMATION
            list2 = ["Virgil: 'You think you have a chance here? I have an army.' Sam: 'Oh, yeah? Well, I’ve got my mom.'",
                     "Dosti ka ek usool hai madam – no sorry, no thank you.",
                     "Mogambo khush hua",
                     "Bade bade deshon mein aisi choti-choti baatein hoti rehti hai, Senorita.",
                     "All izz well",
                     "Tumse naa ho payega.",
                     "Houston, we have a problem.",
                     "ADVENTURE IS OUT THERE",
                     "I’m only brave enough when I have to be. Being brave doesn’t mean you go looking for trouble.",
                     "There is no secret ingredient. It’s just you."]
            
    

            st.markdown('<h1 class="question_font">OH SO FILMY..</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    st.write(random.choice(list1))
                    if(st.button('DIALOGUE1')):
                        st.session_state.thriller+=1
                        
                        
                with col2:
                    st.write(random.choice(list2))
                    if(st.button('DIALOGUE2')):
                        st.session_state.animation+=1


        elif choose == 'CUISINE':
            # ROMANCE
            list1 = ["https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dinner-ideas-for-two-french-onion-soup-1641934966.jpg",
                     "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dinner-ideas-for-two-shrimp-scampi-1641934138.jpg?crop=0.906xw:0.906xh;0.0390xw,0.0625xh&resize=480:*",
                     "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/romantic-dinner-ideas-rigatoni-with-chicken-broccoli-and-bolognese-1609185894.jpg?crop=0.544xw:0.816xh;0,0.184xh&resize=480:*",
                     "https://content3.jdmagicbox.com/comp/def_content/coffee_shops/default-coffee-shops-7.jpg",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8N3R9OEOE8jrW12CTcpwlhmbyd2JZ-YYxQA&usqp=CAU",
                     "https://www.chefworks.com.au/assets/images/blog/most-popular-cafe-foods-2020/Cafe_Burger.jpg",
                     "https://i.pinimg.com/736x/7e/19/45/7e19458b55c8eecde96da947cba2200b.jpg",
                     "https://media.istockphoto.com/photos/margherita-pizza-picture-id1359188521?b=1&k=20&m=1359188521&s=170667a&w=0&h=4cVc9DGaS2eU56QAAXoVCU5BPmuULNMTKPZVJbdEuKc=",
                     "https://bellyfull.net/wp-content/uploads/2020/08/Omelette-blog-3-500x500.jpg",
                     "https://thumbs.dreamstime.com/b/breakfast-french-toast-indian-pakistani-food-bread-tea-breakfast-french-toast-indian-pakistani-food-bread-tea-189702044.jpg"]

            # FAMILY
            list2 = ["https://b.zmtcdn.com/data/pictures/9/19451479/4d73622168afc1c628bf7bad5802fd56.jpg?fit=around|771.75:416.25&crop=771.75:416.25;*,*",
                     "https://static.toiimg.com/thumb/53110049.cms?width=1200&height=900",
                     "https://i.ytimg.com/vi/3dWf6BNZPfo/maxresdefault.jpg",
                     "https://rookiewithacookie.com/wp-content/uploads/2020/05/IMG_2570.jpg",
                     "https://i.ndtvimg.com/i/2017-10/diwali-food-menu_620x350_71507898681.jpg",
                     "https://pipingpotcurry.com/wp-content/uploads/2020/11/Dosa-recipe-plain-sada-dosa-Piping-Pot-Curry.jpg",
                     "https://b.zmtcdn.com/data/pictures/chains/2/47572/6d88abe04745826ed75c704c02581742_featured_v2.jpg",
                     "https://sallysbakingaddiction.com/wp-content/uploads/2013/04/triple-chocolate-cake-4.jpg",
                     "https://curlytales.com/wp-content/uploads/2017/06/Shiv-Mishthan-Bhandar.jpg",
                     "https://i0.wp.com/Tropicsgourmet.com/wp-content/uploads/2015/10/indian-sweet-371357_1920.jpg"]
            
            st.markdown(""" <style> .question_font {color: green} </style> """, unsafe_allow_html=True)
            
            
            st.markdown('<h1 class="question_font">FEED ME PLEASE...</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)

                    if(st.button('BON APPETITE!')):
                        st.session_state.romance+=1
                        
                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)
                    
                    if(st.button('YUMMM')):
                        st.session_state.family+=1



        elif choose == 'CHOICES':
            # SCIFICTION
            list1 = ["https://storage.googleapis.com/gweb-uniblog-publish-prod/images/sleep-01.max-1000x1000.png",
                     "https://images.everydayhealth.com/images/emotional-health/meditation/a-complete-guide-to-meditation-722x406.jpg",
                     "https://images.ctfassets.net/81iqaqpfd8fy/41KiNVEWQM6MgY8QEGkoco/44b9952239085ad2c731b3dcef4cc94f/selfcareguide-02.jpg?h=620&w=1440",
                     "https://thumbs.dreamstime.com/b/angry-arguing-couple-people-shouting-vector-illustration-husband-wife-blaming-each-other-problem-man-woman-quarreling-212871922.jpg",
                     "https://www.rp-assets.com/images/news/2020/01/24/74412-large.jpeg",
                     "https://ggie.berkeley.edu/wp-content/uploads/2019/09/Listening_to_Music_Mindfully_1200x630.jpg",
                     "https://www.parkavepd.com/wp-content/uploads/2019/01/Park-View-Pediatric-7-Ways-To-Make-Brushing-Teeth-Fun-For-Your-Child.jpg",
                     "https://www.petmd.com/sites/default/files/styles/article_image/public/going-for-a-walk-picture-id917875026.jpg?itok=egUc9l-k",
                     "https://www.thesprucecrafts.com/thmb/4krlR_ONU4EDXKbCb8FCWFkz--Y=/2121x1414/filters:fill(auto,1)/GettyImages-922707682-5b90467bc9e77c0025931eef.jpg",
                     "https://www.mountainjobs.com/wp-content/uploads/2021/05/pexels-andre-furtado-2916820-750x458.jpg"]

            # ACTION
            list2 = ["https://thumbs.dreamstime.com/b/kids-play-football-child-soccer-field-outdoor-stadium-children-score-goal-game-little-boy-kicking-ball-school-172305207.jpg",
                     "https://m.economictimes.com/thumb/msid-89199209,width-1200,height-900,resizemode-4,imgsize-51168/working-out-in-the-gym.jpg",
                     "https://www.euston96.com/wp-content/uploads/2019/09/Horse-riding.jpg",
                     "https://media.istockphoto.com/vectors/children-dancing-vector-id939153522?k=20&m=939153522&s=612x612&w=0&h=taiOnstHlJbwXhqahfSuiStk2W_ZYEGf0diYEVkuxbs=",
                     "https://images.pexels.com/photos/2889491/pexels-photo-2889491.jpeg?cs=srgb&dl=pexels-brady-knoll-2889491.jpg&fm=jpg",
                     "http://www.popcornoncouch.com/wp-content/uploads/2016/05/cinemaaudience.jpg",
                     "https://im.rediff.com/news/2019/oct/16khandu1.jpg?w=670&h=900",
                     "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y29va2luZyUyMGhvbWV8ZW58MHx8MHx8&w=1000&q=80",
                     "https://media.istockphoto.com/photos/young-woman-making-bed-at-home-picture-id1138390931?k=20&m=1138390931&s=612x612&w=0&h=of1Asq66j4sa4cTSywHwz5bCmRfTPFZG1_q3pmOxjRE=",
                     "https://www.kevinandamanda.com/wp-content/uploads/2021/12/G0056963-720x960.jpg"]
            
            st.markdown(""" <style> .question_font {color: aqua} </style> """, unsafe_allow_html=True)
            
            
            st.markdown('<h1 class="question_font">LIFE CHOICES...</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)

                    if(st.button('TEAM LEFT')):
                        st.session_state.scifiction += 1

                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)
                    
                    if(st.button('TEAM RIGHT')):
                        st.session_state.action+=1


        elif choose == 'MEMES':
            # DRAMA
            list1 = ["https://i.pinimg.com/originals/9a/c0/a4/9ac0a42d660955f0ecc714c37ae96163.gif",
                     "https://img.buzzfeed.com/buzzfeed-static/static/2017-04/18/15/asset/buzzfeed-prod-fastlane-01/sub-buzz-32159-1492543077-15.png?downsize=900:*&output-format=auto&output-quality=auto",
                     "https://sweatpantsandcoffee.com/wp-content/uploads/2018/12/1-Shampoo-in-eye-guide-dog-meme-600x466.jpg",
                     "https://preview.redd.it/ffnpor4qbjm61.jpg?width=640&crop=smart&auto=webp&s=38d70d75c05f1a0edb9be79864e1ca58f654f8cc",
                     "https://im.indiatimes.in/content/itimes/photo/2016/Aug/5/1470375976-indian-tv-memes-sakshi-tanwar-as-a-bahu.jpg",
                     "http://pm1.narvii.com/7412/26ff708a6494a1438bf006cf288b37cd65015b8ar1-750-995v2_uhq.jpg",
                     "https://techcommunity.microsoft.com/t5/image/serverpage/image-id/364840iE5DAE8BCD2C08C10/image-size/medium?v=v2&px=400",
                     "https://st1.bollywoodlife.com/wp-content/uploads/2018/12/jetha-1.jpg?impolicy=Medium_Resize&w=1200&h=800",
                     "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-02/sub-buzz-2780-1501675431-8.png?output-quality=auto&output-format=auto&downsize=640:*",
                     "https://images.thequint.com/thequint%2F2022-02%2F6f35c499-e44a-4459-9807-54035abc2774%2FScreenshot_2022_02_10_at_12_18_28_PM.png"]

            # COMEDY
            list2 = ["https://i.pinimg.com/originals/c6/21/72/c62172c5234602861377c1c08e2b4d9e.gif",
                     "https://www.memesmonkey.com/images/memesmonkey/38/38e21fc0ab8abc30bd1a5127ce5b8e01.jpeg",
                     "https://simg-memechat.s3.ap-south-1.amazonaws.com/9KWtPFE1rGNjoaPO4h7ibXlla9F3YH2291041.jpg",
                     "https://www.scrolldroll.com/wp-content/uploads/2022/01/best-memes-on-exams-03.png",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC57mSGog_BZBBGYK9mYo4mjbNb1np8gkCiA&usqp=CAU",
                     "https://qph.cf2.quoracdn.net/main-qimg-10710a4815b4fdc9659501fc9b290a23.webp",
                     "https://i.pinimg.com/736x/84/93/24/8493249ebd7168416a39143f0f9f4e45.jpg",
                     "https://filmdaily.co/wp-content/uploads/2021/04/bestfriends_lede.jpg",
                     "https://www.liveabout.com/thmb/Zgk_8zg-PYzx1Tb5U-RZYPZMxtQ=/750x670/filters:no_upscale():max_bytes(150000):strip_icc()/AvengersMemes19-b290903f8d8a47118f3ef98f4dcd8bb7.jpg",
                     "https://static.wikia.nocookie.net/1e371388-62a7-48dc-8d95-e46dc16c8c8e"]
            
            st.markdown(""" <style> .question_font {color: yellow} </style> """, unsafe_allow_html=True)
            
            
            st.markdown('<h1 class="question_font">YOU LAUGH, YOU LOSE</p>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with st.container():
                with col1:
                    link = random.choice(list1)
                    st.image(link, width=300)

                    if(st.button('HAHAHA')):
                        st.session_state.comedy += 1

                with col2:
                    link = random.choice(list2)
                    st.image(link, width=300)

                    if(st.button('HEHEHE')):
                        st.session_state.drama += 1






        elif choose == 'RESULTS':
            st.markdown(""" <style> .question_font {
            font-size:24px ; font-family: 'Clarendon'; border-radius: 5px; padding:10px; text-align: center; color: #FF9633; background-colour: pink} 
            </style> """, unsafe_allow_html=True)
            
            
            #STYLE
            st.markdown(""" <style> h3 {
             text-align: center; } </style> """, unsafe_allow_html=True)
                
            st.markdown(""" <style> img {
             width: 300px; height: 300px } </style> """, unsafe_allow_html=True)
            
            
            st.markdown('<h1 class="question_font">RESULT TIME!</p>', unsafe_allow_html=True)
            sort_results = [st.session_state.thriller,st.session_state.animation, st.session_state.romance, st.session_state.family, 
                            st.session_state.scifiction, st.session_state.action, st.session_state.drama, st.session_state.comedy]
            
            my_dict = {"THRILLER": st.session_state.thriller, "ANIMATION": st.session_state.animation, "ROMANCE": st.session_state.romance, 
                       "FAMILY": st.session_state.family,"SCIFICTION": st.session_state.scifiction, "ACTION": st.session_state.action,
                       "DRAMA": st.session_state.drama,"COMEDY": st.session_state.comedy}
            
            sorted_dict_items = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)
            sort_results.sort()
                
            i=0
            top_genre_list=[]
            while i<3:
                x=sorted_dict_items[i][0]
                top_genre_list.append(x)
                i+=1
            
            poster_link=""
            movie_name=""
            
            #FUNCTION TO RECOMMEND MOVIES BASED ON USER REPLIES
            def get_movies(top_genre_list):
                maxi=0
                #sum_score=0
                for id in quiz.index:  
                    sum_score=0
                    for genre in top_genre_list:
                        sum_score+= quiz[genre][id]
                        
                        if(sum_score>maxi):
                            maxi=sum_score
                            poster_link=quiz['LINK'][id]
                            movie_name=quiz['NAME'][id]
                return poster_link, movie_name
                        

            poster_link, movie_name= get_movies(top_genre_list)
            
            with st.container():
                col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                col2.image(poster_link,use_column_width=True)
                st.subheader(movie_name)   
                with st.expander("PLAY THE TRAILER"):
                    yt_link = play_yt_video(movie_name)
                    st.video(yt_link)
            
            profile_data(poster_link,1)
                
            
            
            
            
    elif choose == 'Map':
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633; text-align:center;} 
        </style> """, unsafe_allow_html=True)
        
        
        st.markdown('<h1 class="font">INDIAN MAP</p>', unsafe_allow_html=True)
        
    
        st.write('Click upon different states to get regional movie recommendations.')
        
        #FUNCTION TO MAKE CLICKABLE STATES IN INDIAN MAP USING HTML IMAGE MAPS TAG
        def indian_map():
            return """
            <img src="https://nriol.com/images/india_state_map.png" alt="Workplace" usemap="#workmap">

            <map name="workmap">
              <area shape="poly" coords="236,151,252,157,264,174,259,183,256,193,252,199,237,197,229,199,
              225,187,218,180,210,178,207,166,206,158,210,152,230,146"
              alt="Uttarakhand"  href="https://timesofindia.indiatimes.com/etmoviedetaillisting/61182603.cms">
              
              <area shape="poly" coords="204,570,220,569,233,564,247,561,254,551,259,566,253,584,250,602,
              251,622,235,633,229,653,210,665,192,680,192,635,184,619,175,604" 
              alt="Tamil Nadu" href="https://www.imdb.com/india/top-rated-tamil-movies/">
              
              <area shape="poly" coords="69,294,84,295,101,303,115,321,125,330,126,342,123,353,118,365,116,
              374,118,387,106,390,98,393,82,363,76,375,66,381,50,381,34,369,20,350,25,333,13,320,11,309,14,304"
              alt="Gujarat" href="https://www.imdb.com/list/ls020229870/">
              
              <area shape="poly" coords="270,369,288,349,296,333,289,317,302,310,320,313,331,318,339,331,341,
              345,331,359,318,378,308,399,299,412,299,429,285,445,278,456,268,438,261,424" 
              alt="Chattisgarh" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=hne">
              
              <area shape="poly" coords="36,231.00000762939453,54,217.00000762939453,86,219.00000762939453,108,
              190.00000762939453,121,173.00000762939453,140,191.00000762939453,157,209.00000762939453,167,
              221.00000762939453,186,222.00000762939453,188,261.00000762939453,184,295.00000762939453,164,
              307.00000762939453,140,305.00000762939453,120,327.00000762939453,78,296.00000762939453,58,284.00000762939453,44,261.00000762939453" 
              alt="Rajasthan" href="https://en.wikipedia.org/wiki/List_of_Rajasthani-language_films">
              
              <area shape="poly" coords="134,572.0000076293945,148,593.0000076293945,159,619.0000076293945,
              172,641.0000076293945,176,663.0000076293945,191,673.0000076293945,195,650.0000076293945,188,
              629.0000076293945,167,600.0000076293945,156,588.0000076293945" 
              alt="Kerala" href="https://www.imdb.com/india/top-rated-malayalam-movies/">
              
              <area shape="poly" coords="147,475,165,465,180,454,197,442,197,457,196,481,189,500,182,522,188
              ,538,204,546,218,555,202,572,196,591,176,599,162,591,143,574,132,557,128,535,123,510,130,481" 
              alt="Karnataka" href="https://www.imdb.com/list/ls041049290/">
              
              <area shape="poly" coords="216,490,233,482,247,474,268,465,300,449,316,439,336,427,350,430,336,
              445,306,469,286,486,268,502,254,517,258,535,260,551,248,553,228,563,218,556,200,545,195,531,178,519,194,498"
              alt="Andhra Pradesh" href="https://www.imdb.com/india/top-rated-telugu-movies/">
              
              <area shape="poly" coords="128,489.00001525878906,142,474.00001525878906,158,463.00001525878906,183,453.00001525878906,197,440.00001525878906,
              208,423.00001525878906,222,413.00001525878906,244,417.00001525878906,262,423.00001525878906,266,403.00001525878906,262,383.00001525878906,254,
              370.00001525878906,224,370.00001525878906,196,371.00001525878906,178,373.00001525878906,155,371.00001525878906,130,360.00001525878906,122,
              374.00001525878906,116,389.00001525878906,98,402.00001525878906,92,412.00001525878906,93,435.00001525878906,97,463.00001525878906,106,495.00001525878906" 
              alt="Maharastra" href="https://www.imdb.com/list/ls052798925/">
              
              <area shape="poly" coords="332,231.00001525878906,352,240.00001525878906,378,247.00001525878906,408,
              253.00001525878906,418,274.00001525878906,414,284.00001525878906,396,295.00001525878906,370,295.00001525878906,
              355,304.00001525878906,337,303.00001525878906,325,281.00001525878906" 
              alt="Bihar" href="https://www.imdb.com/list/ls090204907/">
              
              <area shape="poly" coords="128,175.00000190734863,132,157.00000190734863,147,149.00000190734863,144,134.00000190734863,162,125.00000190734863,166,
              135.00000190734863,174,141.00000190734863,183,151.00000190734863,183,163.00000190734863,172,175.00000190734863,162,179.00000190734863" 
              alt="Punjab" href="https://www.imdb.com/list/ls066141330/">
              
              <area shape="poly" coords="167,217.00001525878906,158,209.00001525878906,149,190.00001525878906,133,181.00001525878906,162,181.00001525878906,178
              ,170.00001525878906,197,173.00001525878906,194,205.00001525878906,198,218.00001525878906,193,228.00001525878906"
              alt="Haryana" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=bgc">
              
              <area shape="poly" coords="468,259,482,257,506,254,518,260,514,271,473,273,461,271" 
              alt="Meghalaya" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=kha">
              
              <area shape="poly" coords="462,260,458,252,460,241,476,241,489,239,506,237,530,227,544,217,554,209,576,199,582,210,560,226,
              549,237,545,248,537,254" alt="Assam" href="https://www.imdb.com/list/ls093032155/">
              
              <area shape="poly" coords="526,288.00000190734863,533,276.00000190734863,536,269.00000190734863,540,261.00000190734863,553,259.00000190734863,
              561,257.00000190734863,562,267.00000190734863,562,277.00000190734863,559,283.00000190734863,555,292.00000190734863,545,293.00000190734863,538,295.00000190734863" 
              alt="Manipur" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=mni">
              
              <area shape="poly" coords="435,359,444,358,449,354,448,345,446,337,445,324,439,315,436,307,427,296,427,286,432,279,436,274,
              429,265,428,256,441,252,449,253,448,241,434,234,423,234,418,261,417,276,417,300,412,306,406,310,397,312,390,317,383,321,378,323,399,341,405,350,414,359" 
              alt="West Bengal" href="https://www.imdb.com/list/ls021587889/">
              
              <area shape="poly" coords="4286,450,290,442,299,429,303,419,299,407,308,406,312,400,308,392,309,381,318,376,326,373,329,366,
              331,351,340,348,352,347,367,352,383,352,387,345,398,350,412,360,404,374,401,388,395,395,371,404,366,412,354,424,333,425"
              alt="Odisha" href="https://www.imdb.com/search/title/?languages=or&sort=user_rating">
              
              <area shape="poly" coords="199,492,194,486,197,477,195,468,199,462,199,452,200,442,201,436,205,431,204,425,209,422,216,
              418,218,408,228,415,236,414,246,415,249,422,257,433,267,437,273,448,279,455,272,462,224,488"
              alt="Telangana" href="https://www.imdb.com/india/top-rated-telugu-movies/">
              
              <area shape="poly" coords="110,500,112,509,116,517,122,518,123,513,124,507,121,503"
              alt="Goa" href="https://www.imdb.com/search/title/?title_type=feature&primary_language=kok">
             
            </map>
            """
        st.markdown(indian_map(), unsafe_allow_html=True)
            
        
        
        
        
        
        
    elif choose == 'Profile':
        
        st.markdown(""" <style> .result_font {
            font-size:40px ; font-family: 'Cooper Black'; text-align: center; color: #FF9633; background-colour: pink} 
            </style> """, unsafe_allow_html=True)
            
        st.markdown('<h1 class="result_font">RESULT TIME!</p>', unsafe_allow_html=True)
            
        #STYLE
        st.markdown(""" <style> h3 {
         text-align: center; } </style> """, unsafe_allow_html=True)
            
        st.markdown(""" <style> img {
         width: 300px; height: 300px; border-radius:10px; border: 10px solid lightgray;
         } </style> """, unsafe_allow_html=True)
        
        
            
        st.subheader("YOUR TOP MOVIE RECOMMENDATION RESULTS:")
        if(len(st.session_state.profile_content_recommendations)==0):
            st.warning("SEARCH SOME MOVIES IN CONTENT RECOMMENDATION SECTION TO CONTINUE")
            
        else:
            key=0
            while key<len(st.session_state.profile_content_recommendations):
                with st.container():
                    col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                    col2.image(st.session_state.profile_content_recommendations[key]["link"],use_column_width=True)
                key+=1
                
                
        st.subheader("YOUR TOP BUZZFEED MOVIE RECOMMENDATION RESULTS:")
        if(len(st.session_state.profile_buzzfeed_recommendations)==0):
           st.error("ATTEMP SOME QUESTIONS IN THE BUZZFEED SECTION TO CONTINUE")
       
        
        else:
           key=0
           while key<len(st.session_state.profile_buzzfeed_recommendations):
               with st.container():
                   col1, col2, col3 = st.columns([0.2, 0.2, 0.2])
                   col2.image(st.session_state.profile_buzzfeed_recommendations[key]["link"],use_column_width=True)
               key+=1
                
        

if __name__ == '__main__':
    main()
