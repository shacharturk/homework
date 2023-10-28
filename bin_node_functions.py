from bin_node import bin_node


def how_many(node, val):
    same, left, right = 0, 0, 0
    if node.has_left():
        left = how_many(node.get_left(), val)
    if node.get_value() == val:
        same = 1
    if node.has_right():
        right = how_many(node.get_right(), val)
    return same + left + right


def are_all(tree, str):#checks if all of the characters in a given string are in a binary tree
      def equalize(left, right):#returns the characters that appear in both of the strings
            str = ""
            if (right == "" or left == ""):
              return ""
            for x in right:
              if x in left:
                str += x
            return str

      def is_in(tree, str):
          right, left = str, str
          if tree.has_left():
            left = (is_in(tree.get_left(), str))
          if tree.has_right():
            right = (is_in(tree.get_right(), str))
          combine = equalize(left, right)
          str=equalize(combine, str)
          if tree.get_value() in str:
            str = str.replace(tree.get_value(), "")#removes the character in the current node from the string
          return str
      d =is_in(tree, str)
      if d == "":
          return True
      else:
          return False
      
      
def scan(tree):
      left,right = "", ""
      if tree.has_left():
        left = scan(tree.get_left())
      val = tree.get_value()
      if tree.has_right():
        right = scan(tree.get_right())
      return left + val + right
#I did not make the function an internal function,
# because I'll use it for the next question as well


def is_pallindrom(tree):
    txt = scan(tree)
    for x in range(0, len(txt)//2):
        if txt[x] != txt[len(txt)-x-1]:
            return False
    return True


def compressed(tree):
    def tree_to_string(tree):
          #if (tree.get_value()=None):
            #return None
        compress = 'bin_node('
        val = tree.get_value()
        if type(val) == str:
            compress += '"'+tree.get_value()+'",'
        else:
            compress += tree.get_value()+','
        if tree.has_left():
            compress += tree_to_string(tree.get_left())+','
        else:
            compress += 'None,'
        if tree.has_right():
            compress += tree_to_string(tree.get_right())+')'
        else:
            compress += 'None)'
        return compress
    file = open("result.txt", "w")
    file.write(tree_to_string(tree))
    file.close()
    print("file name - result.txt")

def decompressed(txt):
    def string_to_tree(txt):
        if txt[:4] == 'None':
          txt = txt[4:]#trimming the text
          return None,txt
        #creating a new binary node
        txt=txt[9:]#removing the 'bin_node' text
          #finding its value and removig the value part
        if txt[0] == '"':#if the value is a string
          txt = txt[1:]
          val = txt.split(chr(34),1)
          n=bin_node(val[0])
          txt = val[1][1:]#removing the coma
        else:#if the value is a number
            val = txt.split(',', 1)
            n = bin_node(val[0])
            txt = val[1]
        #creating the left branch
        left = string_to_tree(txt)
        n.set_left(left[0])
        txt = left[1]#we want to get the text without the parts that were already visited inside the 'left' call
        txt = txt[1:]#removing the coma
        #creating the right branch
        right = string_to_tree(txt)
        n.set_right(right[0])
        txt = right[1]
        txt = txt[1:]#removing the closing bracket
        return n, txt
    return string_to_tree(txt)[0]


