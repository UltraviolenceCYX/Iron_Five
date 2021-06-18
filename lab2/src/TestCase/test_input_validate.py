import unittest
from lab2.src.StateMachine import *

class inputTest(unittest.TestCase):
    def test_add_state(self):
        fsm = FiniteStateMachine("Crossroad Traffic Light")
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a string"):
            r=fsm.add_state(None,{'Green':True, 'Yellow':False, 'Red':False})
        with self.assertRaisesRegex(TypeError, "positional argument 2 should be a type of dict"):
            r=fsm.add_state("Green",None)

    def test_add_transition(self):
        fsm = FiniteStateMachine("Crossroad Traffic Light")
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a string"):
            r = fsm.add_transition(None, "Green", "Yellow", lambda clk_n: clk_n >= 5, lambda clk_n: 1)
        with self.assertRaisesRegex(TypeError, "positional argument 2 should be a string"):
            r = fsm.add_transition("Green2Yellow", None, "Yellow", lambda clk_n: clk_n >= 5, lambda clk_n: 1)
        with self.assertRaisesRegex(TypeError, "positional argument 3 should be a string"):
            r = fsm.add_transition("Green2Yellow", "Green", None, lambda clk_n: clk_n >= 5, lambda clk_n: 1)
        with self.assertRaisesRegex(TypeError, "positional argument 4 should be a function"):
            r = fsm.add_transition("Green2Yellow", "Green", "Yellow", None, lambda clk_n: 1)
        with self.assertRaisesRegex(TypeError, "positional argument 5 should be a function"):
            r = fsm.add_transition("Green2Yellow", "Green", "Yellow", lambda clk_n: clk_n >= 5, None)

    def test_set_start_state(self):
        fsm = FiniteStateMachine("Crossroad Traffic Light")
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a string"):
            r = fsm.set_start_state(None)

    def test_execute(self):
        fsm = FiniteStateMachine("Crossroad Traffic Light")
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a string"):
            r = fsm.execute(None, 14)
        with self.assertRaisesRegex(TypeError, "positional argument 2 should be a type of int"):
            r = fsm.execute("Green", None)

    def test_set_transition(self):
        green = State("Green", {'Green': True, 'Yellow': False, 'Red': False})
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a type of Transition"):
            r = green.set_transition(None)

    def test_activate(self):
        green = State("Green", {'Green': True, 'Yellow': False, 'Red': False})
        with self.assertRaisesRegex(TypeError, "positional argument 1 should be a type of int or str"):
            r = green.activate(None)
