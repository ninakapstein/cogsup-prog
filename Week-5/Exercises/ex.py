from expyriment import design, control, stimuli

exp = design.Experiment(name="ex 1")

""" Global settings """
control.set_develop_mode()
control.initialize(exp)

text = stimuli.TextLine("Press a key")
text.present()

key = exp.keyboard.wait()

#This does not work
text2 = stimuli.TextLine("You pressed", print(key))

text2.present()

exp.clock.wait(3000)

control.end