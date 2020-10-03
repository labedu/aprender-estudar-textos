# 4. Split paragraphs
from formatacao.data.texts_example import text_exe_03


def split_paragraphs(text):
    text = '\n \n ' + text + '\n \n ' # allow closing a paragraph
    title, subtitle = "", ""
    pars = []
    par = ""
    in_header = True
    in_par = False

    text = text.split('\n')

    for t in text:
        line = t.strip()

        if in_header:
            if len(line) > 0:
                if line[0] != '#':
                    in_header = False
                    in_par = True
                elif len(line) > 1 and line[:2] == '##':
                    subtitle = line[2:].strip()
                else:
                    title = line[1:].strip()
        else:
            if len(line) > 0:
                in_par = True

        if in_par: # inside a paragraph
            if len(line) > 0: #still in a paragraph
                if par != '':
                    par += '\n' + line
                else:
                    par += line
            else: # runned out a paragraph
                pars.append(par)
                par = ''
                in_par = False

    return title, subtitle, pars


if __name__ == '__main__':
    title, subtitle, pars = split_paragraphs(text_exe_03)
    print('title', title)
    print('subtitle', subtitle)
    print(len(pars))
    for i, p in enumerate(pars):
        print('\n=par{}\n{}'.format(i,p))