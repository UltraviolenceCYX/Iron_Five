import unittest
from lab2.src.StateMachine import *


class TextParsingTest(unittest.TestCase):
    def test_state_machine(self):
        fsm = FiniteStateMachine("text parsing")
        fsm.add_state("start_a",{'a*': True, 'b*':  False, 'c': False})
        fsm.add_state("middle_b",{'a*': False, 'b*': True, 'c': False})
        fsm.add_state("end_c", {'a*': False, 'b*': False, 'c': True})
        fsm.add_state("error", {'a*': False, 'b*': False, 'c': False})

        fsm.add_transition("a to a","start_a","start_a",lambda i: i == 'a', lambda clk_n: 1)
        fsm.add_transition("a to error", "start_a", "error", lambda i: i != 'a' and i != 'b', lambda clk_n: 1)
        fsm.add_transition("a to b", "start_a", "middle_b", lambda i: i == 'b', lambda clk_n: 1)
        fsm.add_transition("b to b", "middle_b", "middle_b", lambda i: i == 'b',lambda clk_n: 1)
        fsm.add_transition("b to error", "middle_b", "error", lambda i: i != 'b' and i != 'c', lambda clk_n: 1)
        fsm.add_transition("b to c", "middle_b", "end_c", lambda i: i == 'c', lambda clk_n: 1)
        fsm.add_transition("c to error", "end_c", "error", lambda i: True, lambda clk_n: 1)
        fsm.add_transition("error to error", "error", "error", lambda i: True, lambda clk_n: 1)


        #the fsm is going to match string like 'a*b*c', matched return true, not matched return false

        res = fsm.text("abbc")
        self.assertEqual(res, True)

        res = fsm.text("abbcddd")
        self.assertEqual(res, False)

        res = fsm.text("abc")
        self.assertEqual(res, True)

        res = fsm.text("c")
        self.assertEqual(res, False)

        res = fsm.text("aabc")
        self.assertEqual(res, True)

