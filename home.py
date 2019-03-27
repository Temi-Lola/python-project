from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<html>
<head>
  <title>Explore Manchester</title>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" type="text/css" href="home.css">
  <link href="https://fonts.googleapis.com/css?family=Rokkitt" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


</head>
<body>

  <div id="container">

  	<header id="header">

  		<img id="logo" src="https://i.etsystatic.com/14593570/r/il/be970c/1293079357/il_570xN.1293079357_kvsv.jpg">
  		<nav id="navBar">
        <a class="navButton" type="button" href="home.html">HOME</a>
        <a class="navButton" type="button" href="food.html">FOOD</a>
  			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">PLACES</button>
  			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">PEOPLE</button>
  			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">EVENTS</button>
  			<button class="navButton" type="button" onclick="location.href='#contact';">CONTACT</button>

      </nav>
      	</header>

      	<main id="main">
      		<div class="sec1" id="explore">
      			<h1>EXPLORE MANCHESTER</h1>
      			<p>Discover the best things to do, places to go, food to eat and people to follow in the most livable city in the UK .</p>
      		</div>

        <div class="sec2" id="aboutus"
           <h1></h1>

           <div class="container0">
             <h2>Weather</h2>
             <a class="weatherwidget-io" data-height="480px" data-width="311px" href="https://forecast7.com/en/53d48n2d24/manchester/" data-label_1="MANCHESTER" data-label_2="WEATHER" data-icons="Climacons Animated" data-theme="weather_one" >MANCHESTER WEATHER</a>
           <script>
           !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
           </script>
           </div>

           <div class="container1">
  <h2>Transport for Greater Manchester</h2>
  <a class="twitter-timeline" data-height="480px" data-width="400" href="https://twitter.com/OfficialTfGM?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">Tweets by Transport for Greater Manchester</a>
  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
 <a class="follow" href="https://twitter.com/OfficialTfGM?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" target="_blank"><i class="fa fa-twitter fa-lg"></i></a>
</div>

        </div>

        <div class="sec3" id="contact"
         <h1>CONTACT OUR TEAM</h1>
         <p>We're would love to hear from you, let us know about the great places you've been in Manchester</p>

         <div class="container2">
  <form action="/action_page.php" target="_blank" method="POST">
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">

    <label for="rec">Type of recommendation</label>
    <select id="rec" name="rec">
      <option value="place">Place</option>
      <option value="people">People</option>
      <option value="food">Food</option>
      <option value="events">Event</option>
    </select>

    <label for="subject">Description</label>
    <textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>

    <input type="submit" onclick="alert('Thank You for your submition!')" value="Submit">
  </form>
</div>
       </div>

        <div class="footer">
          <a href="#" class="fa fa-facebook"></a>
          <a href="#" class="fa fa-twitter"></a>
          <a href="#" class="fa fa-google"></a>
          <a href="#" class="fa fa-linkedin"></a>
          <a href="#" class="fa fa-youtube"></a>
          <a href="#" class="fa fa-instagram"></a>

        </div>
<body>
  </html>

"""

@app.route('/FOOD')
def food_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Explore Manchester</title>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

    	<link rel="stylesheet" href="food.css">
    </head>
    <body>

      <div id="container">

      	<header id="header">

      	<img id="logo" src="https://i.etsystatic.com/14593570/r/il/be970c/1293079357/il_570xN.1293079357_kvsv.jpg">
      		<nav id="navBar">
            <a class="navButton" type="button" href="home.html">HOME</a>
            <a class="navButton" type="button" href="food.html">FOOD</a>
      			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">PLACES</button>
      			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">PEOPLE</button>
      			<button class="navButton" type="button" onclick="alert('We are sorry! This page is down for maintenance')">EVENTS</button>
            <button class="navButton" type="button" onclick="location.href='#contact';">CONTACT</button>
          </nav>
          	</header>

    <body>
      <br>
      <br>

    <div id="food">
      <article>
        <a href="https://www.tripadvisor.co.uk/Restaurants-g187069-c8-Manchester_Greater_Manchester_England.html" rel="noopener noreferrer" target="_blank">
         <img src="cafe.png" style="width:300px; height: 300px">
         </a>
     <h3>Cafe</h3>
      </article>

    <article>
          <img src="burger_and_pizza.png" style="width:300px; height: 300px">
          <h3>Burger and Pizza</h3>

    </article>

    <article>
    <a href="https://www.tripadvisor.co.uk/Restaurants-g187069-c11-Manchester_Greater_Manchester_England.html" rel="noopener noreferrer" target="_blank">
          <img src="chinese.png" style="width:300px; height: 300px">
    </a>
          <h3>Chinese</h3>
    </article>

    <article>
          <img src="italian.png" style="width:300px; height: 300px">
          <h3>Italian</h3>
    </article>
    </div>
    <br>
    <br>

    <div id="food">
      <article>
          <img src="french.png" style="width:300px; height: 300px">
          <h3>French</h3>

      </article>

    <article>
          <img src="indian.png" style="width:300px; height: 300px">
          <h3>Indian</h3>

    </article>

    <article>
          <img src="local.png" style="width:300px; height: 300px" >
          <h3>Local</h3>
    </article>

    <article>
          <img src="japanese.png" style="width:300px; height: 300px">
          <h3>Japanese</h3>
    </article>
    </div>
    <br>
    <br>
    </body>

    <br>
    <br>

    <div class="sec2" id="aboutus"
       <h1></h1>

       <div class="container0">
         <h2>Weather</h2>
         <a class="weatherwidget-io" data-height="480px" data-width="311px" href="https://forecast7.com/en/53d48n2d24/manchester/" data-label_1="MANCHESTER" data-label_2="WEATHER" data-icons="Climacons Animated" data-theme="weather_one" >MANCHESTER WEATHER</a>
       <script>
       !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
       </script>
       </div>

       <div class="container1">
    <h2>Transport for Greater Manchester</h2>
    <a class="twitter-timeline" data-height="480px" data-width="400" href="https://twitter.com/OfficialTfGM?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">Tweets by Transport for Greater Manchester</a>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    <a class="follow" href="https://twitter.com/OfficialTfGM?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" target="_blank"><i class="fa fa-twitter fa-lg"></i></a>
    </div>
    </div>


    </body>
    </html>

    """

@app.route('/PLACES')
def food_page():
    return """
    "We are Sorry! This page is down for maintenance"
"""
@app.route('/PEOPLE')
def events_page():
    return """
    "We are Sorry! This page is down for maintenance"
"""

@app.route('/EVENTS')
def events_page():
    return """
    "We are Sorry! This page is down for maintenance"
"""
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
