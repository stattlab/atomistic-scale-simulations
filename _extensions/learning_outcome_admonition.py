from docutils.parsers.rst.directives.admonitions import Admonition

# attention, caution, danger, error, hint, important, note, tip, and warning
class LearningOutcome(Admonition):
    """Learning Outcome admonition."""

    def run(self):
        # Manually add a "tip" class to style it
        if "class" not in self.options:
            self.options["class"] = ["tip"]
        else:
            self.options["class"].append("tip")
        # add title to box    
        self.arguments[0] = f"Learning Outcomes: {self.arguments[0]}"
        return super().run()


def setup(app):
    app.add_directive("learningoutcome", LearningOutcome)
