# [HDU-CT] Computational Process Organization-Lab.1  (Spring 2021)
## Group name and list of group members
*group name:* Iron Five 

*list of group members* 

+ Chen Yuxing
+ Li Sicheng

## laboratory work number  
4
## Variant description 
Set based on hash-map (collision resolution: separate chaining, link)
+ You can use the built-in list for storing buckets and a bucket itself
+ You need to check that your implementation correctly works with None value.
## Synopsis

In this lab, we implemented two versions of the set based on hash table, and proved our implementation is correct through testing. 

Next, we will introduce the content of this lab from four aspects.

+ Contribution summary for each group member 
+ Explanation of taken design decisions and analysis
+ Compare mutable and immutable implementation
+ Conclusion
### Contribution summary for each group member 
Chen yuxing finished the immutable parts and corresponding testing, Li sicheng finished the mutable parts and corresponding testing.

 Here is the git log: 
 ![](./fig/log.png)
 

 ### Explanation of taken design decisions and analysis  

A hash table uses a hash function to compute an *index*, also called a *hash code*, into an array of *buckets* or *slots*, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. 

So we  decide to use a list of lists to achieve the hash-map.  Using the hash function that python provided, we can put the key into hash function, calculate the index of the item, then put this item into the indexed list, if other item has the same hash value, it will be append to the indexed list. During the lookup, search every items in the indexed list.

After creating the hash table, we created a set which possesses a hash table and use it to store elements. The key in the hash table is the element itself and the value is an object.

### Work demonstration 

First, you should install the test packages using command `pip install hypothesis and pip install pytest`.

Then, just run the command `python ./src/Testcase/set_pytest.py` and we can see that the results are correct.

### Compare mutable and immutable implementation 


The mutable version of functions are class functions, after an object implement the method, the process will change the original object(some functions, not all functions).

The immutable version of functions are just simple functions. The parameters of the method are the set object and some necessary parameters. The immutable version is implemented by deep copy. It does not modify the passed source object, but first copies the source object through deep copy and then performs the operation, thereby achieving immutability.

###  Conclusion 

In this lab, we first understood the basic concepts and principles of the data structure that we need to implement, and then chose a specific implementation method to implement it(by using a list of lists to implement hash table and use it to implement a set). Finally, we implemented two versions of the set, that is, mutable version and immutable version, and tested to prove that our implementation is reliable and can run stably.