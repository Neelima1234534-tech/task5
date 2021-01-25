
Finally:
   In programming, there may be some situation in which the current method ends up while handling some exceptions. 
But the method may require some additional steps before its termination, 
like closing a file or a network and so on.
So, in order to handle these situations, Python provides a keyword finally,
which is always executed after try and except blocks.
The finally block always executes after normal termination of try block or 
after try block terminates due to some exception.