# python-explicit-aspect

## How to install
* Using pip:
    ```bash
    poetry install git+https://github.com/Gamazic/python-explicit-aspect
    ```

* Using poetry:
    ```bash
    pip install git+https://github.com/Gamazic/python-explicit-aspect
    ```


## Example

* Business module:
    ```python
    import aspect

    from aspect_logic import LogCar


    @aspect.bind(LogCar)
    class Car:
        def __init__(self, car_speed):
            self.__car_speed = car_speed

        def move(self, rotation):
            print(f'move {rotation} with {self.__car_speed:=}')
    ```
* Aspect module:
    ```python
    import aspect


    class LogCar(aspect.BaseAspect):
        @aspect.how(aspect.AdviceType.BEFORE)
        def move(self, rotation):
            print('!!!"before" aspect!!!')

        @aspect.how(aspect.AdviceType.AFTER)
        def move(self, rotation):
            print('!!!"after" aspect!!!')
    ```

* Run example:
    ```python
    from business_logic import Car

    c = Car(1)
    c.move('forward')
    ```
    Output:
    ```
    !!!"before" aspect!!!
    move forward with 1
    !!!"after" aspect!!!
    ```