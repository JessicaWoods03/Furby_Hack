<h1>Furby Hack</h1>

<img width="150" alt="Screenshot 2024-01-19 at 5 44 27 PM" src="https://github.com/JessicaWoods03/Furby_Hack/assets/48572600/5b32e71a-8b3d-4d74-b2c4-89a386e456e7"><br>
In this work, I will be building several functions for the Furby in different neural networks. The first one I am working on in Python, is the function of speech, response. The neural networks will work through different microcontrollers to test and respond to before integrated into the Furbies robotic form. That is currently completely stripped. To be fair this is a Chebbacca Furby. <br>
Personally I love Star Wars and I love Furbies!<br>

Raspberry Pi recently came out with a Pi Zero 2 W. The board specs are phenominal and you can read those here.  https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ This is the board I will use to begin working on the Furby's brain. I call it a brain, but in all reality it is a AI I am developing to integrate into the Furby.
<h3><b>Part One of the Furby Brain<br></b></h3>
<h4></b>Understanding and Interpreting the Natural Language</h4><br>

<img width="900" alt="Screenshot 2024-01-19 at 6 41 53 PM" src="https://github.com/JessicaWoods03/Furby_Hack/assets/48572600/3cfe6cde-d5bf-42a5-8b27-b8cec4b13a15"><br>

Learning Distribution Symantics is no easy task with creating the first neural network for speech and response. Distribution Symantic modeling is an interesting take on words. You can find details of Distribution Symantic Modeling on Wikipedia https://en.wikipedia.org/wiki/Distributional_semantics . Its a entirely different approach than the sensor of photo recognition. There are many scholar writings I have been combing through such as this one "Distributional semantic modeling: a revised technique to train term/word vector space models applying the ontology-related approach." by Vitalii Velychko<br> https://www.researchgate.net/publication/339713296_Distributional_semantic_modeling_a_revised_technique_to_train_termword_vector_space_models_applying_the_ontology-related_approach 
He explores a reasonably interesting Library in Python that I will begin working with, Vec2graph -- a Python library for visualizing word embeddings (term embeddings in my case) as dynamic and interactive graphs. This is also being explored by Cornell University and a few other scholars. It is a good read on how words explored. I also have the PDF loaded into the "Furby Resource" Folder above if you want to have easy access to that information. This further's my journey into building a RNN network. Reccurent Neural Network, LSTM Long term short memory. This uses attention mechanism to catch importance in phrases from Natural Language inputs. You can read more about that in this link. https://www.mdpi.com/2073-8994/13/2/214#B12-symmetry-13-00214
Considering I have never done this before, I am going to start following this approach as a base set up. Part one says to create a Dataset using a large wikipedia data dump set, with Python Gensim to parallelize and process the dump. I need storage off site from my computer because that dump is huge.<br> ((Hardware needed))<br>
NVMe's are highly suggested for hardware and the site for Wikipedia to do the dump download is listed below:
(https://en.wikipedia.org/wiki/Wikipedia:Database_download)
Before I can do the code to sort threw the dump, I needed to upgrade my Linux tower with more go juice in the hardware, its not the recommended hardware, but the stats on this hardware is enough to do small tasks.
![geforcertx4060](https://github.com/JessicaWoods03/Furby_Hack/assets/48572600/acce7fde-e433-44a4-91a0-b290dbecd041)
NVME of 4TB<br>
GEFORCERTX 4060 Ti (its important to ensure you have atleast 16VRAM) <br>
I have been working on configuring these hardware specs before I begin working with the wikipedia dump, as to ensure the tower I have can handle the load.<br>
This would be minimium specs required for this project to get started, I am sure this will still be slightly slower, but once configured, optimizations will be made.
This is a process I hope no one minds following along with me. I will gladly share the steps as I walk threw them and the code to get this going.
Sorry I haven't worked on this in a while...personal things came up-<br>
Ok Hardware is set :) <br>
**Commmands on Linux to use to check GPU setup:<br>
nvidia-smi<br>
nvidia-smi dmon<br>
sudo apt install nvtop<br>
nvtop<br>

![updated](https://github.com/user-attachments/assets/989b78ac-31aa-4855-9ebc-4f4bdb09d241)

I am back at it now-
Next is configuring Apache Spark on Ubuntu for handling the xml files which are huge.<br>
PLS - don't use ChatGPT [[warning it will not work no matter what it tells you to do]]<br>
https://www.virtono.com/community/tutorial-how-to/how-to-install-apache-spark-on-ubuntu-22-04-and-centos/ <br>
-us that site it works.<br>
Wiki-dump site - <br>
https://dumps.wikimedia.org/enwiki/20240701/
<br>
enwiki-20240701-pages-meta-history1.xml-p1p812.bz2 2.4 GB <br>
enwiki-20240701-pages-meta-history1.xml-p813p1460.bz2 2.0 GB <br>
This is kind of hard to configure so I had to make sure that my tower specs were set properly to handle this much data. <br>
Total Memory: 62 GiB<br>
Used Memory: 4.2 GiB<br>
Free Memory: 40 GiB<br>
Total Swap: 15 GiB<br>
Used Swap: 0 B<br>
Bash: watch free -h<br>
Reached an big error with schemas in the xml chunk files. https://www.youtube.com/watch?v=aB_koPUNqfo this Youtube video helped with debugging the schemas of the namespace issues in building a element tree. <br>
<h3>Setting up the Vector Database:</h3>
I wanted to find a way to access large amounts of data efficiently in a vector database. I also miss opinions, in many of the AI sitcoms that has motivated me to build an opinion base on my AI even if it is a mock-up of random saved opinions, that are limited, due to storage limitations. My AI doesn't have to agree with the users opinion even if the opinion is drawn from the vector database as most relvant to the users input. Personally I am not a fan of 
agreeable people. I like K.I.T.T. from the 1970s...the AI car-
<img width="1071" alt="Screenshot 2024-09-05 at 8 44 43 PM" src="https://github.com/user-attachments/assets/b411411e-8d35-4518-a57e-de0f361e6c9c">
<img width="649" alt="Screenshot 2024-09-05 at 8 44 58 PM" src="https://github.com/user-attachments/assets/3760fc52-b885-47ca-893d-bf93e951b023">



<h3>Part Two of the Furby Brain</h3> 
This part is yet to be explored but hints on a few short cuts involve the possibility of a Pixy2 camera.

