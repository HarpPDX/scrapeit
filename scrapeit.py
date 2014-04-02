from urllib import urlopen

server = "http://programmer.97things.oreilly.com"
start_content = '<h1 class="firstHeading">' # "<!-- start content -->"
end_content = "<!-- end content -->"
#end_content = "This work is licensed unde"

doc=urlopen(server + "/wiki/index.php/Edited_Contributions")

urls=[]
newdoc=''
for line in doc.readlines():
    if -1 != line.find( '<li> <a href="/wiki/index.php/' ):
        firstquote = line.find('"')
        secondquote = line.find('"', firstquote + 1)
        urls.append(line[firstquote+1:secondquote])

print "<html>"
for url in urls:
    doc = urlopen(server + url).read()
    start = doc.find(start_content)
    end   = doc.find(end_content)
    #print "read " + server + url
    print doc[start:end]
print "</html>"

