# Pill Pusher

 - URL:[https://www.codewars.com/kata/628e6f112324192c65cd8c97](https://www.codewars.com/kata/628e6f112324192c65cd8c97)
 - Id: 628e6f112324192c65cd8c97
 - Language: python
 - Completed on: 2022-06-24T23:01:20.380Z
 - Tags: Fundamentals
 - Description:
The target dose for the oral medication *Katamol* has been calculated: <code>d</code> (in mg).

The only options to prescribe the medication are pills of strength <code>a</code> (in mg) or <code>b</code> (in mg), so it may not be possible to prescribe the exact target dose.

For a given target dose <code>d</code>, return the highest possible dose that can be made with any amount of pills <code>a</code> and/or <code>b</code> that does not exceed the target dose. 

Input: 3 integers, <code>d</code>,<code>a</code>,<code>b</code> representing the calculated target dose, the dose of pill <code>a</code>, and the dose of pill <code>b</code> (all in mg)

Output: Integer value of the closest dose to the target that can be made with any amount of pills <code>a</code> and/or <code>b</code> without going above the target dose.

Example:
```if:python
    Input:
    99,25,60
    Output:
    85
    # 85 can be made with 1 * 25mg pill and 1* 60mg pill, no closer dose can be made that is less than or equal to 99
    
```

Constraints:

<code>a</code> <= <code>d</code>

2 <=<code>d</code> <=10000

1 <= <code>a</code> < <code>b</code> <5000


