8.1. Syntax Errors
When writing code, it needs to follow a specific structure, called syntax. Syntax errors occur when the code structure is not correct. For example, forgetting to put a colon after a loop condition is a syntax error. The system points out where it noticed the error and stops running the code.

8.2. Exceptions
Even if the code's structure is correct (no syntax errors), problems can still occur when the code runs. These are called exceptions. For instance, dividing a number by zero is not allowed in mathematics, and if the code tries to do that, it will stop running and show an error message.

8.3. Handling Exceptions
To make programs more robust, developers can write code to handle exceptions gracefully. For example, if a program asks a user to input a number but the user enters a word, the program can catch that mistake and ask the user to try again instead of crashing.

8.4. Raising Exceptions
Sometimes, rather than waiting for something to go wrong, programmers intentionally create an error using the raise statement. This is useful for signaling that something unexpected has happened.

8.5. Exception Chaining
When one error is a direct result of another, you can chain them together to show that connection. For instance, if a program tries to open a file that doesn't exist, and an error occurs while trying to handle that, you can see a chain of errors showing how one led to another.

8.6. User-defined Exceptions
Programs can create their own types of errors called exceptions. This is useful when you want to handle specific situations differently. For example, if you're building a program to manage a library, you might create a custom exception for when a book is not available.

8.7. Defining Clean-up Actions
Sometimes, there are tasks that must be done regardless of whether an error occurs or not. The try and finally statements are used to define these clean-up actions. For example, if a program opens a file, the finally block can ensure that the file is closed properly, even if an error occurs.

8.8. Predefined Clean-up Actions
Certain objects, like files, have built-in mechanisms to ensure they are properly cleaned up after use. The with statement is introduced as a convenient way to work with such objects. It automatically takes care of opening and closing the file.

8.9. Raising and Handling Multiple Unrelated Exceptions
Sometimes, you might encounter multiple problems in a program. The ExceptionGroup is introduced as a way to bundle these exceptions together, making it easier to handle multiple issues at once.

8.10. Enriching Exceptions with Notes
After an error occurs, developers may want to add more information to help understand what went wrong. The add_note method allows programmers to attach additional details, called notes, to an exception. These notes are then displayed when viewing the error message.
