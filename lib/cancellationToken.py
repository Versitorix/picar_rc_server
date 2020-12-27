class CancellationToken(object):
    def __init__(self):
        self.isCancelled = False

    def cancel(self):
        self.isCancelled = True
