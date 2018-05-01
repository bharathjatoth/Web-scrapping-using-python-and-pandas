# Web-scrapping-using-python-and-pandas
Using BeautifulSoup to Extract the text into paragraphs or embedded each paragraph into a list
In this we have all the types of data like excel, word, html, pptx and parsing these data into mongodb database
These webscrapping extract the data even from the tables and place according under the headers.
The Structure of the directory is as follows
 Open Text-extract you will have four parsers (pptx) will be added in a day
1) word_parser (deals with word docs including tables)
2) excel_parser (deals with excel worksheets using pandas)
3) html_parser (deals with the html and extracts text using Beautiful Soup and pandas including tables)
# Upcoming
We serach the text from the elastic search and convert the data into json format

write_word_file.py:

In this we write the output of the program to the word document dynamically. For static you can visit word_static.py with pydocx. 
1) Insert a Mailmerge field in the document/ template where you want to populate the data. (creating a mail merge field: Open a Word doc-> Insert ->Quickparts(click)->Field->MergeField(from field Names)->Give a field name(ex:question in out document)) 
2) After inserting a Mailmerge field just runt the above code so that it populates text in the specified location.
3) For tables, First Create a table and in the cell create a Merge Field as explained above in point 1., and populate the text.
4) The above code is for populating into the tables. This dynamically created the number of rows and you can also pass the json objects to write into it
