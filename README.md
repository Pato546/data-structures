# DATASTRUCTURES

This repository is a python implementation of common **datastructures**

## DataStructures Implemented

<details>

  <summary> Stack </summary>

A **Stack** is a collection of objects that are inserted and removed according to the _last-in_, _first-out_ (**LIFO**)
principle. A stack can be implemented by means of an **array**, **structure**, **pointer** and **linked list**. Stack
may have fixed size or it may have a sense of dynamic resizing which is heavily dependent on how the stack was
implemented. The stack datastructure support **two(2)** fundamental operations:

- `push`: Adds elements to the top of the **Stack**
- `pop`: Removes elements from the top of the **Stack**

#### Applications of Stacks

1. Internet Web browsers store addresses of recently visited sites in a stack. Each time a user visits a new site, that
   site's address is **pushed** onto the stack of addresses. The browser then allows the user to **pop** back to previously
   visited sites using the back button.

1. Text Editors usually provide an undo mechanism that cancels recent editing operations and reverts to former states of
   document. This undo operation can be accomplished by keeping text changes in a stack.

1. Stacks can be used to check parenthesis matching in an expression.

1. Processing function calls.

1. Reversing of data in a collection.

#### Example (Parenthesis mathing in an expression)

```python
from linked_list.stack import LinkedStack, ArrayStack

def match_parenthesis(expr: str) -> bool:
  """Checks if parenthesis matches in an expression

  Args:
    expr (str): expression to check.

  Returns:
    bool: `True` if parenthesis matches and `False` if not.

  """

  left: dict = {"{": 0, "(": 1, "[": 2}
  right: dict = {"}": 0, ")": 1, "]": 2}

  stack = LinkedStack() # you can equally use ArrayStack()

  for delimeter in expr:
    if delimeter in left:
      stack.push(delimeter)
    elif delimeter in right:
      if len(stack):
        if left.get(stack.pop()) == right.get(delimeter):
          continue
        else:
          return False

      else:
        return False

  return True

```

</details>
