# from django_q.models import Schedule


# def create_analyzer_schedule():
#     return Schedule.objects.create(
#         func="analyzer.tasks.calculate_current_difference_and_save",
#         args='"test",1000,"07:00:00","19:00:00",60',
#         schedule_type="I",
#         minutes=1,
#         repeats=-1,
#     )
