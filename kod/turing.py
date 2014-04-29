#!/usr/bin/python
# -*- Coding:utf-8 -*-

# ALPHA = 0,1,#
# S1: final|start|
#    0->0,L,S2;
#     ->1,R,S2;
#
#

import re

ParityTM = """
ALPHA = 0,1,#

ODD:
    0->,R,ODD
    1->,R,EVEN
    #->,R,FODD

EVEN: start
    0->,R,EVEN
    1->,R,ODD
    #->,R,FEVEN

FODD: final
FEVEN: final
"""

class TM(object):
    ALPHA_PAT = re.compile('^\s*ALPHA\s*=(?P<alphabet>.*)\s*$', re.IGNORECASE)
    HEAD_PAT  = re.compile('^\s*(?P<statename>\w+):\s*(?P<type>.*)\s*$')
    TRANS_PAT = re.compile('^\s*(?P<inletter>.*)\s*->(?P<outletter>.{0,1})\s*,\s*(?P<direction>[RL])\s*,\s*(?P<state>\w+)\s*.*$', re.IGNORECASE)

    def __init__(self):
        self.alphabet=[]
        self.states = {}
        self.final_states = []
        self.start_state = None
        self._tape=[]
        self._head_pos = 0
        self.current_state=None

    def load(self,definition):
        lines = definition.split('\n')
        self.alphabet=[]
        self.states = {}
        self.final_states = []
        self.start_state = None
        self.current_state = None
        current_state_name = None
        current_state_transmap = {}
        for l in lines:
            m = self.ALPHA_PAT.match(l)
            if m:
                self.alphabet = m.groupdict()['alphabet'].strip().split(',')
                continue
            m = self.HEAD_PAT.match(l)
            if m:
                m = m.groupdict()
                if current_state_name:
                    self.states[current_state_name] = current_state_transmap
                current_state_transmap={}
                current_state_name = m['statename']
                if 'final' in m['type']:
                    self.final_states.append(current_state_name)
                if 'start' in m['type'] or self.start_state is None:
                    self.start_state = current_state_name
                continue
            m = self.TRANS_PAT.match(l)
            if m:
                m = m.groupdict()
                inletters = m['inletter'].split(',')
                action = (m['outletter'],m['direction'],m['state'])
                for let in inletters:
                    current_state_transmap[let]=action
        if current_state_name:
            self.states[current_state_name] = current_state_transmap
        self.current_state = self.start_state

    def step(self):
        trans = self.states[self.current_state]
        inletter = self._tape[self._head_pos]
        if inletter not in trans:
            inletter = ''
        outletter,direction,targetstate = trans[self._tape[self._head_pos]]
        if len(outletter) > 0:
            self._tape[self._head_pos] = outletter
        if direction == 'L':
            self._head_pos -= 1
        else:
            self._head_pos += 1
        if self._head_pos < 0:
            self._head_pos = 0
        self.current_state = targetstate
        if self.current_state in self.final_states:
            return False
        return True

    def run(self,max_steps=1000):
        step = 0
        while step < max_steps and self.step():
            step += 1





