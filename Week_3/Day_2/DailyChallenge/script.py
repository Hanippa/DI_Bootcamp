
# Instructions :

#     Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

#     The Pagination class will accept 2 parameters:
#         items (default: []): A list of contents to paginate.
#         pageSize (default: 10): The amount of items to show in each page.

#     So for example we could initialize our pagination like this:

#     alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

#     p = Pagination(alphabetList, 4)


#     The Pagination class will have a few methods:
#         getVisibleItems() : returns a list of items visible depending on the pageSize

#     So for example we could use this method like this:

#     p.getVisibleItems() 
#     # ["a", "b", "c", "d"]

#         You will have to implement various methods to go through the pages such as:
#             prevPage()
#             nextPage()
#             firstPage()
#             lastPage()
#             goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

#     The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
#     The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
#     Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
#     If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination:
    def __init__(self,list=[],pageSize=10):
        self.list = list
        self.pageSize = int(pageSize)
        self.totalPages = len(self.list)
        self.currentPage = 13
    def getVisibleItems(self):
        relist=[]
        for i in range(self.currentPage*self.pageSize-self.pageSize,(self.currentPage*self.pageSize)):
            relist.append(self.list[i])
        return relist
    # def nextPage(self):

    # def prevPage(self):

    
    # def goToPage(self,page):

    # def firstPage(self):
        
    # def lastPage(self):
        

alphabetList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')

p = Pagination(alphabetList, 2)

print(p.getVisibleItems()) 
# ["a", "b", "c", "d"]

# p.nextPage()

# print(p.getVisibleItems())
# # ["e", "f", "g", "h"]

# p.lastPage()

# print(p.getVisibleItems())
# # ["y", "z"]
