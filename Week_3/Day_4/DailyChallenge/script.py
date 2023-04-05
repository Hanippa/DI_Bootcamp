# Instructions :

# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.


# Part I

# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

#     Create a class called Text that takes a string as an argument and store the text in a attribute.
#     Hint: You need to manually copy-paste the text, straight into the code

#     Implement the following methods:
#         a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#         a method that returns the most common word in the text.
#         a method that returns a list of all the unique words in the text.


# Part II

# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

#     Implement a classmethod that returns a Text instance but with a text file:

#         >>> Text.from_file('the_stranger.txt')

#     Hint: You need to open and read the text from the text file.

#     Now, use the provided the_stranger.txt file and try using the class you created above.


# Bonus:

#     Create a class called TextModification that inherits from Text.

#     Implement the following methods:
#         a method that returns the text without any punctuation.
#         a method that returns the text without any english stop-words (check out what this is !!).
#         a method that returns the text without any special characters.

# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


class Text:
    def __init__(self, text):
        self.text = text
    def word_freqency(self,word):
        text_arr = self.text.split(" ")
        return text_arr.count(word)
    def most_common(self):
        common = "-"
        for x in self.text.split(" "):
            if self.word_freqency(x) > self.word_freqency(common):
                common = x
        return common
    def unique(self):
        unique = []
        for x in self.text.split(" "):
            if self.word_freqency(x) == 1:
                unique.append(x)
        return unique
    @classmethod
    def from_file(self ,file_name):
        with open(file_name, 'r') as file:
            return file.read()



import string
class TextModification(Text):
    def wo_punctuation(self):
        restring = ""
        for i in self.text:
            if i not in string.punctuation:
                restring += i
        return restring
    def wo_stop_words(self):
        with open("stop_words.txt",'r') as file:
            stop_wrods = file.read()
        restring = ""
        for i in self.text.split(" "):
            if i not in stop_wrods:
                restring += i
        return restring
    def wo_special(self):
        restring = ""
        for i in self.text:
            if i in string.ascii_letters:
                restring += i
        return restring
stex = TextModification("i luv you ... Mista, and ")
print(stex.wo_special())

blah = Text(Text.from_file("the_stranger.txt"))
print(blah.word_freqency("the"))
# print(blah.most_common())
print(blah.unique())
# print(blah.from_file("the_stranger.txt"))

