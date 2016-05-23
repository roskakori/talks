"""
Example to run several shell commands in parallel and summarize the result.

Modify this to your own needs:
* Possibly change parameters and add instance variables to ``__init__()``.
* Add the desired shell commands to ``run()``.
"""
import logging
import random
import subprocess
import sys
import threading

_log = logging.getLogger('shell_threads')


class CommandThread(threading.Thread):
    def __init__(self, name, time_to_wait):
        super().__init__(name=name)
        self.error = None
        self._time_to_wait = time_to_wait

    def run(self):
        _log.info('%s: wait for %d second(s)', self.name, self._time_to_wait)
        try:
            subprocess.check_call(['sleep', str(self._time_to_wait)])
            if random.randint(0, 100) <= 20:
                # Randomly make a command fail.
                raise ValueError('command failed as specified')
            _log.info('%s: done', self.name)
        except Exception as error:
            _log.error('%s: failed: %s', self.name, error)
            self.error = error


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Build and start threads to run shell commands.
    command_threads = []
    for thread_number in range(10):
        name = 'command.%d' % thread_number
        time_to_wait = random.randint(1, 5)
        command_thread = CommandThread(name, time_to_wait)
        command_threads.append(command_thread)
        command_thread.start()

    # Wait for the commands to finish and count number of failures.
    failed_commands_count = 0
    for command_thread in command_threads:
        command_thread.join()
        if command_thread.error is not None:
            failed_commands_count += 1

    # Summarize result.
    command_count = len(command_threads)
    _log.info(
        '%d of %d commands ran successfully',
        command_count - failed_commands_count, command_count)

    sys.exit(0 if failed_commands_count == 0 else 1)
