import media
import fresh_tomatoes88

# 88th Academy Awards Best Picture Nominees
# Story Line and Poster Image from IMDb
# Movie Trailer from movie studio's official Youtube channels
spotlight = media.Movie("Spotlight",
                        "The true story of how the Boston Globe uncovered the massive scandal of"
                        " child molestation and cover-up within the local Catholic Archdiocese, shaking"
                        " the entire Catholic Church to its core.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyOTM5OTIzNV5BMl5BanBnXkFtZTgwMDkzODE2NjE@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=56jw6tasomc")

big_short = media.Movie("The Big Short",
                        "Four denizens in the world of high-finance predict the credit and housing"
                        " bubble collapse of the mid-2000s, and decide to take on the big banks for"
                        " their greed and lack of foresight.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc4MThhN2EtZjMzNC00ZDJmLThiZTgtNThlY2UxZWMzNjdkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SX640_CR0,0,640,999_AL_.jpg",
                        "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

bridge_of_spies = media.Movie("Bridge of Spies",
                              "During the Cold War, an American lawyer is recruited to defend an arrested"
                              " Soviet spy in court, and then help the CIA facilitate an exchange of the spy"
                              " for the Soviet captured American U2 spy plane pilot, Francis Gary Powers.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxOTI0MjU5NV5BMl5BanBnXkFtZTgwNzM4OTk4NTE@._V1_SY1000_SX675_AL_.jpg",
                              "https://www.youtube.com/watch?v=7JnC2LIJdR0")

brooklin = media.Movie("Brooklin",
                       "An Irish immigrant lands in 1950s Brooklyn, where she quickly falls into a"
                       " romance with a local. When her past catches up with her, however, she must"
                       " choose between two countries and the lives that exist within.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMzE4MDk5NzEyOV5BMl5BanBnXkFtZTgwNDM4NDA3NjE@._V1_SY1000_SX675_AL_.jpg",
                       "https://www.youtube.com/watch?v=15syDwC000k")

mad_max = media.Movie("Media Max: Fury Road",
                      "A woman rebels against a tyrannical ruler in postapocalyptic Australia in"
                      " search for her home-land with the help of a group of female prisoners, a"
                      " psychotic worshipper, and a drifter named Max.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY1000_CR0,0,687,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his team assume him dead, and must"
                          " rely on his ingenuity to find a way to signal to Earth that he is alive.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_revenant = media.Movie("The Revenant",
                           "A frontiersman on a fur trading expedition in the 1820s fights for survival"
                           " after being mauled by a bear and left for dead by members of his own"
                           " hunting team.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BY2FmODc2N2QtYmY3MS00YTMwLWI2NGYtZWRmYWVkNjFjZmI0XkEyXkFqcGdeQXVyNTMxMjgxMzA@._V1_.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

room = media.Movie("Room",
                   "A young boy is raised within the confines of a small shed.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE4NzgzNzEwMl5BMl5BanBnXkFtZTgwMTMzMDE0NjE@._V1_SY1000_SX675_AL_.jpg",
                   "https://www.youtube.com/watch?v=E_Ci-pAL4eE")

movies = [spotlight, big_short, bridge_of_spies, brooklin, mad_max, the_martian, the_revenant, room]

# Launch Movie Trailer Website
fresh_tomatoes88.open_movies_page(movies)
