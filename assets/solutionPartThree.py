#!/usr/bin/python2


__author__ = 'Taylor Lee'
__email__  = 'tdlee2@wisc.edu'


import re
import sys

# Assumptions: the log file is in the same format as the one provided, including the entries being recorded in chronological order.
# I'm also assuming that the entire log file can fit in memory at once.


class CondorError:

    def __init__(self, error_text, job_id, error_time):
        self.error_text = error_text
        self.job_id_list = [job_id]
        self.least_recent = error_time
        self.most_recent  = error_time
        self.number_of_occurences = 1

    def update(self, job_id, error_time):
        if job_id not in self.job_id_list:
            self.job_id_list.append(job_id)
        self.most_recent = error_time         # Simply updating most recent time, as I assume we are going through the log chronologically
        self.number_of_occurences += 1

    def display(self):
        print self.error_text
        print '- Occured ' + str(self.number_of_occurences) + ' times from ' + self.least_recent + ' to ' + self.most_recent
        print '- Affected ' + str(len(self.job_id_list)) + ' unique jobs\n\n'



def main(file_name):
    fh = open(file_name)
    data_list = fh.read().split('\n...\n')  # Split entire file by entry
    error_dict = {}
    for entry in data_list:
        if entry[0:3] == '007':
            this_data = [line.strip() for line in entry.split('\n')]
            error_text = this_data[1]
            (job_id, error_date, error_time)  = re.split('\s+',this_data[0])[1:4]  # error date not used
            job_id = job_id.strip('()').split('.')[0]
            if error_text not in error_dict:
                error_dict[error_text] = CondorError(error_text, job_id, error_time)
            else:
                error_dict[error_text].update(job_id, error_time)
    for error in error_dict:
        error_dict[error].display()


if __name__ == '__main__':
    main(sys.argv[1])
