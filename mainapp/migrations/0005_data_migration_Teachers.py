# Generated by Django 3.2.16 on 2023-01-17 15:56

from django.db import migrations


def forwards_func(apps, schema_editor):
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")
    CourseTeachers.objects.create(name_first="Роман", name_second="Доржинов", day_birth="1988-02-04").course.add(
        Courses.objects.get(id=1), Courses.objects.get(id=3)
    )
    CourseTeachers.objects.create(name_first="Ярослав", name_second="Конягин", day_birth="1981-12-08").course.add(
        Courses.objects.get(id=2)
    )


def reverse_func(apps, schema_editor):
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_data_migration_Lesson"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]