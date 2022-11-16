# SQL Basics - Trimming the Field

 - URL:[https://www.codewars.com/kata/59401c25c15cbeb58d000028](https://www.codewars.com/kata/59401c25c15cbeb58d000028)
 - Id: 59401c25c15cbeb58d000028
 - Language: sql
 - Completed on: 2017-06-29T10:00:51.668Z
 - Tags: Fundamentals,SQL
 - Description:
You have access to a table of monsters as follows:

**monsters schema**
* id
* name
* legs
* arms
* characteristics

The monsters in the provided table have too many characteristics, they really only need one each. Your job is to trim the characteristics down so that each monster only has one. If there is only one already, provide that. If there are multiple, provide only the first one (don't leave any commas in there).

You must return a table with the format as follows:

**output schema**
* id
* name
* characteristic

Order by id
