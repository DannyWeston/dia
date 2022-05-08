import sys
from tkinter import Button, Canvas, Tk, Widget
from turtle import color

from Simulation import Simulation, SimConfig

class App:
    def __init__(self):
        # Create a window
        self.m_Window = Tk()
        self.m_Window.title("DIA Coursework - DannyWeston")
        self.m_Window.geometry("800x650")
        self.m_Window.resizable(False, False)

        # Create a canvas to draw to
        self.m_Canvas = Canvas(self.m_Window, bg = 'white')
        self.m_Canvas.place(x = 0, y = 0, width = 800, height = 600)

        # Start button
        self.m_BtnStart = Button(self.m_Window, text="Start", command=self.start_sim)
        self.m_BtnStart.place(x = 10, y = 610, width = 40, height = 30)

        # Stop button
        self.m_BtnStop = Button(self.m_Window, text="Stop", command=self.stop_sim)
        self.m_BtnStop.place(x = 60, y = 610, width = 40, height = 30)

        # Make a config for the simulation 
        self.m_Config = SimConfig()
        self.m_Config.Height = 10
        self.m_Config.Width = 10
        self.m_Config.Seed = 0

        self.maze_drawn = False

        self.m_Sim = Simulation(self.m_Config)

        self.m_Window.mainloop()

    def update(self):
        # Update the simulation
        self.m_Sim.update()

        # Update the UI
        self.m_Canvas.delete('redraw-needed')

        if not self.maze_drawn: self.draw_maze()

        # Check if the loop should continue
        if not self.m_Sim.finished: 
            self.m_Window.after(50, self.update)
            return

        print("Simulation finished")

    def draw_maze(self):
        c_width = 800 / self.m_Sim.m_World.width
        c_height = 600 / self.m_Sim.m_World.height

        map_length = self.m_Sim.m_World.map.width * self.m_Sim.m_World.map.height

        for i in range(0, map_length):
            if self.m_Sim.m_World.map.data[i] == 1:
                x1 = (i % self.m_Sim.m_World.width) * c_width
                x2 = x1 + c_width
                y1 = int(i / self.m_Sim.m_World.height) * c_height
                y2 = y1 + c_height

                self.m_Canvas.create_rectangle(x1, y1, x2, y2, fill='black')
        
        self.maze_drawn = True

    def stop_sim(self):
        # End the simulation if it is started
        self.m_Sim.end()

    def start_sim(self):
        # Start the simulation if its not already started
        if not self.m_Sim.finished:
            self.m_Window.after(50, self.update)

def main(args):
    App()

if __name__ == "__main__":
    main(sys.argv)