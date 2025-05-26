---
---
# Data Structures for Technical Questions

<span style="font-size: 1.5em;"><b>Solving Tips for Data Structures</b></span>

Created:  26 May 2025

## Linked List
### Reverse a Linked List
Ok this is super easy and you've just gotta remember the steps.
For the sake of syntax think of this as the nodes staying in the same place but you're making the connections go from left&rarr;right to right&rarr;left
<span style="font-size: 26px;">The Steps:</span>
1. Define a new node that will be used to store the node to the left of the one you're dealing with. Set this to null
2. Iterate over the Linked List and at each point follow these steps:
	1. Save the node to the right in memory
	2. Update the outgoing link from the current node
	3. Save the current node as the left node for the next iteration
	4. Move the current node along to the right
3. Return the left node once you run off the right hand side

Thats:
1. Save right
2. Update link
3. Save current as left
4. Move to the right

```java
public ListNode reverseList(ListNode head) {
	ListNode leftNode = null;
	while (head != null){
		// save right
		ListNode rightNode = head.next;
		// reverse link
		head.next = leftNode;
		// save current for next iteration
		leftNode = head;
		// move to right
		head = rightNode;
	}
	return leftNode;
}
```

## Stack

### When to use
- When you have to process a linked list in reverse (iterate over it adding to stack and then pop from the top of the stack)
- When you have to move through an iterable and update it in some way that is not immediate (ie. you have to remember what to do when you encounter later elements)

## Binary Trees
### General Recursive Approach
- Pass down information that gives **lower** nodes the required info
- Pass up success or failure information
- Store global information above the recursive function. Have the recursive function return void and simply update the global variable in the function.
```java
int result;

public void recurse(TreeNode root, int params){
	if (root == null) return;
	// update result here
}
```

### Avoid making copies when passing down
The naive approach to passing down information that is unique to each node is to make a copy of the information (for example an array containing all of a node's parents).
This uses a lot of memory.
A better way of doing it is to backtrack, whereby you add the node's information to the data structure (ie. the array), do all the stuff you need within the recursive call and just before you pass the success or failure information up to the parent you remove the node's information from the data structure:

```java
public int recurse(root, info){
// base case
// add root to info
// check children
// set return value
// **remove root from info**
// return 
}

```

## Linked Lists
### Useful Techniques
#### Dummy Node
A dummy node can be useful at the start of a list if you have an algorithm that compares adjacent nodes.
It saves you from having to find the first instance of something to start your new linked list.

See [this solution](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solutions/6673690/eliminate-all-duplicates-from-sorted-list-ii-master-this-listnode-pattern-interviewers-love/?envType=problem-list-v2&envId=linked-list) and [my solution here](https://leetcode.com/problems/partition-list/?envType=problem-list-v2&envId=linked-list)for example of dummy node being used at the start of a linked list.

The general approach (that I've seen is):
- Set a dummy node, with next pointing to head or None
- This is the head (and maybe tail) of your new list
- Now iterate through the main list and connect the first good node to the dummy node
- This allows consistent behaviour when adding subsequent nodes to the list
- To return the true head later do dummy.next

#### Don't count
- Try not to count distances
- If, for example, you need to chop out a number of nodes rather than counting and chopping in one go at the end. Simply keep track of the previous node and attach it to each of the nodes you will end up chopping out as you traverse.

#### Work with nexts to avoid custom handling at the end
- Not 100% sure on the intuition here but stand back a node and look forward so that you don't have to have custom handling once you're out of the list. [This same solution](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solutions/6673690/eliminate-all-duplicates-from-sorted-list-ii-master-this-listnode-pattern-interviewers-love/?envType=problem-list-v2&envId=linked-list) shows the logic


