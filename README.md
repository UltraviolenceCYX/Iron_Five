# [HDU-CT] Computational Process Organization  (Spring 2021)
## Group
*name:* Iron Five 

*team members:* 

+ Chen yuxing
+ Li sicheng

## Laboratory 1  
Different approach for algorithms and data structure implementation
## Variant description 
Set based on hash-map (collision resolution: separate chaining, link)
+ You can use the built-in list for storing buckets and a bucket itself
+ You need to check that your implementation correctly works with None value.
## Content 
+ Contribution summary for each group member 
+ Explanation of taken design decisions and analysis
+ Compare mutable and immutable implementation
+ Conclusion

### Contribution summary for each group member 
Chen yuxing finished the mutable parts and corresponding testing, Li sicheng finished the immutable parts and corresponding testing.

 here is the git log: 

 ### Explanation of taken design decisions and analysis  

A hash table uses a hash function to compute an *index*, also called a *hash code*, into an array of *buckets* or *slots*, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. 

So we  decide to use a list of lists to achieve the hash-map.  Using the hash function that python provided, we can put the key into hash function, calculate the index of the item, then put this item into the indexed list, if other item has the same hash value, it will be append to the indexed list. During the lookup, search every items in the indexed list.

### Compare mutable and immutable implementation 

The mutable version of functions are class functions, after an object implement the method, the process will change the original object(some functions, not all functions).

Here is the mutable functions description:

+  `hash(self,key)` :  put item's key into the hash function. 

+ `size(self)` :  return the hash-map's size.
+ `find(self,func)` : func is a function return bool value, it will search all items, add the qualified item into the result list.
+ `filter(self,func)`: func is a function return bool value, it will remove items which are not qualify.
+ `map(self,func)`:  func is a function which will be implement to all items' values.
+ `reduce(self,func,initial_state)`: the func will always take the initial_state and item's value as parameters, to do some calculations like sum up all the numbers.

	The immutable version of functions are just simple functions, the input parameter will just be a reference, after the process it will not change the original object.

###  Conclusion 
The hash-map we created is working just as we excepted.