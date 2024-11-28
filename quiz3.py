import pygame
from pygame.locals import *
pygame.init()

# STYLE
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz 3")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
font = pygame.font.Font(None, 36)

questions = [
    {
        "question": "Você gosta de explorar novos lugares?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Você sente facilidade em aprender coisas novas?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Você prefere resolver problemas sozinho(a)?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    },
    {
        "question": "Você gosta de assumir responsabilidades?",
        "options": ["Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [10, 20, 30, 40]
    }
]

current_question = 0
score = 0
running = True

def draw_question(question_data):
    """Desenha a pergunta e as opções na tela."""
    screen.fill(WHITE)
    question_text = font.render(question_data["question"], True, BLACK)
    screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 50))

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
