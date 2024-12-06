import pygame
from pygame.locals import *
import webbrowser

pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz para Alunos (14-21)")

questions = [
    {"question": "1. Como você avalia a sua compreensão sobre o tema proposto?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "2. Você costuma discutir este tema com seus colegas?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "3. Você já leu algum material sobre o tema?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "4. Como você descreveria sua participação em atividades relacionadas ao tema?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "5. Você sente que suas ações têm impacto sobre esse tema?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "6. Você já discutiu esse tema com professores ou outros especialistas?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "7. Você acha que o tema é importante para a sociedade?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "8. Você já participou de algum evento relacionado a esse tema?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "9. Você sente que pode influenciar mudanças em relação a esse tema?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
    {"question": "10. Você acredita que a conscientização sobre esse tema é suficiente?",
     "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"], "points": [0, 10, 20, 30, 40]},
]

current_question = 0
score = 0
running = True
state = "intro"

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


def draw_intro():
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Bem-vindo ao Quiz para Professores", True, BLACK)
    instructions_text = font.render("Pressione ESPAÇO para começar.", True, BLUE)
    keys_info_text = font.render("Responda usando as teclas 1, 2, 3, 4 ou 5.", True, BLACK)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
    screen.blit(keys_info_text, (WIDTH // 2 - keys_info_text.get_width() // 2, HEIGHT // 2 + 50))


def draw_final_message():
    screen.fill(WHITE)
    final_text = font.render("Obrigada por Responder!", True, BLACK)
    screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, HEIGHT // 3))

    pesquisa_text1 = "Contribua para uma pesquisa em 2025!"
    pesquisa_text2 = "Acesse o formulário: https://forms.gle/HG7PGPpYx3dB3qr87"
    draw_text_wrapped(screen, pesquisa_text1, font, BLACK, WIDTH // 2 - 350, HEIGHT // 2, 700)

    link_font = pygame.font.Font(None, 30)
    link_surface = link_font.render(pesquisa_text2, True, BLUE)
    link_rect = link_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(link_surface, link_rect.topleft)

    return link_rect


link_rect = None

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if state == "intro":
                if event.key == K_SPACE:
                    state = "quiz"
            elif state == "quiz":
                if event.key in [K_1, K_2, K_3, K_4, K_5]:
                    selected_option = event.key - K_1
                    if 0 <= selected_option < len(questions[current_question]["points"]):
                        score += questions[current_question]["points"][selected_option]
                        current_question += 1
                        if current_question >= len(questions):
                            state = "finished"
            elif state == "finished":
                if event.key == K_ESCAPE:
                    running = False

        if event.type == MOUSEBUTTONDOWN and state == "finished":
            if link_rect and link_rect.collidepoint(event.pos):
                webbrowser.open("https://forms.gle/HG7PGPpYx3dB3qr87")

    if state == "intro":
        draw_intro()
    elif state == "quiz":
        if current_question < len(questions):
            draw_question(questions[current_question])
    elif state == "finished":
        link_rect = draw_final_message()

    pygame.display.flip()

pygame.quit()
