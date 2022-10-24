In this note, I will describe the Analyzer part of the system

<img width="537" alt="Screen Shot 2022-10-23 at 11 43 28 PM" src="https://user-images.githubusercontent.com/103418311/197449972-cc3ec944-87aa-4e58-953a-a12322eb8e70.png">

In the StatsAnalyzer, it will consistantly analyze the light illumination difference from the light sensor and the target illumination configured by the user.

In order to do this, there will be an additional container(django-q) that runs the analysis periodically.

This container creates a scheduler as follows
```python
Schedule.objects.create(
    func="analyzer.tasks.calculate_current_difference_and_save",
    args='"test",1000,"07:00:00","19:00:00",60',
    schedule_type="I",
    minutes=1,
    repeats=-1,
)
```
-> 
```
run a function `analyzer.tasks.calculate_current_difference_and_save`
with arguments of
  job = 1000
  target_illumination=1000
  sun_rise = 07:00:00
  sun_set = 19:00:00
  period_in_seconds=60
every minute
```

In the `calculate_current_difference_and_save` function, it retrieves the average illumination collected from the photosensor and caculates the average illumination.

Then, the it calculates the difference from the target illumination and save that difference in the database.
