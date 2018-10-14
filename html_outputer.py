#html输出
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=open('output.html','w',encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>")
            fout.write(data['url'])
            fout.write("</td>")
            fout.write("<td>")
            fout.write(data['title'])
            fout.write("</td>")
            fout.write("<td>")
            fout.write(data['summary'])
            fout.write("</td>")
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
