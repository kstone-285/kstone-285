# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random, math, time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=30):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.start_time = time.time()
        self.paused = False

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=50):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):

        if(self.paused) :
            return
        
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())
        self.now_time = time.time() - self.start_time

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(f'  Timer : {self.now_time:.1f}', font=('Arial', 12, 'bold'))

        if(is_catched) :
            self.paused = True
            self.display_score()
            return

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def display_score(self):

        end_time = time.time()
        survived_time = end_time - self.start_time

        self.drawer.clear()
        self.drawer.setpos(0,0)
        self.drawer.write(f'          GAME OVER!\n\n Your score : {survived_time:.1f} seconds', align='center', font=('Arial', 24, 'bold'))

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=15, step_turn=15):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        
        runner_pos = self.pos()
        dx = opp_pos[0] - runner_pos[0]
        dy = opp_pos[1] - runner_pos[1]
       
        angle_to_opponent = math.degrees(math.atan2(dy, dx))
        heading_diff = angle_to_opponent - self.heading()

        if heading_diff > 180:
            heading_diff -= 360
        elif heading_diff < -180:
            heading_diff += 360
      
        if abs(heading_diff) < self.step_turn:
            self.setheading(angle_to_opponent)
            self.forward(self.step_move)
        elif heading_diff > 0:
            self.left(self.step_turn)
        else:
            self.right(self.step_turn)

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    root.title("Turtle Runaway")

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("#808080")

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()


