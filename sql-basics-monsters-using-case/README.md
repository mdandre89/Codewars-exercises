# SQL Basics - Monsters using CASE

 - URL:[https://www.codewars.com/kata/593ef0e98b90525e090000b9](https://www.codewars.com/kata/593ef0e98b90525e090000b9)
 - Id: 593ef0e98b90525e090000b9
 - Language: sql
 - Completed on: 2017-07-01T18:50:36.141Z
 - Tags: Fundamentals,SQL
 - Description:
You have access to two tables named top\_half and bottom\_half, as follows:

**top\_half schema**
* id
* heads
* arms

**bottom\_half schema**
* id
* legs
* tails

You must return a table with the format as follows:

**output schema**
* id
* heads
* legs
* arms
* tails
* species

The IDs on the tables match  to make a full monster. For heads, arms, legs and tails you need to draw in the data from each table.

For the species, if the monster has more heads than arms, more tails than legs, or both, it is a 'BEAST' else it is a 'WEIRDO'. This needs to be captured in the species column.

All rows should be returned (10).

Tests require the use of CASE. Order by species.

Please use pure SQL, only testing is done in Ruby.
