#coding:utf8

class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self,data):
        if data is None:
            retuen
        self.data.append(data)

    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.data:
            fout.write("<tr>")

            fout.write("<td>%s<td>" % data['url'])
            fout.write("<td>%s<td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s<td>" % data['summary'].encode('utf-8'))

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()