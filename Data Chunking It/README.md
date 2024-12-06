<h1>Data Chunking It</h1>
In this file there are various ways to Data Chunk it from a wiki-dumps for building your AI. I personally have never done this. So I explored how to do it.
One folder is the testing folder, where I am testing different ways to do it called : "Try Chunking It!" <br>
Once I structured my backend, and how I wanted it stored in my collection for ChromaDB, that code is in the file, "The Chunking I choose!"

<h4>Whats the most important thing about doing this?</h4>
What most don't know going into this build, is choosing the right code editor that can handle large data chunking. EMAC's literally is the only one for this job. My Emacs is "GNU Emacs 27.1 x86_64-pc-linux-gnu version 1.16.0".<br>
Emacs Link is below:<br>
https://www.gnu.org/software/emacs/
<br>
Juypter or any "notebook" will crumble under this kind of processing, even if you tried to stream it to minimize the loading, it will still not work. (I tried it, I am spoiled on notebooks myself.)
<br>
I am running this threw a command line, with jupyter, that I built a pyspark environment inside of so the streaming is sortive being done. Pyspark was built through Apache Spark installation on jupyter. All inside the command line on Ubuntu OS.<br>
Links to do this are below:<br>
https://www.virtono.com/community/tutorial-how-to/how-to-install-apache-spark-on-ubuntu-22-04-and-centos/
<br>
https://medium.com/@patilmailbox4/install-apache-spark-on-ubuntu-ffa151e12e30<br>
https://medium.com/@agusmahari/pyspark-step-by-step-guide-to-installing-pyspark-on-linux-bb8af96ea5e8
<br>
<br>
<b>Please note linux os is picky, and you will encounter many bugs getting this environment set up, as I did, may not even be the same bugs, but work threw it! </b>

<h4>Chunking by stages in different sizes:</h4>
The first bit of Chunking was done in element trees by size still keeping parameters accurate. That gave me 5 Chunks.<br>
<b>Please Note:</b>  that your bash commands and your spark parameters must be tuned to your hardware specs, or you will get java heap errors and run out of memory. Do not do any kind of buffering, that will cause memory issues as well.
<br>
The final break of Chunking was by "Namespace" and "Subject" to produce KB sized data chunks that I can analyze on Jyputer Notebook, so I can clean it, encode it and start to build the ontology with the data per subject for the Furby.
What some of the command lines look like running it threw Ubuntu OS, with personal config hardware: <br>
<b>(pyspark_env)jessica@jessica-z690-UD-AX-DDR4:"~/Documents/GitHub/Furby_Hack$ spark-submit smaller_xml_chunks.py</b><br>
The reason it is chunked twice, is to ensure data integrity and schema integrety and that the tree's hold integrity per page. It is hard to see that or check back on that if you do not have a seperate file to check it with. This overall performance produced 464 xml files.
