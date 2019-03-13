import cgi

def getData():
    formData = cgi.FieldStorage()
    favcolor = formData.getvalue('favcolor')
    return favcolor


#main

print("""content-type:text/html]\n\n 
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8/>
            </head>
        <body>""")

        favcolor = getData()
        print("Nice, I also like {}!".format(favcolor))
        print("""</body>
            </html>""")