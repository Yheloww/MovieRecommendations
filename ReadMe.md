<p align="center"> 
  <img src="./assets/BeCode_color.png" alt="Becode logo" width="250px">
</p>
<h1 align="center"> Movie Recommendation </h1>
<h3 align="center"> Becode project to learn Natural language processing and recommendation system </h3>

<p align="center"> 
  <img src="./assets/movies.png" alt="Sample signal" width="25%" height="25%">
</p>

<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Description"> ➤ Description</a></li>
    <li><a href="#Objectives"> ➤ Objectives</a></li>
    <ul>
        <li><a href="#Challenges"> Challenges</a></li>
        <li><a href="#Limitations">Limitations</a></li>
        <li><a href="#Further developments">Further developments</a></li>
      </ul>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#installation"> ➤ Installation</a></li>
    <li><a href="#usage"> ➤ Usage</a></li>
    <li><a href="#Results-and-discussion"> ➤ Results and Discussion</a></li>
    <li><a href="#Visuals"> ➤ Visuals</a></li>
    <!--<li><a href="#experiments">Experiments</a></li>-->
    <li><a href="#Timeline"> ➤ Timeline</a></li>
    <li><a href="#contributors"> ➤ Contributors</a></li>
  </ol>
</details>

<h2 id="Description"> :memo: Description</h2>
    <p align="justify"> 
    Small app about movie recommendation (the app is still in development) so for now it is just some python functions that needs to be implemented in an API. </p>

<h2 id="Objectives"> :dart: Objectives</h2>
    <p align="justify">  
     :radio_button: Use spacy to implement one extra feature, for example key-word extraction, sentiment analysis, or text summarization.</br>
     :radio_button: Explain which NLP methods can be used to compute similarities between texts (i.e. TD-IDF, cosine-similarity, etc.) and how they work in the big picture.</br>
     :radio_button: (Optional) Deploy your solution locally or in Render using Flask or Streamlit. </br>
    </p>
    <h3 id="Strenghs"> Strenghts</h3>
        <p align="justify"> 
         :radio_button: recommendation system based on other users ratings</br>
         :radio_button: keyword extraction using spacy</br>
         :radio_button: search functions based on title</br>
        </p>
    <h3 id="Limitations"> Limitations </h3>
        <p align="justify"> 
        :radio_button: Not enough time to deploy the app</br>
        :radio_button: API not complete</br>
        </p>
    <h3 id="Further Developments"> Further developments</h3>
        <p align="justify"> 
        :radio_button: Creation of an user interface (Deployement of an application) </br>
        :radio_button: The app will have a story based on the years and the different movies of the year</br>
        </p>

<h2 id="folder-Structure"> :file_folder: Folder structure</h2>
    <p align="justify"> 
    1. <b>/api</b>-folder contains the starting code for my API</br>
    2. <b>/App-reco</b>-folder that contains a sveltekit to develop the apllication further, right now it communicate with the API </br>
    3. <b>/notebook/</b>-folder that contains the notebook of explorations  </br>
    4. <b>/src/</b>-folder that contains the python files with the different implementations of recommendations alogrithms</br>
    </p>

<h2 id="installation"> :repeat: Installation</h2>
    <p align="justify"> 
    clone the repo on your machine </br>
    Activate an virtual environment in <b>Python 3.10</b> </br>
    then install the different dependecies mentionned in the requirement.txt
    </p>

<h2 id="Results-and-discussion"> :microscope: Results and discussions</h2>
    <h3 id="Optimization"> :ledger: Search function</h3>
            <p align="justify"> function that search the csv file and return how many films we want that have similarities to the title we entered. The function can be improved by using for exemple the overview of the movies to find movies with similar overviews
            </p>
    <h3 id="forecasting"> :chart_with_upwards_trend: Recommendation based on other users</h3>
            <p align="justify"> For this part i have used the cosine similarities to find movies that others users like me have liked. The idea behind recommendation based on others is that you have to find people with specific enough taste to be sure that it is a great movie to recommend. So we have to get rid of the movies that everybody have liked to do that. During this part I also had to merge the ratings.csv avec le moviemetadata.csv so I had to find the columns that matches togethers. 
            </p>
    <h3 id="together"> :key: Keyword extraction</h3>
            <p align="justify"> to make the keyword extraction code, I used the Spacy model for nlp. It was great so I extracted keyword for every movies planning to use them in my app. I also wanted to extract keyword per year to see wich keywords were the most used in each year, i still need to finish this part to get rid of the keywords that are always used to have more specific ones. 
            </p>


<h2 id="Timeline"> :calendar: Timeline</h2>
    <p align="justify"> 
    from the  17/04/23 to the 25/04/23 </br>
    10 days total
    </p>

<h2 id="Contributors"> :raising_hand: Contributors</h2>
    <p>Héloïse feldmann <a href="https://github.com/Yheloww">  Github account</a></p>