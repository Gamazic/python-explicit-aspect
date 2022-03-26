import aspect


class LogCar(aspect.BaseAspect):
    @aspect.how(aspect.AdviceType.BEFORE)
    def move(self, rotation):
        print('!!!!"before" aspect!!!')

    @aspect.how(aspect.AdviceType.AFTER)
    def move(self, rotation):
        print('!!!"after" aspect!!!')
