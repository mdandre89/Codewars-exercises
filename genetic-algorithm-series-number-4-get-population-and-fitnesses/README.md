# Genetic Algorithm Series - #4 Get population and fitnesses

 - URL:[https://www.codewars.com/kata/567b468357ed7411be00004a](https://www.codewars.com/kata/567b468357ed7411be00004a)
 - Id: 567b468357ed7411be00004a
 - Language: javascript
 - Completed on: 2017-08-06T13:37:26.123Z
 - Tags: Algorithms,Genetic Algorithms,Arrays
 - Description:
In a genetic algorithm, a population is a collection of candidates that may evolve toward a better solution.

We determine how close a chromosome is to a ideal solution by calculating its fitness.
https://www.codewars.com/kata/567b468357ed7411be00004a/train
You are given two parameters, the `population` containing all individuals and a function `fitness` that determines how close to the solution a chromosome is.

Your task is to return a collection containing an object with the chromosome and the calculated fitness.

```
[
  { chromosome: c, fitness: f },
  { chromosome: c, fitness: f },
  ...
]
```
~~~if:csharp
Note: you have a pre-loaded class `ChromosomeWrap` and you should return a collection of it instead.
```csharp
public class ChromosomeWrap
{
    public string Chromosome { get; set; }
    public double Fitness { get; set; }
}
```
~~~

~~~if:python
Note: you have a pre-loaded namedtuple `ChromosomeWrap` and you should return a collection of it instead.
```python
ChromosomeWrap = namedtuple("ChromosomeWrap", ["chromosome", "fitness"])
```
~~~

~~~if:php
Note: you have to return **an array of associative arrays** instead:
```php
// E.g.
array(
  array("chromosome" => $c, "fitness" => $f),
  array("chromosome" => $c, "fitness" => $f),
  // ... 
  array("chromosome" => $c, "fitness" => $f)
);
```
~~~

# See other katas from this series

  - [Genetic Algorithm Series - #1 Generate](http://www.codewars.com/kata/genetic-algorithm-series-number-1-generate)
  - [Genetic Algorithm Series - #2 Mutation](http://www.codewars.com/kata/genetic-algorithm-series-number-2-mutation)
  - [Genetic Algorithm Series - #3 Crossover](http://www.codewars.com/kata/genetic-algorithm-series-number-3-crossover)
  - **Genetic Algorithm Series - #4 Get population and fitnesses**
  - [Genetic Algorithm Series - #5 Roulette wheel selection](http://www.codewars.com/kata/genetic-algorithm-series-number-5-roulette-wheel-selection)

*This kata is a piece of [Binary Genetic Algorithm](http://www.codewars.com/kata/526f35b9c103314662000007)*
