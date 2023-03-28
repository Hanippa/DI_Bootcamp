# Exercise 1

# Access the value of key "history"
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

# answer
print(sample_dict["class"]["student"]["marks"]["history"])


# Exercise 2

# Delete set of keys from Python Dictionary


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

# answer

del sample_dict["name"] , sample_dict["salary"]
print(sample_dict)