'''
    Siyan
    CS5001
    Fall 2018
    November 30, 2018
'''

'''
This module contains score-related functions used by Othello game
'''

# Define the file name of the scores file as constant
SCORE_FILE = 'scores.txt'

def read_scores(filename=SCORE_FILE):
    ''' Function read_scores
        Parameters: filename (string, optional)
        Returns: data, a string read from the file 
                 (returns nothing but exit gracefully if error occurs)
        
        Does: Reads all scores from the score file (​one score per line with 
              a space between the user’s name and their score) to a single 
              string, and returns the string. Linebreaks are reserved. 
              However, if the file does not exist, returns empty string; 
              if the file cannot be read, returns nothing.
    '''
    try:
        infile = open(filename, 'r')
        data = infile.read()
        infile.close()
        return data
    except FileNotFoundError:
        return ''
    except OSError:
        print('Error reading the score file.')
        return
    
def write_scores(new_data, filename=SCORE_FILE, mode='a'):
    ''' Function write_scores
        Parameters: new_data (string), filename (string, optional), 
                    mode (string, 'a' or 'w')
        Returns: nothing

        Does: Writes new score data to the score file. If the file already 
              exists, writes at the end of the file for mode='a', or 
              rewrites the file for mode='w'; creates and writes the file 
              if it doesn’t exist. Reports error and returns empty string
              if the file cannot be written.
    '''
    try:
        outfile = open(filename, mode)
        outfile.write(new_data)
        outfile.close()
    except OSError:
        print('Error updating the score file.')
        return ''

def update_scores(name, score, filename=SCORE_FILE):
    ''' Function update_scores
        Parameters: name (string), score (integer), 
                    filename (string, optional)
        Returns: new_record (string)

        Does: Updates the score file. The format is one score per line with 
              a space between the user’s name and their score. Appends a 
              linebreak if the last line ends with no linebreak. The highest 
              score is ​always t​he first entry in the file. If the user is 
              the new high-scorer, writes their name with the score in the 
              first line of the file; otherwise, they go at the end. 
              Returns user's record in string if updating successfully; 
              otherwise, reports error and returns empty string.
    '''
    new_record = name + ' ' + str(score)
    new_data = new_record + '\n'
    scores_data = read_scores(filename)

    if scores_data == None:
        return ''

    if scores_data:
        records = scores_data.splitlines()
        high_scorer = records[0].rsplit(' ', 1)
        try:
            highest_score = int(high_scorer[1])
            if score > highest_score:
                scores_data = new_data + scores_data
                if write_scores(scores_data, filename, 'w') == '':
                    return ''
                else:
                    return new_record
        except ValueError:
            print('Unknown format for the score file.')
            return ''
        if scores_data[-1] != '\n':
            new_data = '\n' + new_data
    
    if write_scores(new_data, filename) == '':
        return ''
    else:
        return new_record
