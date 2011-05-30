#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Code skeleton for ThePythonGameBook examples
"""

####

import pygame

####

class PygView(object):

  
    def __init__(self, width=800, height=600, fps=50, backcol=(0,0,0)):
        
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        pygame.display.set_caption("Press ESC to quit")

        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill(backcol)
       

    def run(self):
        """
        The mainloop
        """
        running = True
        while running:
            self.flip()    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False          
        pygame.quit()


    def flip(self):

         pygame.display.flip()
         self.clock.tick(self.fps)
         self.screen.blit(self.background, (0, 0))

####

if __name__ == '__main__':

    PygView().run()
