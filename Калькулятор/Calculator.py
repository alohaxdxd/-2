class Calculator:
    """
    Класс для выполнения арифметических операций.
    """

    def add(self, operand1: float, operand2: float) -> float:
        """
        Суммирует два числа.

        Args:
            operand1: Первое число.
            operand2: Второе число.

        Returns:
            Сумма двух чисел.
        """
        return operand1 + operand2

    def subtract(self, minuend: float, subtrahend: float) -> float:
        """
        Вычитает одно число из другого.

        Args:
            minuend: Уменьшаемое.
            subtrahend: Вычитаемое.

        Returns:
            Результат вычитания.
        """
        return minuend - subtrahend

    def multiply(self, factor1: float, factor2: float) -> float:
        """
        Умножает два числа.

        Args:
            factor1: Первый множитель.
            factor2: Второй множитель.

        Returns:
            Произведение двух чисел.
        """
        return factor1 * factor2

    def divide(self, dividend: float, divisor: float) -> float:
        """
        Делит одно число на другое.

        Args:
            dividend: Делимое.
            divisor: Делитель.

        Returns:
            Результат деления.

        Raises:
            ZeroDivisionError: Если делитель равен нулю.
        """
        if divisor == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return dividend / divisor