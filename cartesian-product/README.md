# Cartesian product

 - URL:[https://www.codewars.com/kata/59ca6fda23dacca1e300003e](https://www.codewars.com/kata/59ca6fda23dacca1e300003e)
 - Id: 59ca6fda23dacca1e300003e
 - Language: python
 - Completed on: 2017-10-30T11:56:43.961Z
 - Tags: Mathematics,Sets,Data Structures,Set Theory,Algorithms
 - Description:
The __cartesian product__ of two sets A and B, written __"A × B"__ is equal to the set of all possible combinations of values from both sets. Here's an example, taken from <a href='https://www.mathstopia.net/sets/cartesian-product'>Mathstopia</a> :

<a href='https://www.mathstopia.net/sets/cartesian-product'><img src='https://www.mathstopia.net/sites/default/files/cartesian-products.jpg'></a>

<h2>Your task</h2>
<p>Implement function <code>cart_prod</code>, which returns the cartesian product (in the form of <code>tuples</code>) of any number of sets passed to it (note the <code>*</code> before <code>sets</code> in the function definition). Also,
<ul>
<li>The cartesian product A × B × C, where A, B and C are sets, is equal to (A × B) × C. See bottom of description for a concrete e×ample.</li>
<li>If no set is passed in, return a set containing an tempty tuple.</li>
<li>If a single set is passed in, return a set of tuples of the elements of the set.</li>
<li>If any of the sets passed in is empty, return an empty set.</li>
</ul>

*Note* : You are not allowed to use the word "itertools" in your solution (as in, <code>from itertools import product ¯\\_(ツ)_/¯</code>).

<h3>Ecample with three sets</h3>
If <code>A = {1, 2}; B = {'x', 'y'}; C = {δ, γ}</code>
Then <code>A × B × C = {(1, 'x', δ), (1, 'x', γ), (1, 'y', δ), (1, 'y', γ),
                  (2, 'x', δ), (2, 'x', γ), (2, 'y', δ), (2, 'y', γ)}</code>
Note that the cardinality (number of elements) of a cartesian product is always equal to the product of the cardinalities of the sets in the cartesian product (here, |A| = |B| = |C| = 2, therefore |A × B × C| = 8).
