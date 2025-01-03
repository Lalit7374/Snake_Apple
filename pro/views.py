from django.shortcuts import render
from django.http import JsonResponse
import random

def game_page(request):
    
    return render(request, 'pro/index.html')

DIRECTIONS = {
    'UP': (0, -20),
    'DOWN': (0, 20),
    'LEFT': (-20, 0),
    'RIGHT': (20, 0)
}

def start_game(request):
    """Initialize the game state."""
    snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake positions
    direction = 'RIGHT'
    apple = generate_apple(snake)
    game_state = {'snake': snake, 'apple': apple, 'direction': direction, 'score': 0}
    return JsonResponse(game_state)

def move_snake(request):
    """Update the snake's position and handle collisions."""
    snake = [tuple(map(int, seg.split(','))) for seg in request.GET.get('snake', '').split(';')]
    direction = request.GET.get('direction', 'RIGHT')
    apple = tuple(map(int, request.GET.get('apple', '').split(',')))
    score = int(request.GET.get('score', 0))

    head = snake[0]
    dx, dy = DIRECTIONS[direction]
    new_head = (head[0] + dx, head[1] + dy)

    # Check for collision with the walls
    if new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400:
        return JsonResponse({'gameOver': True})

    # Check for collision with the snake itself
    if new_head in snake:
        return JsonResponse({'gameOver': True})

    # Check for collision with the apple
    if new_head == apple:
        snake.append(snake[-1])  # Grow snake
        apple = generate_apple(snake)
        score += 10
    else:
        snake = [new_head] + snake[:-1]

    return JsonResponse({'snake': snake, 'apple': apple, 'direction': direction, 'score': score, 'gameOver': False})

def generate_apple(snake):
    """Generate a new apple at a random position."""
    while True:
        apple = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)  # Adjusted for grid size
        if apple not in snake:
            break
    return apple
