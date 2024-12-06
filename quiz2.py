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
        "question": "1. Antes do primeiro ano de idade, seu filho (a) apresentou comportamentos precoces? (Primeiras palavras e primeiros passos.)",
        "options": ["Não sei", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "2. Seu filho (a) foi alfabetizado antes da idade recomendada?",
        "options": ["Não","Sim"],
        "points": [0, 30]
    },
    {
        "question": "3. Seu filho (a) se interessa por vários assuntos em um curto intervalo de tempo?",
        "options": ["Não sei", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "4. Seu filho (a) é mais observador que os colegas? Percebendo coisas que os demais não percebem?",
        "options": ["Não sei", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "5. A velocidade de aprendizado dele(a) surpreende você e as pessoas à sua volta?",
        "options": ["Não sei", "Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "6. Seu filho (a) tem a memória destacada especialmente em assuntos de seu interesse?",
        "options": ["Não sei", "Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
    {
        "question": "7. Seu filho (a) possui/possuia rigidez sobre coisas que não lhe interessam? Atividades escolares por exemplo.",
        "options": ["Não sei", "Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "8. Seu filho (a) procura entender a origem das coisas e utilizar palavras complicadas?",
        "options": ["Não sei", "Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "9. Seu filho (a) é intenso emocionalmente? Se preocupa demais com as coisas ao seu redor?",
        "options": ["Não sei", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
       {
        "question": "Seu filho(a) relata casos de tédio em sala de aula?",
        "options": ["Não sei", "Nunca", "Às vezes", "Frequentemente", "Sempre"],
        "points": [0, 10, 20, 30, 40]
    },
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

def get_resultado(score):
    if score <= 100:
        return "Seu filho possui um desenvolvimento dentro da normalidade neurotípica."
    elif score <= 200:
        return "Seu filho possui inteligência média, possivelmente o normal para grande parte da população. Tem a capacidade de desenvolver e se aprofundar em conhecimentos e talentos."
    elif score <= 300:
        return "Seu filho possui características de um desenvolvimento acima da média, com indícios para desenvolver Altas Habilidades. Recomendamos o acompanhamento neuropsicológico."
    elif score <= 400:
        return "Seu filho possui características significativamente acima da média, típicas de altas habilidades/superdotação. Recomendamos o acompanhamento neuropsicológico."
    else:
        return "Seu filho possui características excepcionais, típicas de altas habilidades/superdotação."

def draw_final_message(score):
    screen.fill(WHITE)
    parecer = get_resultado(score)

    final_text = font.render("Obrigada por responder!", True, BLACK)
    screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, HEIGHT // 3))
    draw_text_wrapped (screen, f"Parecer: {parecer}", font, BLUE, WIDTH // 2 - 350, HEIGHT // 2, 700)
    
    if score > 300: 
        pesquisa_text1 = "Você gostaria de contribuir para uma pesquisa em 2025?"
        pesquisa_text2 = "Acesse o formulário: [INSIRA O LINK AQUI]"
        draw_text_wrapped(screen, pesquisa_text1, font, BLACK, WIDTH // 2 - 350, HEIGHT // 2 + 100, 700)
        draw_text_wrapped(screen, pesquisa_text2, font, BLUE, WIDTH // 2 - 350, HEIGHT // 2 + 150, 700)

def draw_intro():
    screen.fill(WHITE)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Bem-vindo ao Quiz para Responsáveis!", True, BLACK)
    instructions_text = font.render("Pressione ESPAÇO para começar.", True, BLUE)
    keys_info_text = font.render("Responda usando as teclas 1, 2, 3, 4 ou 5.", True, BLACK)
    
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
    screen.blit(keys_info_text, (WIDTH // 2 - keys_info_text.get_width() // 2, HEIGHT // 2 + 50))

current_question = 0
score = 0
quiz_finished = False
running = True
state = "intro" 

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

    if state == "intro":
        draw_intro()
    elif state == "quiz":
        if current_question < len(questions):
            draw_question(questions[current_question])
    elif state == "finished":
        draw_final_message(score)

    pygame.display.flip()

pygame.quit()