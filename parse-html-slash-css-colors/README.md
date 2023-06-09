# Parse HTML/CSS Colors

 - URL:[https://www.codewars.com/kata/58b57ae2724e3c63df000006](https://www.codewars.com/kata/58b57ae2724e3c63df000006)
 - Id: 58b57ae2724e3c63df000006
 - Language: javascript
 - Completed on: 2017-08-30T09:23:26.285Z
 - Tags: Fundamentals,Algorithms,Strings,Parsers
 - Description:
In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).


## Input:
The input string represents one of the following:

- **6-digit hexadecimal** - "#RRGGBB"  
  e.g. "#012345", "#789abc", "#FFA077"  
  Each pair of digits represents a value of the channel in hexadecimal: 00 to FF


- **3-digit hexadecimal** - "#RGB"  
  e.g. "#012", "#aaa", "#F5A"  
  Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.


- **Preset color name**  
 e.g. "red", "BLUE", "LimeGreen"  
  You have to use the predefined map `PRESET_COLORS` (JavaScript, Python, Ruby), `presetColors` (Java, C#, Haskell), or `preset-colors` (Clojure). The keys are the names of preset colors *in lower-case* and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").


## Examples:

```ruby
parse_html_color('#80FFA0')   # => { r: 128, g: 255, b: 160 }
parse_html_color('#3B7')      # => { r: 51,  g: 187, b: 119 }
parse_html_color('LimeGreen') # => { r: 50,  g: 205, b: 50  }
```
```python
parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }
```
```javascript
parseHTMLColor('#80FFA0');    // => { r: 128, g: 255, b: 160 }
parseHTMLColor('#3B7');       // => { r: 51,  g: 187, b: 119 }
parseHTMLColor('LimeGreen');  // => { r: 50,  g: 205, b: 50  }
```
```clojure
(parse-html-color "#80FFA0")   ; => {:r 128 :g 255 :b 160}
(parse-html-color "#3B7")      ; => {:r 51  :g 187 :b 119}
(parse-html-color "LimeGreen") ; => {:r 50  :g 205 :b 50 }
```
```haskell
-- You can get a value from the map like this:
presetColors ! "blue"
--
parseHtmlColor "#80FFA0"   === fromList [('r',128), ('g',255), ('b',160)]
parseHtmlColor "#3B7"      === fromList [('r',51), ('g',187), ('b',119)]
parseHtmlColor "LimeGreen" === fromList [('r',50), ('g',205), ('b',50)]
```
```java
parse("#80FFA0")   === new RGB(128, 255, 160))
parse("#3B7")      === new RGB( 51, 187, 119))
parse("LimeGreen") === new RGB( 50, 205,  50))

// RGB class is defined as follows:
final class RGB {
    public int r, g, b;
    
    public RGB();
    public RGB(int r, int g, int b);
}
```
```csharp
Parse("#80FFA0")   === new RGB(128, 255, 160))
Parse("#3B7")      === new RGB( 51, 187, 119))
Parse("LimeGreen") === new RGB( 50, 205,  50))

// RGB struct is defined as follows:
struct RGB
{
    public byte r, g, b;
    public RGB(byte r, byte g, byte b);
}
```

