# this file converts the raw Trump tweet data we found at https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FKJEBIL, which is in JSON format, the the desired format (just the tweet text separated by newlines)

import json

def main():
    in_file = './realdonaldtrump.ndjson'
    out_file = './donald_trump_data'
    f = open(in_file, 'r')
    lines = f.read().split('\n')
    f.close()
    f = open(out_file, 'w')
    for line in lines:
        if line:
            line_parsed = json.loads(line)
            if not line_parsed['truncated'] and line_parsed['user']['id'] == 25073877:  # 25073877 is Trump's Twitter id
                # print(json.dumps(json.loads(line), indent=4, sort_keys=True))
                f.write((json.loads(line)['text']).replace('\n', 'NEWLINE'))
                f.write('\n')
    f.close()

if __name__ == '__main__':
    main()