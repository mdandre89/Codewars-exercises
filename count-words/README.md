# Count words

 - URL:[https://www.codewars.com/kata/56b3b27cadd4ad275500000c](https://www.codewars.com/kata/56b3b27cadd4ad275500000c)
 - Id: 56b3b27cadd4ad275500000c
 - Language: python
 - Completed on: 2017-12-20T10:16:44.538Z
 - Tags: Strings,Regular Expressions,Fundamentals
 - Description:
Kate likes to count words in text blocks. By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:

`Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp.` contains "words" `['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']`

Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

Today Kate's too lazy and have decided to teach her computer to count "words" for her.


Example Input 1
-------------
Hello there, little user5453 374 ())$.

Example Output 1
-------------
4

Example Input 2
-------------

  I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.

Example Output 2
--------------

112
