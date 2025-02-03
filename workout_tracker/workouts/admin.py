from django.contrib import admin
from .models import User, Exercise, WorkoutPlan, WorkoutExercise, WorkoutSession

# Registrar el modelo de usuario personalizado
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Registrar el modelo de Exercise
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)

# Registrar el modelo de WorkoutPlan
@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'created_at')
    search_fields = ('name', 'user__username')

# Registrar el modelo de WorkoutExercise
@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_plan', 'exercise', 'sets', 'reps', 'weight')
    search_fields = ('workout_plan__name', 'exercise__name')

# Registrar el modelo de WorkoutSession
@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_plan', 'date', 'status')
    search_fields = ('workout_plan__name',)

