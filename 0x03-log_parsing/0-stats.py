#!/usr/bin/python3
''' A script that parses HTTP request logs '''
import re

def extract_input(input_line):
    '''Extractd sections of a line of HTTP request log '''
    hash_temp = (
                r'\s*(?P<ip>\S+)\s*',
                r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                r'\s*"(?P<request>[^"]*)"\s*',
                r'\s*(?P<status_code>\S+)',
                r'\s*(?P<file_size>\d+)'
            )
    info = {
            'status_code': 0,
            'file_size': 0,
            }
    log_form = '{}\\-{}{}{}{}\\s*'.format(hash_temp[0], hash_temp[1],
                                        hash_temp[2], hash_temp[3], hash_temp[0])
    resp_match = re.fullmatch(log_form, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info

def print_stats(total_size, status_stats):
    ''' Prints accumulates stats of HTTP req log '''
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_stats.keys()):
        n = status_stats.get(status_code, 0)
        if n > 0:
            print('{:s}: {:d}'.format(status_code, n), flush=True)


def update_lines(line, file_size, status_stats):
    ''' Updates metrics from HTTP request log.
    Args: line (str): Input line
    Returns: int: total file size
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_stats.keys():
        status_stats[status_code] += 1
    return file_size + line_info['file_size']

if __name__ == '__main__':
    ''' Starts the log parsing '''
    line = 0
    file_size = 0
    status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
    }
    try:
        while True:
            line = input()
            file_size = update_lines(line, file_size, status_codes_stats)
            line += 1
            if line % 10 == 0:
                print_stats(file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes_stats)
