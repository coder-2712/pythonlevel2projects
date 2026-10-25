import datetime as dt
import time

print("Welcome to the birthday countdown!")

try:
    year = int(input("Which year were you born in?\n"))
    month = int(input("Which month were you born in? (1 for January, 2 for February and so on)\n"))
    day = int(input("Which day of that month?\n"))

    try:
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday']

        date_birth = dt.datetime(year, month, day)

        leap_year_bday = 0

        if date_birth.day == 29 and date_birth.month == 2:
            leap_year_bday = 1
            print('Your birthday is a leap year day.')

        weekday_num = date_birth.weekday()

        print()
        print("You were born on a...", end=' ')
        print(weekday_names[weekday_num])

        current_time = dt.datetime.now()
        thisyear = current_time.year

        if date_birth < current_time:

            try:
                thisyear_bday = dt.datetime(thisyear, month, day)

                if thisyear_bday > current_time:
                    next_bday = thisyear_bday
                    print('Your next birthday will be this year:')

                else:
                    if leap_year_bday != 1:
                        next_bday = dt.datetime(thisyear + 1, month, day)
                    else:
                        next_bday = dt.datetime(thisyear + 4, month, day)

                    print('Your next birthday will be next year:')

            except:
                
                next_bday = dt.datetime(
                    thisyear + (4 - thisyear % 4),
                    month,
                    day
                )

            print(next_bday)

            weekday_num = next_bday.weekday()

            print()
            print("Your next birthday will be on a ... ", end=' ')
            print(weekday_names[weekday_num])

            diff = current_time - date_birth
            a = diff.days // 365

            print("You are", a, "years old as of now.")

            famous_ppl_bdays = ["J. D. Salinger", "Isaac Asimov", "J. R. R. Tolkien", "Isaac Newton", "Diane Keaton", "Rowan Atkinson", "Nicolas Cage", "Elvis Presley", "Kate Middleton", "Rod Stewart", "Mary J. Blige", "Jeff Bezos", "Orlando Bloom", "Jason Bateman", "Martin Luther King Jr.", "Kate Moss", "Benjamin Franklin", "Kevin Costner", "Edgar Allan Poe", "David Lynch", "Emma Bunton", "Lord Byron", "Tiffani Thiessen", "Neil Diamond", "Virginia Woolf", "Ellen DeGeneres", "Wolfgang Amadeus Mozart", "Elijah Wood", "Oprah Winfrey", "Franklin D. Roosevelt", "Justin Timberlake", "Harry Styles", "Shakira", "Warwick Davis", "Rosa Parks", "Cristiano Ronaldo", "Bob Marley", "Charles Dickens", "James Dean", "Tom Hiddleston", "Emma Roberts", "Thomas Edison", "Charles Darwin", "Peter Gabriel", "Frederick Douglass", "Galileo Galilei", "John McEnroe", "Michael Jordan", "John Travolta", "Millie Bobby Brown", "Rihanna", "Nina Simone", "George Washington", "Emily Blunt", "Steve Jobs", "George Harrison", "Johnny Cash", "John Steinbeck", "John Turturro", "Gioachino Rossini", "Justin Bieber", "Dr. Seuss", "Alexander Graham Bell", "Antonio Vivaldi", "Eva Mendes", "Michelangelo", "Bryan Cranston", "Freddie Prinze Jr.", 
                                "Yuri Gagarin", "Sharon Stone", "Douglas Adams", "Liza Minnelli", "William H. Macy", "Albert Einstein", "Eva Longoria", "Alexandra Daddario", "Rob Lowe", "Queen Latifah", "Bruce Willis", "Spike Lee", "Johann Sebastian Bach", "Reese Witherspoon", "Akira Kurosawa", "Harry Houdini", "Elton John", "Diana Ross", "Quentin Tarantino", "Lady Gaga", "Christopher Lambert", "Vincent van Gogh", "René Descartes", "Sergei Rachmaninoff", "Hans Christian Andersen", "Marlon Brando", "Maya Angelou", "Gregory Peck", "Paul Rudd", "Russell Crowe", "Kristen Stewart", "Mandy Moore", "Joss Stone", "David Letterman",
                                "Thomas Jefferson", "Sarah Michelle Gellar", "Leonardo da Vinci", "Charlie Chaplin", "Jennifer Garner", "Conan O'Brien", "James Franco", "Adolf Hitler", "Queen Elizabeth II", "Jack Nicholson", "William Shakespeare", "Barbra Streisand", "Al Pacino", "Carol Burnett", "Ulysses S. Grant", "Jessica Alba", "Uma Thurman", "Gal Gadot", "Tim McGraw", "Dwayne Johnson", "James Brown", "Audrey Hepburn", "Adele", "George Clooney", "Pyotr Tchaikovsky", "Enrique Iglesias", "Billy Joel", "Bono", "Salvador Dalí", "Florence Nightingale", "Stevie Wonder", "George Lucas", "Andy Murray", "Megan Fox", "Enya", 
                                "Tina Fey", "Malcolm X", "Cher", "Mr. T", "Arthur Conan Doyle", "Joan Collins", "Queen Victoria", "Mike Myers", "Helena Bonham Carter", "Christopher Lee", "Kylie Minogue", "John F. Kennedy", "Idina Menzel", "Clint Eastwood", "Marilyn Monroe", "Justin Long", "Josephine Baker", "Angelina Jolie", "Mark Wahlberg", "Alexander Pushkin", "Prince", "Kanye West", "Johnny Depp", "Judy Garland", "Jacques Cousteau", "Anne Frank", "Chris Evans", "Che Guevara", "Courteney Cox", "Tupac Shakur", "Venus Williams", "Isabella Rossellini", "Hugh Dancy", "Nicole Kidman", "Chris Pratt", "Meryl Streep", "Zinedine Zidane", 
                                "Lionel Messi", "George Michael", "Ariana Grande", "Helen Keller", "Mel Brooks", "Antoine de Saint-Exupéry", "Mike Tyson", "Princess Diana", "Margot Robbie", "Tom Cruise", "Nathaniel Hawthorne", "Edie Falco", "Frida Kahlo", "Ringo Starr", "Kevin Bacon", "Tom Hanks", "Nikola Tesla", "Giorgio Armani", "Henry David Thoreau", "Harrison Ford", "Gustav Klimt", "Rembrandt", "Will Ferrell", "Luke Bryan", "Nelson Mandela", "Benedict Cumberbatch", "Carlos Santana", "Ernest Hemingway", "Selena Gomez", "Daniel Radcliffe", "Amelia Earhart", "Matt LeBlanc", "Mick Jagger", "Alexandre Dumas", "Jacqueline Kennedy Onassis", 
                                "Fernando Alonso", "Arnold Schwarzenegger", "J. K. Rowling", "Jason Momoa", "James Baldwin", "Tom Brady", "Barack Obama", "Neil Armstrong", "Andy Warhol", "David Duchovny", "Roger Federer", "Whitney Houston", "Antonio Banderas", "Chris Hemsworth", "Cara Delevingne", "Alfred Hitchcock", "Steve Martin", "Jennifer Lawrence", "Madonna", "Robert De Niro", "Patrick Swayze", "Bill Clinton", "H. P. Lovecraft", "Usain Bolt", "Dua Lipa", "Kobe Bryant", "Rupert Grint", "Sean Connery", "Macaulay Culkin", "Lyndon B. Johnson", "Jack Black", "Michael Jackson", "Cameron Diaz", "Richard Gere", "Zendaya", "Keanu Reeves", 
                                "Charlie Sheen", "Beyoncé", "Freddie Mercury", "Idris Elba", "Queen Elizabeth I", "Pink", "Adam Sandler", "Colin Firth", "O. Henry", "Jesse Owens", "Roald Dahl", "Amy Winehouse", "Agatha Christie", "Mickey Rourke", "Narendra Modi", "Greta Garbo", "Jimmy Fallon", "George R. R. Martin", "Stephen King", "Tom Felton", "Bruce Springsteen", "F. Scott Fitzgerald", "Catherine Zeta-Jones", "Serena Williams", "Avril Lavigne", "Brigitte Bardot", "Miguel de Cervantes", "Monica Bellucci", "Julie Andrews", "Mahatma Gandhi", "Gwen Stefani", "Dakota Johnson", "Kate Winslet", "Le Corbusier", "Simon Cowell", "Matt Damon", 
                                "John Lennon", "Giuseppe Verdi", "Eleanor Roosevelt", "Hugh Jackman", "Sacha Baron Cohen", "Usher", "Oscar Wilde", "Angela Lansbury", "Rita Hayworth", "Zac Efron", "John le Carré", "Snoop Dogg", "Kim Kardashian", "Catherine Deneuve", "Pelé", "Dracula", "Pablo Picasso", "Hillary Clinton", "Sylvia Plath", "Bill Gates", "Bob Ross", "Diego Maradona", "John Keats", "Anthony Kiedis", "David Schwimmer", "Kendall Jenner", "Matthew McConaughey", "Art Garfunkel", "Emma Stone", "Marie Curie", "Gordon Ramsay", "Carl Sagan", "Martin Luther", "Leonardo DiCaprio", "Anne Hathaway", "Robert Louis Stevenson", "Claude Monet", 
                                "Georgia O'Keeffe", "Maggie Gyllenhaal", "Martin Scorsese", "Owen Wilson", "Indira Gandhi", "Joe Biden", "Goldie Hawn", "Scarlett Johansson", "Miley Cyrus", "Katherine Heigl", "Andrew Carnegie", "Rita Ora", "Bruce Lee", "Jon Stewart", "C. S. Lewis", "Mark Twain", "Woody Allen", "Britney Spears", "Brendan Fraser", "Jay-Z", "Walt Disney", "Judd Apatow", "Noam Chomsky", "Nicki Minaj", "Judi Dench", "Emily Dickinson", "Hailee Steinfeld", "Frank Sinatra", "Taylor Swift", "Vanessa Hudgens", "Don Johnson", "Jane Austen", "Milla Jovovich", "Brad Pitt", "Jake Gyllenhaal", "Jonah Hill", "Samuel L. Jackson",
                                "Giacomo Puccini", "Humphrey Bogart", "Ricky Martin", "Annie Lennox", "Jared Leto", "Timothée Chalamet", "Denzel Washington", "Jude Law", "LeBron James", "Anthony Hopkins"]


            start_of_year = dt.datetime(2000,1,1)
            bday_2000 = dt.datetime(2000, month, day)
            days_passed = (bday_2000 - start_of_year).days
            famous_bday = famous_ppl_bdays[days_passed]
            print("You were born on the same day as", famous_bday, ". If you dont know who that is, search it up!")



            if year >= 1946 and year <= 1964:
                print('You are a part of the generation of baby boomers.')
            elif year >= 1965 and year <= 1980:
                print("You are a part of Generation X.")
            elif year >= 1981 and year <= 1996:
                print("You are a part of Generation Y.") 
            elif year >= 1997 and year <= 2009:
                print("You are a part of Generation Z.")
            elif year >= 2010 and year <= 2024:
                print('You are a part of Generation Alpha.')
            elif year >= 2025 and year <= 2036:
                print("You are a part of Generation Beta.")

            while next_bday > current_time:

                current_time = dt.datetime.now()
                dd = next_bday - current_time

                days_left = dd.days
                total_seconds_left = dd.seconds

                total_seconds = total_seconds_left % 60
                total_minutes_left = total_seconds_left // 60
                minutes_left = total_minutes_left % 60
                hours_left = total_minutes_left // 60

                print(
                    "Your next birthday is in", days_left, "days", hours_left, "hours,", minutes_left, "minutes, and", total_seconds, "seconds.", end='\r')

                time.sleep(1)

        else:
            print("Future birthdate entered. Please try again.")

    except:
        print("Invalid date. Please try again.")

except:
    print("It looks like there were incorrect values entered. Please try again.")
