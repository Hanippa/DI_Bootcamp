// Instructions

// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

//     Create a class named Video. The class should be constructed with the following parameters:
//         title (a string)
//         uploader (a string, the person who uploaded it)
//         time (a number, the duration of the video - in seconds)
//     Create a method called watch() which displays a string as follows:
//     “uploader parameter watched all time parameter of title parameter!”
//     Instantiate a new Video instance and call the watch() method.
//     Instantiate a second Video instance with different values.
//     Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
//     Think of the best data structure to save this information within the array.
//     Bonus: Loop through the array to instantiate those instances.

class Video {
  constructor(title , uploader , time){
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }
  watch(){
    return `${this.uploader} watched all ${this.time} of ${this.title}!`
  }
}

const zoovideo = new Video('Me at the zoo' , 'Jawed' , 0.19)

console.log(zoovideo.watch())

const dargvideo = new Video('Drama at dragcon' , 'swell entertainment' , 27.37)

const videosdata = [
  {"title" : "video1" , "uplodaer" : "uploader1" , "time" : "time1"},
  {"title" : "video2" , "uplodaer" : "uploader2" , "time" : "time2"},
  {"title" : "video3" , "uplodaer" : "uploader3" , "time" : "time3"},
  {"title" : "video4" , "uplodaer" : "uploader4" , "time" : "time4"},
  {"title" : "video5" , "uplodaer" : "uploader5" , "time" : "time5"}
]

for (let video of videosdata){
  console.log(video)
  window[video.title] = new Video(video.title , video.uplodaer , video.time);
}