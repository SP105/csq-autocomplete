[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
![Version](https://img.shields.io/badge/version-1.0-blue) 


To test with a bigger datset, I download the following:
-  [WikiWords_FirstMillion_Refined_V6](https://www.kaggle.com/dataistic/wiki-words)

You can choose wich dataset will be used (by default use the list of keywords that are provide in the doc).

To run the project execute the followings docker commands.

````
docker build -t csq-autocomplete .
docker run -it csq-autocomplete
````

### Questions
> What would you change if the list of keywords was much larger (300 Gb) ? 
> Please explain and describe the concepts that would allow to handle this if you decide to use specific 
> tools (frameworks, databases…)

 If that is the case, using only an efficient search algorithm is not enough. To attack this problem we will need to partition
the data in order to have smaller chunks of data to analyze. We could arrange in partitions of the three first letters of the words and sort the file in a distributed database (or filesystem).
If three letters will still be lots of data, we could have more letters to the partitions. In anycase, we need to pre process the data and sort it in the most convenient way. 
Depending on the requirements we could use different tools. If response time will be on top, I will use some non-relational database like cassandra but if we need to analyze and keep the information for some batch processing I will use Spark with some distributed file system (s3, hadoop)

> What would you change if the requirements were to match any portion of the
keywords (for example, given the string “pro”, the program could suggest the
keyword “re pro be”) ?

If the requirement changes to be in any part of the word, having the data in partition is not enough. 
We will need some pattern-indexing over the data to speed-up the process of searching and some auxiliary structure 
(like search trees) to find the words.