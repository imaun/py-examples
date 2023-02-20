# How old are you?
In this example we want to get the User birthday from standard input and tell him/her how much he/she old. We begin with getting the year, month and day, then creates a datetime object with the given inputs. Then calculate its difference with now :
```py
birthday = datetime.datetime(year, month, day)
```
This will give us `birthday` which its type is `<class 'datetime.timedelta'>` and we can use it to calculate gap between date and times.

# You will learn...
- How to get current datetime in python
- How to calculate diffrence between two datettime
- How to calculates someone age from her/his birthday

---


