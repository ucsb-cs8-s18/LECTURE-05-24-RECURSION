
def addOneToCount(countdict, key):
  " add one to entry for key in dictionary of counts"
  if key in countdict:
    countdict[key]+=1
  else:
    countdict[key]=1
  return countdict


def test_addOneToCount_1():
  assert addOneToCount({},"a")=={"a":1}

def test_addOneToCount_2():
  assert addOneToCount({'a':1,'b':2},"b")=={"a":1,"b":3}

def test_addOneToCount_3():
  assert addOneToCount({'a':1,'b':2},"c")=={"a":1,"b":2,'c':1}


def countchars(s):
  if len(s)==0:
    return {}
  first = s[0]
  rest = s[1:]
  countdict_rest = countchars(rest)
  print(' first=',first,
        ' rest=',rest,
        ' countdict_rest=',countdict_rest)
  return addOneToCount(countdict_rest,first)
  
  
def test_countchars_base():
  assert countchars("")=={}
  
def test_countchars_1():
  assert countchars("UCSB")=={'U':1,'C':1,'S':1,'B':1}

def test_countchars_2():
  assert countchars("UC Santa Barbara")=={'U':1,'C':1,' ':2,'S':1,
                                         'a': 5, 'n':1,'t':1,
                                         'B':1,'r':2, 'b':1}
