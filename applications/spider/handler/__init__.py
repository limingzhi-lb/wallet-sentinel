
class Processer(object):

    def __init__(self) -> None:
        self.valid_tasks = self._get_valid_tasks()
        self.processed_tasks = []
        self.failed_tasks = []

    def _get_valid_tasks(self):
        """
        获取所有任务
        """
        # todo 从models里获取，不同平台的链接要有不同的kind
        return ['https://item.jd.com/7836786.html']

    def process(self):
        for task in self.valid_tasks:
            base = BaseTask(task)
            res = base.execute()
            if res:
                self.processed_tasks.append(task)
            else:
                self.failed_tasks.append(task)


class BaseTask(object):

    def __new__(cls, *args, **kwargs):
        from .jd import JdTask
        category = kwargs.get('category')
        if category == 1:
            return object.__new__(JdTask, *args, **kwargs)

    def execute(self):
        raise NotImplementedError

    def query_by_playwright(self):
        pass