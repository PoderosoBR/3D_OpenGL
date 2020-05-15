'''glfw:Graphics Library Framework e permite que programadores possam criar e gerenciar janelas e contextos OpenGL,
 assim como interagir com joysticks, mouses e teclados.'''

import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos

#iniciou  GLFW
glfw.init()

# cria a janela (comprimento, largura, titulo, none,none)
window = glfw.create_window(800,400, "3D com OpenGL", None, None)

# Definica a posicao da janela (nome_janela , PosX , posY)
glfw.set_window_pos(window, 400, 200)

# # Esta função atualiza o contexto OpenGL ou OpenGL ES da janela especificada no encadeamento de chamada.
glfw.make_context_current(window)

#Vertice do triangulo
vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0]

# cor do triangulo
colors = [1.0, 1.0, 0.0,
          0.0, 0.0, 0.0,
          0.0, 0.0, 0.0]

vertices = np.array(vertices, dtype=np.float32) # Array Vertices do tipo Float
colors = np.array(colors, dtype=np.float32)  # Array Cores do tipo Float

''' 
glEnableClientState: Especifica a capacidade de ativar. Constantes simbólicas GL_COLOR_ARRAY , GL_EDGE_FLAG_ARRAY ,
# GL_FOG_COORD_ARRAY , GL_INDEX_ARRAY , GL_NORMAL_ARRAY , GL_SECONDARY_COLOR_ARRAY , GL_TEXTURE_COORD_ARRAY
# e GL_VERTEX_ARRAY são aceitas.
'''
'''
    GL_VERTEX_ARRAY: Se ativada, a matriz de vértices é ativada para gravação e usada durante a renderização quando glDrawArrays
    ou glDrawElements é chamado. Veja glVertexPointer.
'''
glEnableClientState(GL_VERTEX_ARRAY)

#definir uma matriz de dados de vértice (tamanho , tipo , indices , vertices )
glVertexPointer(3, GL_FLOAT, 0, vertices)

'''
    GL_COLOR_ARRAY: Se ativada, a matriz de cores é ativada para gravação e usada durante a renderização quando
     glDrawArrays ou glDrawElements é chamado. Veja glColorPointer
'''
glEnableClientState(GL_COLOR_ARRAY)

#definir uma matriz de dados de vértice (tamanho , tipo , indices , Cores )

glColorPointer(3, GL_FLOAT, 0, colors)

glClearColor(0, 0.1, 0.5, 1) # muda cor de fundo Aceita 0.0 ate 1.0



# window_should_close : fecha a janela
while not glfw.window_should_close(window):
   #ler os eventos da janela(mouse em cima da janela é um evento)
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT) # limpa o baffer de bits das cores

    glLoadIdentity() # atualiza  as configurações
    ct = glfw.get_time()  # retorna o tempo decorrido, pois init foi chamado

    #  ESCALA (X,Y,Z)
    glScale(abs(sin(ct)), abs(sin(ct)), abs(sin(ct)))

    # Rotacao (Angulo,x,y,z)
    glRotatef( 45, abs(sin(ct)), abs(sin(ct)), abs(cos(ct)))

    # translacao (x,y,z)
    glTranslatef(0, abs(cos(ct)), 0)

#Desenha um (Tipo_Desenho, Numero_Indices, Numero_Vertices)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window) # serve para atualizar a janela

# encerra glfw
glfw.terminate()

