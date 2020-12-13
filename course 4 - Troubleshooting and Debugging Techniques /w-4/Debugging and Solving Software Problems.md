# Debugging and Solving Software Problems

## Introduction 

You're a member of your company's IT department. A colleague that recently left the company wrote a program that's 90% complete; it's designed to read some data files with information on employees and then generate a report. It's up to you to finish the code -- this includes fixing any errors, bugs, and slowness that might be in the unfinished code.

## Improve performance

The program ```w-4-assigment.py``` will start processing the file but it takes a long time to complete. This is because the program goes slowly line by line instead of printing the report quickly. You need to debug why the program is slow and then fix it. In this section, you need to find bottlenecks, improve the code, and make it finish faster.

The problem with the script is that it’s downloading the whole file and then going over it for each date. The current script takes almost 2 minutes to complete for ```2019-01-01```. An optimized script should generate reports for the same date within a few seconds.

To check the execution time of a script, add a prefix "time" and run the script.

```shell
time ./test.py
```

In order to fix this issue, we are now modifying the ```get_same_or_newer()``` function to preprocess the file, so that the output generated can be used for various dates instead of just one.

Here are few hints to fix this issue:

- Download the file only once from the URL.

- Pre-process it so that the same calculation doesn't need to be done over and over again. This can be done in two ways. You can choose any one of them:
  - To create a dictionary with the start dates and then use the data in the dictionary instead of the complicated calculation.
  - To sort the data by start_date and then go date by date.
Choose any one of the above preprocessing options and modify the script accordingly.

The improved version is realized over ```w-4-assigment-improved.py``` script. 