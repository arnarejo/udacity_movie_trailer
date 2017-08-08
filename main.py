# webbrowser library required to open/view the html file
import webbrowser

# os library reqiured to find the path of current working directory
import os

# movies file contains Movie class to generate individual movie database
import movies

# create movies database
toy_story = movies.Movie(
    'Toy Story',
    1995,
    8.3,
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')
gladiator = movies.Movie(
    'Gladiator',
    2000,
    8.5,
    'https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg',
    'https://www.youtube.com/watch?v=owK1qxDselE')
the_shawshank_redemption = movies.Movie(
    'The Shawshank Redemption',
    1994,
    9.3,
    'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',  #noqa
    'https://www.youtube.com/watch?v=6hB3S9bIaco')
finding_nemo = movies.Movie(
    'Finding Nemo',
    2003,
    8.1,
    'https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg',
    'https://www.youtube.com/watch?v=wZdpNglLbt8')
badlapur = movies.Movie(
    'Badlapur',
    2015,
    7.5,
    'http://www.bollywoodirect.com/wp-content/uploads/2014/12/badlapur1.jpg',
    'https://www.youtube.com/watch?v=9KEoZanqlOE')
# final movies_list contains all the movies database generated
movies_list = [
    toy_story,
    gladiator,
    the_shawshank_redemption,
    finding_nemo,
    badlapur]

html_start = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        .movies {
            margin: 10px;
            }

        .navbar {
            background-color: #3b5998;
            color: #f7f7f7;
            }

        .box {
            background-color: #eee;
            border: 10px solid white;
            text-align: center;
            }

        img {
            width: 80%;
            margin: auto;
            margin-bottom: 20px;
            }
    </style>
  </head>
  <body>
<div class="navbar">
  <h2>Udacity - Movie Trailer Site</h2>
</div>
<div class="movies row">
  '''

html_end = '''
    </div>
  </div>
</body>
</html>'''

# create open_movies_age function
def open_movies_page(movieList):

    # create dynamic html by iterating through the movies list
    html_inner = ''
    for movie in movieList:
        html_inner += '<div class="box col-sm-6 col-md-4"><h5>'+movie.title+'</h5><p>IMDB Rating: ' +str(movie.imdb_rating) +'</p><img src="'+movie.poster_url+'" alt=""><br><a href="'+movie.trailer_url+'" target="_blank"><button class="btn btn-primary">Click to Watch Trailer</button></a></div>'

    # combine dynamic html with rest of html to create complete html page
    html_final = html_start + html_inner + html_end

    # open, write and close html file
    with open('sample.html', 'w') as f:
        f.write(html_final)
        f.close()

    # url file name
    url_name = "sample.html"

    # get current folders
    current_directory = os.getcwd()

    # set html file path
    file_path = current_directory + '/sample.html'

    # MacOS Chrome Path
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # open html file
    webbrowser.get(chrome_path).open_new_tab(file_path)

# call open_movies_page function
open_movies_page(movies_list)
