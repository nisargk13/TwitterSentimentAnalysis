# Twitter Sentiment Analysis
In this project, I have analysed tweets of 45th president of USA, Donald Trump.  The sentiment of tweets is divided into three parts. 
       
         Positive, 
         Negative, 
         Neutral.

Here, I have used Google colab (Jupyter notebook is also works).

##	Libraries used:

**Tweepy**

  - Tweepy is a Python library for accessing the Twitter API. It is useful to get tweets from timeline. Follow and unfollow user. Create and delete tweets. For that you need twitter developer account.

**Pandas** 
  - Pandas stands for “Python Data Analysis Library”.  It is useful for data manipulation, analysis, and cleaning. 

**Numpy** 
  - Numpy is useful for adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

**Re (Regular expression) and WordCloud**

**TextBlob**
  - TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

**Matplotlib** 
  - Matplotlib is a basic library that enables many other libraries to run and plot on its base including seaborn or wordcloud.
  
  
## Steps for creating Developer Account in Twitter

First, I generated Twitter API credentials (Consumer Key, Consumer Secret, Access Token and Access Token secret).  For this I have created twitter developer account and created new application. 
1.	Use this link to create developer account. ( https://developer.twitter.com/ ). After applying for developer account, this Screen will be there. If you already have some applications, then it will show list of applications in place of No apps here.


   ![Welcome_Page](https://user-images.githubusercontent.com/60724707/84947571-6bf65c00-b0b8-11ea-8713-df1558c71204.png)
   
   
 
2.	In the next phase you have to add some details of Application. Such as App Name(required), App description(required), Website URL(add github link) , and How app will be used(You can write any thing). No need too fills other details.



   ![Welcome_3](https://user-images.githubusercontent.com/60724707/84947788-d27b7a00-b0b8-11ea-92c9-2521b6de4ee7.png)
   
   
   ![Welcome_2](https://user-images.githubusercontent.com/60724707/84947809-ddcea580-b0b8-11ea-9cbb-ec524aa702e6.png)


3.	After creating App, you will find this screen. For Consumer Api Keys and Access token api go to Keys and tokens.
   
   
    ![Welcome_4](https://user-images.githubusercontent.com/60724707/84947833-e7580d80-b0b8-11ea-86ac-47e31837d08d.png)


 
## Result Screenshots

1.  Before data cleaning process, last 5 tweets made by President Trump.


![1_1](https://user-images.githubusercontent.com/60724707/84949524-61899180-b0bb-11ea-90fa-babc8b4adbd9.png)


2.  After Cleaning data (Removed unnecessary hyperlink and user names from tweets)


![2_2](https://user-images.githubusercontent.com/60724707/84949756-b62d0c80-b0bb-11ea-9d1d-9afacbcc87a0.png)


3.  Using TextBlob library, added Subjectivity and Polarity of tweets.


![3_3](https://user-images.githubusercontent.com/60724707/84949992-23d93880-b0bc-11ea-94d6-667512973eed.png)


4.  Plotted a wordcloud of size 500*300. 


![4_4](https://user-images.githubusercontent.com/60724707/84950245-9a763600-b0bc-11ea-8f98-c28c871ff090.png)


5.  On the basis of Polarity, tweets are divided into Positive, Negative ane Neutral.


![5_5](https://user-images.githubusercontent.com/60724707/84950528-11abca00-b0bd-11ea-8030-2d62263a4032.png)


6.  Positive, Negative and Neutral tweets. 


![6_6](https://user-images.githubusercontent.com/60724707/84951150-04dba600-b0be-11ea-8903-7d7770bf268d.png)


7.  Plotted scatter plot of Subjectivity V/S Polarity


![7_7](https://user-images.githubusercontent.com/60724707/84951476-7ae00d00-b0be-11ea-8136-174b3356aa7f.png)


![10_10](https://user-images.githubusercontent.com/60724707/84951786-ecb85680-b0be-11ea-9cb6-46f8bdd75e68.png)

