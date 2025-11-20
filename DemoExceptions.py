import sys
import traceback as tb

try:
    dividend = int(input('Enter a dividend '))
    divisor = int(input('Enter a divisor '))
    result = dividend / divisor
    print(result)
except ZeroDivisionError as e:
    print(e)  # prints the cause of execution
    e_type, e_cause, e_trace, = sys.exc_info()
    print(f'{e_type} , {e_cause}')  # prints the class and cause of exception
except ValueError as e:
    print(e)
    print(tb.print_exc())  # prints the stacktrace
    tb.print_exception(e)  # prints the stacktrace
else:
    print('Try is successful')
finally:
    print('Always executes')

