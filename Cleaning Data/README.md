<h1>Cleaning and Extracting Key Data Points for ChromaDB</h1>
<img width="1029" alt="Screenshot 2024-12-11 at 3 53 44 PM" src="https://github.com/user-attachments/assets/5046052a-15e5-4a14-848d-4ed552c280c6" />
Working with key points for hierarchy data structure when confirming ontology and creating subclasses for more dynamic query's.
So with cleaning the data, we needed to learn what kind of structures I would find appropriet to use when moving data over to the ChromaDb. 
Its best to work firstly with Geo Data. It is the most complicated data structure. After about a week or more (plus holidays, I didn't work on this during 
the Christmas Holiday in December.) Node Graphs afford the luxery of having more than one parent. 
<br>
Some of the data I will be going threw might just be a node tree, with only one parent...but affording the luxery of having a node graph, gives the oppurtunity to capture all 
possiblilities.  <br>
Ontology is based on "relationships" if you are familiar with databases such as SQL or POSTGRE, this is a similar approach. SQL has relationships one-to-many, many-to-many, one-to-one, with Primary keys and foreign keys. In the data we are working with in ChromaDB, we are creating the same asthetics while also implimenting vector space. This gives the data a well distribution for ontology and sementanics. <br>
<img width="216" alt="Screenshot 2025-01-22 at 9 33 12 AM" src="https://github.com/user-attachments/assets/a2906ab0-74dd-4999-b63f-c053b74dcae2" /><br>
We define three relationships(we can create more, for now I will keep it simple):<br>
<b>Geographical<br>
Functional<br>
Comparison<br></b>
For example, if "Aalborg" is a "seaport" and you want it to be bidirectional, you can add both directions.
Defining these relationships gives the same oppurtunities as SQL's one-to-one, one-to-many and many-to-many. The Primary keys, and Foreign Keys are stored in the 'meta_data' as Parent_nodes and child_nodes. This is a great migration of using SQL properties inside a vector database for proper distribution. <br>
I beleive you can theoretically use this concept to compress SQL databases into vector storage spaces in ChromaDB if structured properly, this will give corporations who face large data issues for storage a bit of breathing space on paying for those in cloud. That is the ongoing scam with cloud users, is the ignorance behind actual investors.
From this point on handling data...it comes down to if you want to have a directional graph or a bidirectional graph when adding these to meta data. Below is a Youtube video of what the difference is in these node graphs:<br>
<img width="1012" alt="Screenshot 2025-01-22 at 10 43 01 AM" src="https://github.com/user-attachments/assets/a4725679-47aa-454d-a5c6-d93739be851a" />
https://www.youtube.com/watch?v=1oVuQsxkhY0

