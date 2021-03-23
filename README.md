# [HDU-CT] Computational Process Organization-Lab.1  (Spring 2021)
## Group name and list of group members
*group name:* Iron Five 

*list of group members* 

+ Chen yuxing
+ Li sicheng

## laboratory work number  
Laboratory 1. Different approach for algorithms and data structure implementation
## Variant description 
Set based on hash-map (collision resolution: separate chaining, link)
+ You can use the built-in list for storing buckets and a bucket itself
+ You need to check that your implementation correctly works with None value.
## Synopsis

In this lab, we implemented two versions of the hash table, and proved our implementation is correct through testing. 

Next, we will introduce the content of this lab from four aspects.

+ Contribution summary for each group member 
+ Explanation of taken design decisions and analysis
+ Compare mutable and immutable implementation
+ Conclusion
### Contribution summary for each group member 
Chen yuxing finished the mutable parts and corresponding testing, Li sicheng finished the immutable parts and corresponding testing.

 Here is the git log: 

 ### Explanation of taken design decisions and analysis  

A hash table uses a hash function to compute an *index*, also called a *hash code*, into an array of *buckets* or *slots*, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. 

So we  decide to use a list of lists to achieve the hash-map.  Using the hash function that python provided, we can put the key into hash function, calculate the index of the item, then put this item into the indexed list, if other item has the same hash value, it will be append to the indexed list. During the lookup, search every items in the indexed list.

### Work demonstration 

First, you should install the test packages using command pip install hypothesis.

Then, run the test with command  

The following is a description of the methods in the hash table.

The mutable version of functions are class functions, after an object implement the method, the process will change the original object(some functions, not all functions).

Here is the mutable functions description:

+  `hash(self,key)` :  Put item's key into the hash function. 

+ `size(self)` :  Return the hash-map's size.

+ `find(self,func)` : func is a function return bool value, it will search all items, add the qualified item into the result list.

+ `filter(self,func)`: func is a function return bool value, it will remove items which are not qualify.

+ `map(self,func)`:  func is a function which will be implement to all items' values.

+ `reduce(self,func,initial_state)`: The func will always take the initial_state and item's value as parameters, to do some calculations like sum up all the numbers.

The immutable version of functions are just simple functions. The parameters of the method are the hash map object and some necessary parameters. The immutable version is implemented by deep copy. It does not modify the passed source object, but first copies the source object through deep copy and then performs the operation, thereby achieving immutability.

Here is the immutable functions description:

+  `cons(hash_map, key, value)` :  Add a key-value set to the hash map. 
+  `remove(hash_map,key)` :  Remove a key and it's value.
+  `size(hash_map)` :  Return the size of the hash map.
+  `from_list(hash_map, list)` :  Add elements of the list to the end of the hash map.
+  `to_list(hash_map)` :  Convert the hash map to a list.
+  `find(hash_map, is_satisfied)` : is_satisfied is a function return bool value,it will judge if the elements in hash map meet the condition we set.  This function will search all items in hash map, add the qualified item which satisfy the condition we set into the result list and return it.
+  `filter(hash_map, is_filtered)`: is_filtered is a function return bool value, it will judge whether the elements in the hash table meet the filtering condition we set. This method will delete the elements that meet the condition and return the remaining elements.
+  `map(hash_map, func)`:  func is a function which will change the value in the hash map. This function will change all items in the hash map by func function.
+  `reduce(hash_map, func, initial_state)`: The func function defines the operation performed on two elements in the hash map. This function can do some calculations like sum up all the values in the hash map with the func function.
+  `mconcat(hash_map_A,hash_map_B)`: Combine two hash maps A and B
###  Conclusion 

In this lab, we first understood the basic concepts and principles of the data structure that we need to implement, and then chose a specific implementation method to implement it(by using a list of lists). Finally, we implemented two versions of the hash table, that is, variable Version and immutable version, and tested to prove that our implementation is reliable and can run stably.