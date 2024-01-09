Opening Files:
open() function is used to open a file and returns a file object.
Syntax: open(filename, mode, encoding=None)
filename: A string containing the name of the file.
mode: A string indicating the mode of file access ('r' for read, 'w' for write, 'a' for append, 'r+' for read and write).
encoding: An optional parameter specifying the encoding (default is platform-dependent).
File Modes:
'r': Read mode.
'w': Write mode (existing file content is erased).
'a': Append mode.
'r+': Read and write mode.
'b': Binary mode (e.g., 'rb' for reading binary).
Using with Statement:
It's recommended to use the with statement when dealing with file objects.
Ensures the file is properly closed after use, even if an exception occurs.
Reading and Writing:
f.read(size): Reads a specified number of characters or the entire file.
f.readline(): Reads a single line from the file.
Looping over a file object reads lines efficiently.
f.write(string): Writes the contents of a string to the file.
File Position and Seeking:
f.tell(): Returns the current position in the file.
f.seek(offset, whence): Changes the file object's position.
whence: 0 for the beginning, 1 for the current position, 2 for the end (optional, defaults to 0).
Closing Files:
It's important to close files explicitly with f.close() or use the with statement.
Failure to close files may result in data not being completely written to disk.
JSON Serialization:
The json module allows serialization and deserialization of Python objects.
json.dumps(obj): Serializes an object to a JSON formatted string.
json.dump(obj, file): Serializes an object to a text file.
json.load(file): Deserializes an object from a file.
It's worth noting that the text provides practical examples and recommendations for file handling and emphasizes the importance of encoding and closing files properly. The json module is introduced as a convenient way to handle structured data serialization.
