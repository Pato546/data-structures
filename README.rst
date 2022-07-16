DATASTRUCTURES
**************
This repository is a python implementation of common **datastructures**

DataStructures Implemented
==========================

**Stack**
---------
A *Stack* is a collection of objects that are inserted and removed according to the *last-in*, *first-out* (**LIFO**)
principle. A stack can be implemented by means of an **array**, **structure**, **pointer** and **linked list**. Stack
may have fixed size or it may have a sense of dynamic resizing which is heavily dependent on how the stack was
implemented. The stack datastructure support **two(2)** fundamental operations:
    #. **push**: Adds elements to the top of the **Stack**
    #. **pop**: Removes elements from the top of the **Stack**

**Applications of Stacks**
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Internet Web browsers store addresses of recently visited sites in a stack. Each time a user visits a new site, that
site's address is **pushed** onto the stack of addresses. The browser then allows the user to **pop** back to previously
visited sites using the back button.

2. Text Editors usually provide an undo mechanism that cancels recent editing operations and reverts to former states of
document. This undo operation can be accomplished by keeping text changes in a stack.

3. Stacks can be used to check parenthesis matching in an expression.

4. Processing function calls.

5. Reversing of data.