from json.encoder import ESCAPE
import webbrowser
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
        "question": "1. Antes do seu primeiro ano de idade, você apresentou comportamentos precoces? (Primeiras palavras e primeiros passos.)",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "2. Você tem/tinha interesses aguçados, diferentes, diversos e avançados para pessoas da sua idade?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "3. Você possui muitos hiperfocos? (interesses exacerbados por tempo indeterminado)",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "4. Você acha que percebe as emoções ou intenções das pessoas dentro de padrões com facilidade?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "5. Sua velocidade de aprendizado surpreende você e as pessoas à sua volta?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "6. Você acha que as pessoas às vezes não entendem seus interesses ou suas ideias?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "7. Você se entedia com assuntos repetitivos em sala de aula?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "8. Você conhece mais palavras que seus colegas, ou palavras mais complexas que seus colegas não conhecem?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "9. Você encontra soluções e adaptações rápido para problemas?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "10. Você as vezes se percebe preocupado demais ou com suas emoções a flor da pele?",
        "options": ["Não sei", "Pouco", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
]

current_question: int = 0
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

def get_resultado(score):
    if score <= 100:
        return "Inconsistente, seu desenvolvimento é dentro da normalidade."
    elif score <= 200:
        return "Você possui inteligência média, possivelmente o normal para grande parte da população. Tem a capacidade de desenvolver e se aprofundar em conhecimentos e talentos."
    elif score <= 300:
        return "Você possui características de um desenvolvimento acima da média, com indícios para desenvolver Altas Habilidades. Recomendamos o acompanhamento neuropsicológico."
    elif score <= 400:
        return "Você possui características significativamente acima da média, típicas de altas habilidades/superdotação. Recomendamos o acompanhamento neuropsicológico."
    else:
        return "Você possui características excepcionais, típicas de altas habilidades/superdotação."


current_question = 0
score = 0
quiz_finished = False
running = True
state = "intro"

def draw_intro():
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Bem-vindo ao Quiz para Alunos (14-21)!", True, BLACK)
    instructions_text = font.render("Pressione ESPAÇO para começar.", True, BLUE)
    keys_info_text = font.render("Responda usando as teclas 1, 2, 3, 4 ou 5.", True, BLACK)
    
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
    screen.blit(keys_info_text, (WIDTH // 2 - keys_info_text.get_width() // 2, HEIGHT // 2 + 50))

def draw_final_message(score):
    screen.fill(WHITE)
    parecer = get_resultado(score)
    
    final_text = font.render("Obrigada por Responder!", True, BLACK)
    screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, HEIGHT // 3))
    draw_text_wrapped(screen, f"Parecer: {parecer}", font, BLUE, WIDTH // 2 - 350, HEIGHT // 2, 700)
    
    if score >= 300:
        pesquisa_text1 = "Você gostaria de contribuir para uma pesquisa em 2025?"
        pesquisa_text2 = "Acesse o formulário: https://forms.gle/HG7PGPpYx3dB3qr87"
        draw_text_wrapped(screen, pesquisa_text1, font, BLACK, WIDTH // 2 - 350, HEIGHT // 2 + 100, 700)
        link_font = pygame.font.Font(None, 30)
        link_surface = link_font.render(pesquisa_text2, True, BLUE)
        link_rect = link_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(link_surface, link_rect.topleft)

        return link_rect 
    return None 

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
                if event.key == ESCAPE: 
                    running = False

        # Detecta clique no link
        if event.type == MOUSEBUTTONDOWN and state == "finished": # type: ignore
            if link_rect and link_rect.collidepoint(event.pos):  
                webbrowser.open("https://forms.gle/HG7PGPpYx3dB3qr87")  

    if state == "intro":
        draw_intro()
    elif state == "quiz":
        if current_question < len(questions):
            draw_question(questions[current_question])
    elif state == "finished":
        link_rect = draw_final_message(score) 

    pygame.display.flip()

pygame.quit()
