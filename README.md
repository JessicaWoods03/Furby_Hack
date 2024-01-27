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
This is a process I hope no one minds following along with me. I will gladly share the steps as I walk threw them and the code to get this going.
<h3>Part Two of the Furby Brain</h3> 
This part is yet to be explored but hints on a few short cuts involve the possibility of a Pixy2 camera.

