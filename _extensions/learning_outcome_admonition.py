from docutils.parsers.rst.directives.admonitions import Admonition


class LearningOutcome(Admonition):
    """Learning Outcome admonition."""

    def run(self):
        self.arguments[0] = f"Learning Outcomes: {self.arguments[0]}"
        return super().run()


def setup(app):
    app.add_directive("learningoutcome", LearningOutcome)
