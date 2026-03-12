import expyriment

expyriment.control.set_develop_mode()

#Set up experiment
exp = expyriment.design.Experiment(name = "edge experiment")
expyriment.control.initialize(exp)
expyriment.control.start(exp)


width, height = exp.screen.size

square_size = int(width * 0.05)

square_edge = square_size//2

left = -width // 2 + square_edge
right = width // 2 - square_edge
top = height // 2 - square_edge
bottom = -height // 2 + square_edge


rect1 = expyriment.stimuli.Rectangle(size = (square_size, square_size), line_width =1, colour = (255, 0, 0), position = (left, bottom))
rect2 = expyriment.stimuli.Rectangle(size = (square_size, square_size), line_width =1, colour = (255, 0, 0), position = (right, bottom))
rect3 = expyriment.stimuli.Rectangle(size = (square_size, square_size), line_width =1, colour = (255, 0, 0), position = (left, top))
rect4 = expyriment.stimuli.Rectangle(size = (square_size, square_size), line_width =1, colour = (255, 0, 0), position = (right, top))

#Show the square
rect1.present(clear = True, update= False)
rect2.present(clear = False, update= False)
rect3.present(clear = False, update= False)
rect4.present(clear = False, update= True)

exp.keyboard.wait()

#End experiment
expyriment.control.end()
