import doctest


class ObjectColor:
    """
    Класс, представляющий цветной объект.

    :param name: Название объекта.
    :param color: Цвет объекта.

    Пример:
    >>> obj = ObjectColor("Generic Object", "Red")
    """

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def describe_object(self) -> str:
        """
        Способ представления описания объекта.

        :return: Описание объекта.
        """
        ...

    def perform_action(self, action: str) -> None:
        """
        Метод для выполнения действия над объектом.

        :param action: Дейтсвие, которое должно быть выполнено.
        """
        ...


class MaterialEntity(ObjectColor):
    """
    Класс представляющий матреиал объекта.

    :param material_type: Тип материала.
    :param weight: Вес материала.

    Пример:
    >>> entity = MaterialEntity("Деревянный стол", "Коричневый", "Дерево", 15.0)
    """

    def __init__(self, name: str, color: str, material_type: str, weight: float):
        super().__init__(name, color)
        self.material_type = material_type
        self.weight = weight

    def calculate_volume(self) -> float:
        """
        Метод расчета объема материала.

        :return: Объем материала.
        """
        ...

    def break_entity(self) -> str:
        """
        Метод для симуляции разрушения материального объекта.

        :return: Сообщение, указывающее, что объект поврежден.
        """
        ...


class ImmaterialEntity(ObjectColor):
    """
    Класс представляющий нематериальный объект.

    :param transparency_level: Уровень прозрачности.
    :param energy_type: Тип связанной энергии.

    Пример:
    >>> entity = ImmaterialEntity("Невидимая сила", "Невидимый", 0.9, "Неизвестен")
    """

    def __init__(self, name: str, color: str, transparency_level: float, energy_type: str):
        super().__init__(name, color)
        self.transparency_level = transparency_level
        self.energy_type = energy_type

    def manipulate_energy(self, action: str) -> None:
        """
        Метод манипулирования энергией, связанной с нематериальный объектом.

        :param action: Действие, которое должно быть выполнено с энергией.
        """
        ...

    def become_visible(self) -> None:
        """
        Способ сделать нематериальную сущность видимой.

        :return: None
        """


class AbstractLivingBeing(ObjectColor):
    """
        Класс представляющий живое существо.

        :param species: Вид существа.
        :param lifespan: Продолжительность жизни.

        Examples:
        >>> being = AbstractLivingBeing("Человек", "Коричневый", "Homo sapiens", 80)
        """

    def __init__(self, name: str, color: str, species: str, lifespan: int):
        super().__init__(name, color)
        self.species = species
        self.lifespan = lifespan

    def age(self, years: int) -> None:
        """
            Метод моделирования процесса старения живого существа..

            :param years: Количество лет, на которые стареет существо.
            :return: None
            """
        ...

    def communicate(self, message: str) -> str:
        """
            Способ общения существа.

            :param message: Информация, подлежащая передаче.
            :return: Ответ на переданную информацию.
            """
        ...


if __name__ == "__main__":
    doctest.testmod()
