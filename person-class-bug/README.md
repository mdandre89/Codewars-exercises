# Person Class Bug

 - URL:[https://www.codewars.com/kata/513f887e484edf3eb3000001](https://www.codewars.com/kata/513f887e484edf3eb3000001)
 - Id: 513f887e484edf3eb3000001
 - Language: python
 - Completed on: 2022-06-13T14:20:34.128Z
 - Tags: Bugs
 - Description:
The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails. 

```ruby
person = Person.new('Yukihiro', 'Matsumoto', 47)
puts person.full_name
puts person.age
```
```python
person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)
```

For this exercise you need to fix the code so that it works correctly.
