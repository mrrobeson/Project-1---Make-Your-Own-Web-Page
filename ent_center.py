import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
#toy_story.show_trailer()
emps_groove = media.Movie("Emperor's New Groove",
                          "Prince gets turned into a llama",
                          "http://upload.wikimedia.org/wikipedia/en/6/69/Grooveposter.jpg",
                          "https://www.youtube.com/watch?v=t_YjSbp5KHM")
#emps_groove.show_trailer()

step_bros = media.Movie("Step Brothers",
                        "Two spoiled guys become competitive stepbrothers after their single parents get hitched", "http://upload.wikimedia.org/wikipedia/en/thumb/d/d9/StepbrothersMP08.jpg/220px-StepbrothersMP08.jpg",
                        "https://www.youtube.com/watch?v=ANjenc4W1_Q")                        

movies = [toy_story, emps_groove, step_bros]
fresh_tomatoes.open_movies_page(movies)

