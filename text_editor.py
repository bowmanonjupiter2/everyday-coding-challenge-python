import unittest


class TextEditor:
    text = ""

    ops_stack = []
    undo_stack = []
    redo_stack = []

    class AddOperation:
        def __init__(self, ops: str, s: str):
            self.ops = ops
            self.s = s

    class DeleteOperation:
        def __init__(self, ops: str, k: int):
            self.ops = ops
            self.k = k

    def add_text(self, s: str):
        if len(self.redo_stack) > 0:
            self.redo_stack = []
            self.undo_stack = []

        self.text += s
        self.ops_stack.append(self.AddOperation("ADD", s))
        self.undo_stack.append(self.DeleteOperation("DEL", len(s)))

    def delete_text(self, k: int) -> int:
        if len(self.redo_stack) > 0:
            self.redo_stack = []
            self.undo_stack = []

        actual_k = min(k, len(self.text))

        self.ops_stack.append(self.DeleteOperation("DEL", actual_k))
        self.undo_stack.append(self.AddOperation("ADD", self.text[-actual_k:]))
        self.text = self.text[:-actual_k]

    def undo(self):
        if len(self.undo_stack) > 0:
            ops = self.undo_stack.pop()
            self.redo_stack.append(self.ops_stack.pop())

            if ops.ops == "DEL":
                self.text = self.text[:-ops.k]
            else:
                self.text += ops.s

    def redo(self):
        if len(self.redo_stack) > 0:
            ops = self.redo_stack.pop()

            if ops.ops == "DEL":
                self.text = self.text[:-ops.k]
            else:
                self.text += ops.s


class TestTextEditor(unittest.TestCase):
    def test_add_text(self):
        editor = TextEditor()
        editor.add_text("Hello")
        self.assertEqual(editor.text, "Hello")

    def test_delete_text(self):
        editor = TextEditor()
        editor.add_text("Hello")
        editor.delete_text(2)
        self.assertEqual(editor.text, "Hel")

    def test_undo_add(self):
        editor = TextEditor()
        editor.add_text("Hello")
        editor.undo()
        self.assertEqual(editor.text, "")

    def test_undo_delete(self):
        editor = TextEditor()
        editor.add_text("Hello")
        editor.delete_text(2)
        editor.undo()
        self.assertEqual(editor.text, "Hello")

    def test_redo_add(self):
        editor = TextEditor()
        editor.add_text("Hello")
        editor.undo()
        editor.redo()
        self.assertEqual(editor.text, "Hello")

    def test_redo_delete(self):
        editor = TextEditor()
        editor.add_text("Hello")
        editor.delete_text(2)
        editor.undo()
        editor.redo()
        self.assertEqual(editor.text, "Hel")


if __name__ == "__main__":
    unittest.main()
