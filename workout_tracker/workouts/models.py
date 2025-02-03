from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Solución: Evita conflicto con `groups` y `user_permissions`
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Evita colisión con `auth.User.groups`
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Evita colisión con `auth.User.user_permissions`
        blank=True
    )

    def __str__(self):
        return self.username

    
class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_plans")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name="exercises")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Opcional

    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"

class WorkoutSession(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
    ]

    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name="sessions")
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.workout_plan.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"
