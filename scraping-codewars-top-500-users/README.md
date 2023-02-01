# Scraping: Codewars Top 500 Users

 - URL:[https://www.codewars.com/kata/581c06b95cfa838603000435](https://www.codewars.com/kata/581c06b95cfa838603000435)
 - Id: 581c06b95cfa838603000435
 - Language: python
 - Completed on: 2022-06-12T21:23:20.934Z
 - Tags: Fundamentals
 - Description:
You should get and parse the html of the [codewars leaderboard page](https://www.codewars.com/users/leaderboard).

You can use `Nokogiri`(Ruby) or `BeautifulSoup`(Python) or `CheerioJS`(Javascript).

For Javascript: Return a Promise resolved with your 'Leaderboard' Object!

 ----

 #### Return a 'Leaderboard' object with a position property.
```
Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index).
```

 #### Each User should have the following properties
```
User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer
```


 #### Ex:
```
  an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
  an_alien.name                        # => "myjinxin2015"
  an_alien.clan                        # => "China Changyuan"
  an_alien.honor                       # => 21446
  
```

