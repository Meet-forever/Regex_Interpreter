
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EPSILON LETTER LPAREN PLUS RPAREN SEMI STARstart : re SEMIre : re PLUS termre : termterm : term factorterm : factorfactor : factor STARfactor : basementbasement : LETTERbasement : EPSILONbasement : LPAREN re RPAREN'
    
_lr_action_items = {'LETTER':([0,3,4,5,6,7,8,10,11,12,14,15,],[6,6,-5,-7,-8,-9,6,6,-4,-6,6,-10,]),'EPSILON':([0,3,4,5,6,7,8,10,11,12,14,15,],[7,7,-5,-7,-8,-9,7,7,-4,-6,7,-10,]),'LPAREN':([0,3,4,5,6,7,8,10,11,12,14,15,],[8,8,-5,-7,-8,-9,8,8,-4,-6,8,-10,]),'$end':([1,9,],[0,-1,]),'SEMI':([2,3,4,5,6,7,11,12,14,15,],[9,-3,-5,-7,-8,-9,-4,-6,-2,-10,]),'PLUS':([2,3,4,5,6,7,11,12,13,14,15,],[10,-3,-5,-7,-8,-9,-4,-6,10,-2,-10,]),'RPAREN':([3,4,5,6,7,11,12,13,14,15,],[-3,-5,-7,-8,-9,-4,-6,15,-2,-10,]),'STAR':([4,5,6,7,11,12,15,],[12,-7,-8,-9,12,-6,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'re':([0,8,],[2,13,]),'term':([0,8,10,],[3,3,14,]),'factor':([0,3,8,10,14,],[4,11,4,4,11,]),'basement':([0,3,8,10,14,],[5,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> re SEMI','start',2,'p_start','REParser.py',19),
  ('re -> re PLUS term','re',3,'p_re','REParser.py',24),
  ('re -> term','re',1,'p_re_base','REParser.py',28),
  ('term -> term factor','term',2,'p_term','REParser.py',32),
  ('term -> factor','term',1,'p_term_base','REParser.py',36),
  ('factor -> factor STAR','factor',2,'p_factor','REParser.py',40),
  ('factor -> basement','factor',1,'p_factor_base','REParser.py',44),
  ('basement -> LETTER','basement',1,'p_basement_letter','REParser.py',48),
  ('basement -> EPSILON','basement',1,'p_basement_epsilon','REParser.py',52),
  ('basement -> LPAREN re RPAREN','basement',3,'p_basement_re_run','REParser.py',56),
]