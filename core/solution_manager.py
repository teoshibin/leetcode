
from typing import Dict, Optional
from core.abstract_solution import AbstractSolution

class SolutionManager:
    _solution_classes = {}

    @classmethod
    def register(cls, solution_class: type) -> None:
        if not issubclass(solution_class, AbstractSolution):
            raise TypeError(f"Expected subclass of AbstractSolution, got {solution_class}")
        cls._solution_classes[solution_class.__name__] = solution_class

    @classmethod
    def unregister(cls, solution: str | int) -> None:
        if type(solution) == str:
            if solution in cls._solution_classes:
                del cls._solution_classes[solution]
        elif type(solution) == int:
            if len(cls._solution_classes) > solution:
                solution_name = list(cls._solution_classes.keys())[solution]
                del cls._solution_classes[solution_name]

    @classmethod
    def get(cls, solution: str | int) -> Optional[type]:
        if type(solution) == int:
            return cls._solution_classes.get(list(cls._solution_classes.keys())[solution])
        return cls._solution_classes.get(solution)

    @classmethod
    def get_all(cls) -> Dict[str, type]:
        return cls._solution_classes

    @classmethod
    def register_from_module(cls, module) -> None:
        """
        Register all solution classes from a module.

        Args:
            module (ModuleType): The module

        Raises:
            TypeError: If a class in the module is not a subclass of AbstractSolution
        """
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, AbstractSolution) and attr is not AbstractSolution:
                cls.register(attr)

