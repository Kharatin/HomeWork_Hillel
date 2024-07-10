import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        pattern = r'<[^>]*>'
        html = re.sub(pattern, '', html)
        html = html.replace("  ", '', 1000).replace("   ", '', 1000).replace("\n\n\n", '', 50)
        print(html)

    with codecs.open(result_file, 'w', 'utf-8') as file2:
        html2 = file2.write(html)




doc = delete_html_tags(r"C:\Users\Maximus\Desktop\draft.html", r"C:\Users\Maximus\Desktop\cleaned.txt")


