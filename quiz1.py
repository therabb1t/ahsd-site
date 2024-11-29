import pygame
from pygame.locals import *
pygame.init()

# STYLE
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz 1")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
font = pygame.font.Font(None, 36)

questions = [
    {
        "question": "Você se sente frustrado(a) quando algo não sai exatamente como esperava?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Você acha que percebe as emoções ou intenções das pessoas com facilidade?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Já sentiu que era difícil explicar para os outros o que você pensa ou sente?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Você acha que as pessoas às vezes não entendem seus interesses ou suas ideias?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    }
]

current_question = 0
score = 0
running = True

def draw_text_wrapped(surface, text, font, color, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if font.size(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y + i * font.get_linesize()))

def draw_question(question_data):
    screen.fill(WHITE)
    draw_text_wrapped(screen, question_data["question"], font, BLACK, WIDTH // 2 - 350, 50, 700)

    for i, option in enumerate(question_data["options"]):
        option_text = font.render(f"{i + 1}. {option}", True, BLUE)
        screen.blit(option_text, (100, 150 + i * 50))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_1, K_2, K_3, K_4]:  
                selected_option = event.key - K_1
                score += questions[current_question]["points"][selected_option]  
                current_question += 1
                if current_question >= len(questions):  
                    print(f"Pontuação final: {score}")  
                    running = False

    if current_question < len(questions):
        draw_question(questions[current_question])
    else:
        screen.fill(WHITE)
        final_text = font.render("Quiz encerrado! Veja sua pontuação no console.", True, BLACK)
        screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, HEIGHT // 2 - final_text.get_height() // 2))

    pygame.display.flip()

pygame.quit()
