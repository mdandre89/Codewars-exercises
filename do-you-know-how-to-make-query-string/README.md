# Do you know how to make Query String?

 - URL:[https://www.codewars.com/kata/595249fc10b69f4f7a000003](https://www.codewars.com/kata/595249fc10b69f4f7a000003)
 - Id: 595249fc10b69f4f7a000003
 - Language: javascript
 - Completed on: 2017-06-30T13:42:14.166Z
 - Tags: Algorithms,Data Structures,Strings
 - Description:
[Query string](https://en.wikipedia.org/wiki/Query_string) is a way to _serialize_ object, which is used in HTTP requests. You may see it in URL:

```
codewars.com/kata/search/?q=querystring
```

The part `q=querystring` represents that parameter `q` has value `querystring`. Also sometimes querystring used in HTTP POST body:

```
POST /api/users
Content-Type: application/x-www-form-urlencoded

username=warrior&kyu=1&age=28
```

The string `username=warrior&kyu=1&age=28` represents an entity (user in this example) with username equals warrior, kyu equals 1 and age equals 28. The entity may be represented as object:

```
{
  "username": "warrior",
  "kyu": 1,
  "age": 28
}
```

Sometimes there are more than one value for property:

```
{
  "name": "shirt",
  "colors": [ "white", "black" ]
}
```

Then it represents as repeated param:

```
name=shirt&colors=white&colors=black
```

So, your task is to write a function that convert an object to query string:

```crystal
to_query_string({ "bar": [ 2, 3 ], "foo": 1 }) # => "bar=2&bar=3&foo=1"
```
```javascript
toQueryString({ foo: 1, bar: [ 2, 3 ] }) // => "foo=1&bar=2&bar=3"
```
```python
to_query_string({ "bar": [ 2, 3 ], "foo": 1 }) // => "bar=2&bar=3&foo=1"
```
```ruby
to_query_string({ "bar": [ 2, 3 ], "foo": 1 }) # => "bar=2&bar=3&foo=1"
```

Next you may enjoy kata [Objectify a URL Query String](https://www.codewars.com/kata/objectify-a-url-query-string).

```if:python
Note: `urllib.parse.urlencode` has been deactivated.
```
```if:javascript
Note: `require` has been disabled.
```
