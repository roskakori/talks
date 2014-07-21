"""
Example context manager to be used together with the ``with`` statement.
"""
import os


class CopyTask():
    def __init__(self, source_path, target_path):
        self.source_path = source_path
        self.target_path = target_path
        self._source_file = None
        self._target_file = None

        try:
            print('  open source %s' % source_path)
            self._source_file = open(source_path, 'rb')
            print('  open target %s' % target_path)
            self._target_file = open(target_path, 'wb')
        except:
            self.close()
            raise

    def run(self):
        BUFFER_SIZE = 1024
        buffer = self._source_file.read(BUFFER_SIZE)
        while len(buffer) > 0:
            self._target_file.write(buffer)
            buffer = self._source_file.read(BUFFER_SIZE)

    def close(self):
        """Release resources acquired by `__init__()`."""
        if self._target_file is not None:
            print('  close target %s' % self.target_path)
            self._target_file.close()
            self._target_file = None
        if self._source_file is not None:
            print('  close source %s' % self.source_path)
            self._source_file.close()
            self._source_file = None

    def __enter__(self):
        """Value ``with`` statement should assign to its target variable."""
        return self

    def __exit__(self, type, value, traceback):
        self.close()


class NaiveCopyTask():
    """
    A naive variant for CopyTask for illustrative purpose that does not
    cleanup properly if error happen during `__init__()`.
    """
    def __init__(self, source_path, target_path):
        print('  open source %s' % source_path)
        self._source_file = open(source_path, 'rb')
        print('  open target %s' % target_path)
        self._target_file = open(target_path, 'wb')

    def run(self):
        BUFFER_SIZE = 1024
        buffer = self._source_file.read(BUFFER_SIZE)
        while len(buffer) > 0:
            self._target_file.write(buffer)
            buffer = self._source_file.read(BUFFER_SIZE)

    def close(self):
        """Release resources acquired by `__init__()`."""
        print('  close target %s' % self.target_path)
        self._target_file.close()
        print('  close source %s' % self.source_path)
        self._source_file.close()


if __name__ == '__main__':
    test_path = 'some.txt'
    with open(test_path, 'w') as test_file:
        for line_number in range(1, 10000):
            test_file.write('this is line number %d' % line_number)
            test_file.write(os.linesep)

    print('example of a working CopyTask')
    with CopyTask('some.txt', 'copy_of_some.txt') as some_copy_task:
        some_copy_task.run()

    print('example of a working CopyTask without using with')
    another_copy_task = CopyTask('some.txt', 'copy_of_some.txt')
    try:
        another_copy_task.run()
    finally:
        another_copy_task.close()

    print('example of a broken CopyTask that cannot find the source')
    source_path = 'no_such_file.txt'
    target_path = 'copy_of_some.txt'
    try:
        with CopyTask(source_path, target_path) as broken_copy_task:
            assert False, 'copy fail'
    except IOError as error:
        print('as expected: cannot copy %s to %s: %s' % (source_path, target_path, error))

    print('example of a broken CopyTask that cannot open target but still closes the already opened source')
    source_path = 'some.txt'
    target_path = os.path.join('no_such_folder', 'copy_of_some.txt')
    try:
        with CopyTask(source_path, target_path) as broken_copy_task:
            assert False, 'copy must fail'
    except IOError as error:
        print('as expected: cannot copy %s to %s: %s' % (source_path, target_path, error))

    print('example for naive CopyTask (without proper cleanup in case of error')
    source_path = 'some.txt'
    target_path = 'copy_of_some.txt'
    with CopyTask(source_path, target_path) as naive_copy_task:
        naive_copy_task.run()
