class bin_node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.right = right_child
        self.left = left_child

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_left(self, bin_node):
        self.left = bin_node

    def set_right(self, bin_node):
        self.right = bin_node

    def has_left(self):
        if self.get_left() != None:
            return True
        else:
            return False

    def has_right(self):
        if self.get_right() != None:
            return True
        else:
            return False
# I am going to use the inorder system of searching, meaning left-root-right