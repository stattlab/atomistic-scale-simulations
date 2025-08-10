from docutils.parsers.rst.directives.admonitions import Admonition


class Exercise(Admonition):
    """Example admonition."""

    def run(self):
        # Manually add a "tip" class to style it
        if "class" not in self.options:
            self.options["class"] = ["note"]
        else:
            self.options["class"].append("note")

        self.arguments[0] = f"Exercise: {self.arguments[0]}"
        return super().run()


def setup(app):
    app.add_directive("exercise", Exercise)
